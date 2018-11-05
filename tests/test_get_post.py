import pytest
import jsonschema


def test_post_response_code(get_post_by_id):
    assert 200 == get_post_by_id.status_code


@pytest.mark.parametrize('post_id', ['1', '50', '100'], indirect=['post_id'])
def test_response_json_schema(get_post_by_id, post_id, single_post_schema):
    jsonschema.validate(get_post_by_id.json(), single_post_schema)


@pytest.mark.parametrize('post_id', ['1', '35', '100'], indirect=['post_id'])
def test_request_url_index_matches_with_response_json_id_value(get_post_by_id, post_id):
    assert get_post_by_id.json()['id'] == int(post_id)


@pytest.mark.parametrize('post_id', ['1', '35', '100'], indirect=['post_id'])
def test_response_json_matches_with_all_posts_response_element_with_same_id(all_posts, get_post_by_id, post_id):
    assert get_post_by_id.json() == all_posts.json()[get_post_by_id.json()['id']-1]


@pytest.mark.parametrize('post_id', ['-1', '0', '101'], indirect=['post_id'])
def test_request_url_index_invalid_values(get_post_by_id, post_id):
    assert 404 == get_post_by_id.status_code
