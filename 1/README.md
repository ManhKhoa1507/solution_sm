1. You have 3 Availability Zones (AZs) with n Private Subnets, and m NAT Instances per AZ. Private Subnets need to route traffic through NAT Instances which block any traffic not going to a whitelisted domain. 
For HA we have to dynamically allocate private subnets to NAT Instances. First of all, we need to allocate subnets to NAT Instances within the same AZ. If there are no healthy NAT Instances in the same AZ, only then will we allocate subnets to any NAT Instance in any other AZ.

- We can have multiple NAT Instances per AZ
- NAT Instances may fail, resulting in AZs with fewer or no NAT Instances. 
- If there are no NAT Instances in an AZ, the private subnets of that AZ should be allocated to egress via available NAT Instances in other AZs. 
- If there is still at least 1 NAT Instance in an AZ, the subnets of that AZ should still be allocated to that NAT Instance which is in the same AZ
- We try to have as close to the same number of private subnets allocated to each NAT Instance. But allocation to a NAT Instance in the same AZ takes priority.

If you use Golang, you can use the following playground to implement function

https://play.golang.org/p/zYJ-bf_MDBg

Possible problem and solution:
   
```
   # problem
   NATInstances:
     1 - us-west1-a
     2 - us-west1-b
     3 - us-west1-b
   
   Subnets:
     1 - us-west1-a
     2 - us-west1-b
     3 - us-west1-b
     4 - us-west1-c
   
   # solution
   Instance (1 - us-west1-a):
	subnet (1 - us-west1-a)
	subnet (4 - us-west1-c)
   Instance (2 - us-west1-b):
	subnet (2 - us-west1-b)
   Instance (3 - us-west1-b):
	subnet (3 - us-west1-b)
```
 Bonus: What if each Subnet has a `Weight int32` attribute and we try to make total weight allocated to each NAT Instance the same no matter how subnets allocated to each NAT Instance?

# Solutions for problems 1:



I have 2 solutions for this, but the time is limited, So I decide to implement with the bonus point **Bonus: What if each Subnet has a `Weight int32` attribute and we try to make total weight allocated to each NAT Instance the same no matter how subnets allocated to each NAT Instance?**

2 solutions I will brief above:


The complex of this code is O(n*m)
```bash
❯ python3 solve.py
Enter number of nat:4
This NAT id belongs to instance: us-west1-a
This NAT id belongs to instance: us-west1-a
This NAT id belongs to instance: us-west1-a
This NAT id belongs to instance: us-west1-b
Enter number of subnet of zone:5
0-subnet  belongs to instance: us-west1-a
Weight: 10
1-subnet  belongs to instance: us-west1-a
Weight: 1
2-subnet  belongs to instance: us-west1-a
Weight: 9
3-subnet  belongs to instance: us-west1-b
Weight: 20
4-subnet  belongs to instance: us-west1-c
Weight: 10

## Output

NAT in zone us-west1-a:
[['us-west1-a-0', 10], ['us-west1-a-1', 11], ['us-west1-a-2', 9]]
NAT in zone us-west1-b:
[['us-west1-b-3', 20]]
NAT in zone us-west1-c:
[]
['us-west1-a-0', 10, 'us-west1-a-0']
['us-west1-a-1', 1, 'us-west1-a-1']
['us-west1-a-2', 9, 'us-west1-a-2']
['us-west1-b-3', 20, 'us-west1-b-3']
['us-west1-c-4', 10, 'us-west1-a-1']
```
