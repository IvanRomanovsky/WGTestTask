import requests

HOST = 'jsonplaceholder.typicode.com'


def get_list_posts(headers=None):
    command = 'posts'
    url = 'https://{}/{}'.format(HOST, command)
    response = requests.get(url, headers=headers)
    return response


def get_single_post(num: int, headers=None):
    command = 'posts/{}'.format(num)
    url = 'https://{}/{}'.format(HOST, command)
    response = requests.get(url, headers=headers)
    return response


def get_post_comments(num: int, headers=None):
    command = 'posts/{}/comments'.format(num)
    url = 'https://{}/{}'.format(HOST, command)
    response = requests.get(url, headers=headers)
    return response
