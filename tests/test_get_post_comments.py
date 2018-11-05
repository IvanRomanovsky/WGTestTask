import jsonschema
import pytest
import re

from tests.conftest import HOST


def test_comments_response_code(get_comments_by_id):
    assert 200 == get_comments_by_id.status_code


@pytest.mark.parametrize('post_id', ['1', '50', '100'], indirect=['post_id'])
def test_response_json_schema(get_comments_by_id, post_id, post_comment_schema):
    jsonschema.validate(get_comments_by_id.json(), post_comment_schema)


def test_comments_ids_through_numbering(api_get_call, user_agents):
    headers = {'User-Agent': user_agents}
    comments = []
    for i in range(1, 6):
        comments.append(api_get_call(HOST, ['posts', str(i), 'comments'], headers=headers).json())
    comments = sum(comments, [])

    _ids = [comment['id'] for comment in comments]

    assert all(_ids[i] <= _ids[i + 1] for i in range(len(_ids) - 1)), 'comments ids have not through numbered'


@pytest.mark.parametrize('post_id', ['1', '50', '100'], indirect=['post_id'])
def test_validate_email(get_comments_by_id, post_id):
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    for comment in get_comments_by_id.json():
        assert email_regex.match(comment['email'])


@pytest.mark.parametrize('post_id', ['-1', '0', '101'], indirect=['post_id'])
def test_request_url_index_invalid_values(get_comments_by_id, post_id):
    assert get_comments_by_id.status_code == 200  # current behavior
    assert len(get_comments_by_id.json()) == 0
