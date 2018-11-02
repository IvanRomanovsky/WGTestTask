SINGLE_POST_SCHEMA = {
    'type': 'object',
    'properties': {
        'userId': {'type': 'number'},
        'id': {'type': 'number'},
        'title': {'type': 'string'},
        'body': {'type': 'string'}
       }
    }


LIST_POSTS_SCHEMA = {
    'type': 'array',
    'items': SINGLE_POST_SCHEMA
}


POST_COMMENT_SCHEMA = {
    'type': 'object',
    'properties': {
        'postId': {'type': 'number'},
        'id': {'type': 'number'},
        'name': {'type': 'string'},
        'email': {'type': 'string'},
        'body': {'type': 'string'}
    }
}
