import requests
import logging
import os
from flask import Flask, request, jsonify, Response
from prometheus_client import start_http_server, Gauge, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware


app = Flask(__name__)
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

# Provider API
ANKR_API = "https://rpc.ankr.com/eth"
INFURA_API = "https://mainnet.infura.io/v3/ec00a294dc2f419e99d5b2d08317f441"

ankr_number_gauge = Gauge('ankr_number', 'number of Ankr block')
infura_number_gauge = Gauge('infura_number', 'number of Infura block')
block_status_gauge = Gauge('block_status', 'Status of the block number check (1 = success, 0 = fail)')


# Data to make requests
data = {
    "jsonrpc": "2.0",
    "method": "eth_blockNumber",
    "params": [],
    "id": 1
}

logging.basicConfig(
    format='[%(levelname)s] - %(message)s', level=logging.INFO)

# @app.route('/metrics', methods=['GET'])
# def metrics_handler():
#     infura_block = get_infura_block_num()
#     ankr_block = get_ankr_block_num()
#     status, _ = get_status()
#
#     infura_number_gauge.set(infura_block)
#     ankr_number_gauge.set(ankr_block)
#     block_status_gauge.set(status)
#
#     return Response('Metrics', status=200)

@app.route('/health', methods=['GET'])
def health_check():
    _, status = get_status()
    target_group = [
        {
            "targets": ["app:8080"],
            "labels": {
                "job": "block_check",
                "status": status,
            },
        }
    ]
    return jsonify(target_group)


def get_status():
    infura_block = get_infura_block_num()
    ankr_block = get_ankr_block_num()

    logging.info(f"infura_block: { infura_block}")
    logging.info(f"ankr_block: { ankr_block}")

    infura_number_gauge.set(infura_block)
    ankr_number_gauge.set(ankr_block)

    if ankr_block - infura_block < 5:
        block_status_gauge.set(1)
        return 1, "success"

    block_status_gauge.set(0)
    return 0, "failed"


def get_ankr_block_num():
    ankr_res = make_requests(ANKR_API)
    return get_number_in_response(ankr_res)


def get_infura_block_num():
    infura_res = make_requests(INFURA_API)
    return get_number_in_response(infura_res)


def make_requests(api):
    try:
        r = requests.post(api, json=data)
        return r.json()

    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to make requests to {api}: {e}")


def get_number_in_response(response):
    hex_number = response['result']
    return int(hex_number, 16)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
