from sys import argv

usage = 'usage: python cds1.py <authorization token> ' + \
        '<load balancer ID> <droplet ID>'

if len(argv) != 4:
    print(usage)
token, balancer_id, droplet_id = argv[1:]
# TODO

