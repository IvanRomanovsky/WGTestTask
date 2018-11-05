import jsonschema
import pytest


def test_response_code(all_posts):
    assert 200 == all_posts.status_code


def test_response_json_schema(all_posts, posts_list_schema):
    jsonschema.validate(all_posts.json(), posts_list_schema)


def test_response_json_sorting(all_posts):
    def validate_sorting(response_body):
        ids = [post['id'] for post in response_body]
        user_ids = [post['userId'] for post in response_body]
        assert all(ids[i] <= ids[i + 1] for i in range(len(ids) - 1)), 'posts are not sorted by id'
        assert all(user_ids[i] <= user_ids[i + 1] for i in range(len(user_ids) - 1)), 'posts are not sorted by userId'

    validate_sorting(all_posts.json())


@pytest.mark.parametrize('headers, response', [({'Accept-Encoding': 'gzip'}, {'Content-Encoding': 'gzip'}),
                                               ({'Accept-Encoding': 'br'}, {'Content-Encoding': 'gzip'})], indirect=['headers'])
def test_response_with_custom_request_headers(all_posts, response):
    for key in response.keys():
        assert all_posts.headers[key] == response[key]


def test_response_header(all_posts):
    expected_values = {'Content-Encoding': 'gzip',
                       'X-Content-Type-Options': 'nosniff',
                       'Expect-CT': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"',
                       'Content-Type': 'application/json; charset=utf-8',
                       'X-Powered-By': 'Express',
                       'Vary': 'Origin, Accept-Encoding',
                       'CF-Cache-Status': 'HIT',
                       'Access-Control-Allow-Credentials': 'true',
                       'Connection': 'keep-alive',
                       'Cache-Control': 'public, max-age=14400',
                       'Server': 'cloudflare',
                       'Transfer-Encoding': 'chunked',
                       'Pragma': 'no-cache',
                       'Via': '1.1 vegur'}

    for key in expected_values.keys():
        assert all_posts.headers[key] == expected_values[key]
