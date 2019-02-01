from os import path, makedirs

LOG_PATH = '/home/oxadmin/ox/logs'

if not path.exists(LOG_PATH):
    makedirs(LOG_PATH)

import logging
logging.basicConfig(level=logging.DEBUG, filename=LOG_PATH + '/cds1.log')
logging.debug('starting cds1.py')

from sys import argv
from requests import get, delete
from json import loads
from time import sleep

# The load balancer pool must always have at least this many app hosts.
MINIMUM_HOSTS = 1


# TODO: maybe don't use imported module names as local variables
def count_droplets(path, headers):
    response = loads(get(path, headers=headers).text)
    logging.info('requested load balancer information from Digital Ocean')
    return len(response['load_balancer']['droplet_ids'])


USAGE = 'usage: python cds1.py <authorization token> ' + \
        '<load balancer ID> <droplet ID>'

if len(argv) != 4:
    print(USAGE)
else:
    # TODO: error handling
    token, balancer_id, droplet_id = argv[1:]
    path_prefix = 'https://api.digitalocean.com/v2/load_balancers/'
    path = path_prefix + balancer_id
    headers = {'Authorization': 'Bearer ' + token}
    #while count_droplets(path, headers) <= MINIMUM_HOSTS:
    #    sleep(5)
    json = {'droplet_ids': [droplet_id]}
    #delete(path + '/droplets', headers=headers, json=json)
    #logging.info('requested Digital Ocean to remove droplet from balancer')
logging.debug('cds1.py completed')

