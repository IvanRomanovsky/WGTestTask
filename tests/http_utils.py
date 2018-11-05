import requests


def http_get(host: str, args: list, headers=None):
    command = '/'.join(args)
    url = 'https://{}/{}'.format(host, command)
    return requests.get(url, headers)
