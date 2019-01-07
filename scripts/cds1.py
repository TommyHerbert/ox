from sys import argv
from requests import get
from json import loads
from time import sleep

# The load balancer pool must always have at least this many app hosts.
MINIMUM_HOSTS = 1


def count_droplets(path, headers):
    response = loads(get(path, headers=headers).text)
    return len(response['load_balancer']['droplet_ids'])


USAGE = 'usage: python cds1.py <authorization token> ' + \
        '<load balancer ID> <droplet ID>'

if len(argv) != 4:
    print(USAGE)
token, balancer_id, droplet_id = argv[1:]
path_prefix = 'https://api.digitalocean.com/v2/load_balancers/'
path = path_prefix + balancer_id
headers = {'Authorization': 'Bearer ' + token}
while count_droplets(path, headers) <= MINIMUM_HOSTS:
    print('Insufficient droplets in load balancer pool. Waiting for more.')
    sleep(5)
print('There are now enough droplets. We can remove this one.')

