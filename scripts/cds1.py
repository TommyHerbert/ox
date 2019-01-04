from sys import argv

usage = 'usage: python cds1.py <authorization token> ' + \
        '<load balancer ID> <droplet ID> ' + \
        '[<minimum number of hosts in pool>]'

if len(argv) not in [4, 5]:
    print(usage)
token, balancer_id, droplet_id = argv[1:]
# TODO

