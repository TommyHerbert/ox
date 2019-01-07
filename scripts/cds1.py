from sys import argv
from requests import get, delete
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
else:
    # TODO: logging and error handling
    token, balancer_id, droplet_id = argv[1:]
    path_prefix = 'https://api.digitalocean.com/v2/load_balancers/'
    path = path_prefix + balancer_id
    headers = {'Authorization': 'Bearer ' + token}
    while count_droplets(path, headers) <= MINIMUM_HOSTS:
        sleep(5)
    json = {'droplet_ids': [droplet_id]}
    delete(path + '/droplets', headers=headers, json=json)

