from sys import argv
from requests import get
from json import loads

usage = 'usage: python cds1.py <authorization token> ' + \
        '<load balancer ID> <droplet ID>'

if len(argv) != 4:
    print(usage)
token, balancer_id, droplet_id = argv[1:]
path_prefix = 'https://api.digitalocean.com/v2/load_balancers/'
path = path_prefix + balancer_id
headers = {'Authorization': 'Bearer ' + token}
response = loads(get(path, headers=headers).text)
droplet_ids = response['load_balancer']['droplet_ids']
print('there are {} droplets in the load balancer'.format(len(droplet_ids)))

# TODO

