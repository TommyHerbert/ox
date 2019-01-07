from sys import argv
from requests import get
from json import loads

# The load balancer pool must always have at least this many app hosts.
MINIMUM_HOSTS = 1

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
droplet_count = len(droplet_ids)
print('there are {} droplets in the load balancer'.format(droplet_count))
if droplet_count > MINIMUM_HOSTS:
    print('So we can afford to remove this one temporarily.')
else:
    message = 'So we must wait for more droplets to add ' + \
              'themselves before we remove this one.'
    print(message)

# TODO

