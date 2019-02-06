from os import makedirs
from os.path import exists, join
import logging
from sys import argv
from requests import post

LOG_PATH = '/home/oxadmin/ox/logs'
USAGE = 'usage: python cds1.py <authorization token> ' + \
        '<load balancer ID> <droplet ID>'

if not exists(LOG_PATH):
    makedirs(LOG_PATH)
logging.basicConfig(level=logging.DEBUG, filename=join(LOG_PATH, 'cds3.log'))
logging.info('starting cds3.py')

if len(argv) != 4:
    log.error('wrong number of arguments')
    print(USAGE)
else:
    token, balancer_id, droplet_id = argv[1:]
    uri_template = 'https://api.digitalocean.com/v2/load_balancers/{}/droplets'
    uri = uri_template.format(balancer_id)
    headers = {'Authorization': 'Bearer ' + token}
    json = {'droplet_ids': [droplet_id]}
    post(uri, headers=headers, json=json)
    logging.info('asked Digital Ocean to add droplet to balancer')

logging.info('cds3.py completed')

