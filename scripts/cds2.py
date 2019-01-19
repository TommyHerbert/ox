from os import path, makedirs

LOG_PATH = '/home/oxadmin/ox/logs'

if not path.exists(LOG_PATH):
    makedirs(LOG_PATH)

import logging

logging.basicConfig(level=logging.INFO, filename=LOG_PATH + '/cds2.log')

logging.info('started cds2')

import knowledge

logging.info('completed cds2')
