# list NAT, subnet
nat = []
subnet = []

nat_A = []
nat_B = []
nat_C = []

nat_by_az = {"us-west1-a": [], "us-west1-b": [], "us-west1-c": []}


def solve():
    get_input()
    map_subnet_nat()

    # Print weight of each nat
    print("NAT in zone us-west1-a:")
    print(nat_A)

    print("NAT in zone us-west1-b:")
    print(nat_B)

    print("NAT in zone us-west1-c:")
    print(nat_C)

    # Print subnet belongs to nat ?
    print("[sub_id, weight, belong_to_nat]")
    for sub in subnet:
        print(sub)

def get_input():
    # Get NAT
    num_nat = int(input(f"Enter number of nat:"))
    for i in range(num_nat):
        e = input("This NAT id belongs to instance: ")
        nat_id = f"{e}-{i}"
        nat_weight = 0
        if "us-west1-a" in nat_id:
            nat_A.append([nat_id, nat_weight])
        if "us-west1-b" in nat_id:
            nat_B.append([nat_id, nat_weight])
        if "us-west1-c" in nat_id:
            nat_C.append([nat_id, nat_weight])

    # Get subnet
    num_sub = int(input(f"Enter number of subnet of zone:"))
    for i in range(num_sub):
        id = input(f"{i}-subnet  belongs to instance: ")
        weight = int(input("Weight: "))
        nat_id = None

        sub = [f"{id}-{i}", weight, nat_id]
        subnet.append(sub)


def map_subnet_nat():
    for sub in subnet:
        # Get sub_id, sub_weight
        sub_id = sub[0]
        sub_weight = sub[1]

        nat_list = get_nat_list(sub_id)

        # Get min least nat, then append subnet to the least weight nat
        pos = find_min_nat(nat_list)
        add_subnet_to_nat(sub, nat_list, pos)


def get_nat_list(sub_id):
    # Get that nat_list base on sub_id
    # If nat_X down -> return 2 others NAT
    if "us-west1-a" in sub_id:
        if len(nat_A) == 0:
            return nat_B + nat_C
        return nat_A
    if "us-west1-b" in sub_id:
        if len(nat_B) == 0:
            return nat_A + nat_C
        return nat_B
    if "us-west1-c" in sub_id:
        if len(nat_C) == 0:
            return nat_B + nat_A
        return nat_C


def find_min_nat(nat_list):
    # Find the least weight NAT_id in nat_list
    # Return index of nat_list

    min_value = nat_list[0][1]
    index = 0

    for i in range(len(nat_list)):
        if min_value > nat_list[i][1]:
            min_value = nat_list[i][1]
            index = i

    return index


def add_subnet_to_nat(sub, nat_list, index):
    sub_weight = sub[1]
    sub[2] = nat_list[index][0]

    nat_list[index][1] += sub_weight

solve()
