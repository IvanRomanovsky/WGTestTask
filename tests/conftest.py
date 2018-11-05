import pytest

from tests.http_utils import http_get

pytest_plugins = ['user_agent_fixtures', 'json_validate_schema_fixtures']

HOST = 'jsonplaceholder.typicode.com'


@pytest.fixture(scope='session')
def api_get_call():
    return http_get


@pytest.fixture(params=['user_agents'])
def all_posts(api_get_call, request, user_agents, headers):
    headers['User-Agent'] = request.getfixturevalue(request.param)
    return api_get_call(host=HOST, args=['posts'], headers=headers)


@pytest.fixture()
def headers(request):
    headers = {}
    if hasattr(request, 'param'):
        for key, value in request.param.items():
            headers[key] = value
    return headers


@pytest.fixture()
def post_id(request):
    _id = '1'
    if hasattr(request, 'param'):
        _id = request.param
    return _id


@pytest.fixture(params=['user_agents'])
def get_post_by_id(api_get_call, post_id, request, user_agents, headers):
    headers['User-Agent'] = request.getfixturevalue(request.param)
    return api_get_call(host=HOST, args=['posts', post_id], headers=headers)


@pytest.fixture(params=['user_agents'])
def get_comments_by_id(api_get_call, post_id, user_agents, request, headers):
    headers['User-Agent'] = request.getfixturevalue(request.param)
    return api_get_call(host=HOST, args=['posts', post_id, 'comments'], headers=headers)
