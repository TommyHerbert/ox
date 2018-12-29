import time
from threading import Thread
import requests
from json import loads

path_prefix = 'https://api.digitalocean.com/v2/load_balancers/'


def get_time_string():
    return time.ctime(time.time())


def build_headers(token):
    return {'Authorization': 'Bearer ' + token}


def remove_droplet(balancer_id, droplet_id, headers):
    print('time before removing droplet: ' + get_time_string())
    body = {'droplet_ids': [droplet_id]}
    path = path_prefix + balancer_id + '/droplets'
    requests.delete(path, headers=headers, json=body)
    print('time after removing droplet: ' + get_time_string())


def get_droplets(balancer_id, headers):
    print('time before getting droplets: ' + get_time_string())
    response = requests.get(path_prefix + balancer_id, headers=headers).text
    print('droplets: ' + str(loads(response)['load_balancer']['droplet_ids']))
    print('time after getting droplets: ' + get_time_string())


class RemovalThread()


def run(balancer_id, droplet_id, headers):
    print 'starting removal thread'
    

