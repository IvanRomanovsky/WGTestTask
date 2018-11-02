from src.http_requests import get_list_posts, get_post_comments, get_single_post
from tests.data import *


@pytest.fixture(scope='session', params=['user_agents'])
def all_posts_full_response(request):
    # user_agent = request.getfixturevalue(request.param)
    # return get_list_posts(headers={'User-Agent': user_agent})
    return get_list_posts()

@pytest.fixture
def all_posts_code(request, all_posts_full_response):
    return all_posts_full_response.status_code


@pytest.fixture
def all_posts_header(all_posts_full_response):
    return all_posts_full_response.headers


@pytest.fixture(scope='session')
def all_posts_body(all_posts_full_response):
    return all_posts_full_response.json()


@pytest.fixture(scope='session')
def get_posts_one_by_one_full_response(all_posts_body):
    result = []
    for post in all_posts_body:
        result.append(get_single_post(post['id']))
    return result


@pytest.fixture()
def get_posts_one_by_one_codes(get_posts_one_by_one_full_response):
    return [response.status_code for response in get_posts_one_by_one_full_response]


@pytest.fixture()
def get_posts_one_by_one_headers(get_posts_one_by_one_full_response):
    return [response.headers for response in get_posts_one_by_one_full_response]


@pytest.fixture()
def get_posts_one_by_one_body(get_posts_one_by_one_full_response):
    return [response.json() for response in get_posts_one_by_one_full_response]


def post_comments():
    pass