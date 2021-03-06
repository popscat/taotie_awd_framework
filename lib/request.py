import requests
from lib.logger import log
def get(**args):
    try:
        return requests.get(timeout=3,**args)
    except requests.Timeout:
        log.debug('Http requests to {} Timeout'.format(args['url']))

def post(**args):
    try:
        return requests.post(timeout=3,**args)
    except requests.Timeout:
        log.debug('Http requests to {} Timeout'.format(args['url']))

def request(**args):
    try:
        return requests.request(timeout=3,**args)
    except requests.Timeout:
        log.debug('Http requests to {} Timeout'.format(args['url']))