from os import path, makedirs

LOG_PATH = '/home/oxadmin/ox/logs'

if not path.exists(LOG_PATH):
    makedirs(LOG_PATH)

import logging

logging.basicConfig(filename=LOG_PATH + '/cds2.log')

import knowledge

logging.info('hello world')
