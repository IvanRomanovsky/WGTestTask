import pytest


SINGLE_POST_SCHEMA = {
    'type': 'object',
    'properties': {
        'userId': {'type': 'number'},
        'id': {'type': 'number'},
        'title': {'type': 'string'},
        'body': {'type': 'string'}
       },
    'required': ['userId', 'id', 'body', 'title']
    }


POSTS_LIST_SCHEMA = {
    'type': 'array',
    'items': SINGLE_POST_SCHEMA
}


POST_COMMENT_SCHEMA = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'postId': {'type': 'number'},
            'id': {'type': 'number'},
            'name': {'type': 'string'},
            'email': {'type': 'string'},
            'body': {'type': 'string'}
            },
        'required': ['postId', 'id', 'name', 'body', 'email']
    }
}


@pytest.fixture(scope='session')
def single_post_schema():
    return SINGLE_POST_SCHEMA


@pytest.fixture(scope='session')
def posts_list_schema():
    return POSTS_LIST_SCHEMA


@pytest.fixture(scope='session')
def post_comment_schema():
    return POST_COMMENT_SCHEMA
