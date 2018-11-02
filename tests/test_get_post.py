import pytest
import jsonschema

from src.json_schema import SINGLE_POST_SCHEMA
from src.http_requests import get_single_post

def test_response_json_schema(get_posts_one_by_one_body):
    for post in get_posts_one_by_one_body:
        jsonschema.validate(post, SINGLE_POST_SCHEMA)


def test_request_url_index_matches_with_response_json_id_value():
    pass


def test_response_json_matches_with_all_posts_response_element_with_same_id(all_posts_body, get_posts_one_by_one_body):
    assert all_posts_body == get_posts_one_by_one_body


@pytest.mark.parametrize('num', [-1, 0, 101])
def test_request_url_index_invalid_values(num):
    response = get_single_post(num, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
    assert response.status_code == 200
    assert response.json() == {}
    assert response.headers['content-lenght'] == 2