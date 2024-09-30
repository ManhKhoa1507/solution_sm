Write an application [http sd exporter](https://prometheus.io/docs/prometheus/latest/http_sd/). 

Your application needs write blackbox exporter check the difference in block number between two providers Ankr and Infura.:
-   if Ankr blocknumber - Infura blocknumber < 5 => success
-   else => fail

We're assuming that Infrura is the trusted source for checking the block number.

Note: Infura for sign up free account and docs https://www.ankr.com/rpc/eth/ and https://docs.infura.io/

Example: Get blocknumber with curl
```
curl https://mainnet.infura.io/v3/ID
-X POST \
-H "Content-Type: application/json" 
-d '{ 
 "jsonrpc": "2.0", 
 "method": eth_blockNumber, 
 "params": [], 
 "id": 1, 
}'
```
Please submit a link to a public GitHub repository with the source code of your solution. As an alternative, you may send a tar archive by email, but this is discouraged.


https://medium.com/@squadcast/prometheus-blackbox-exporter-a-guide-for-monitoring-external-systems-a8fff19a8bd0

# Solution

