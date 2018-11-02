import jsonschema

from src.json_schema import LIST_POSTS_SCHEMA
from src.http_requests import get_list_posts


def validate_sorting(body):
    ids = [post['id'] for post in body]
    user_ids = [post['userId'] for post in body]
    assert all(ids[i] <= ids[i+1] for i in range(len(ids)-1)), 'posts are not sorted by id'
    assert all(user_ids[i] <= user_ids[i+1] for i in range(len(user_ids)-1)), 'posts are not sorted by userId'


def test_response_header(all_posts_header):
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
        assert all_posts_header[key] == expected_values[key]



def test_response_code(all_posts_code):
    assert all_posts_code == 200


def test_response_json_schema(all_posts_body):
    jsonschema.validate(all_posts_body, LIST_POSTS_SCHEMA)


def test_response_json_sorting(all_posts_body):
    validate_sorting(all_posts_body)


def test_different_user_agents():
    pass


def test_invalid_request_headers():
    headers = {'Accept-Encoding': 'gzip',
               'Accept': 'image/gif',
               'Accept-Charset': 'iso - 8859 - 1',
               'Cache-Control': 'no-cache'}
    response = get_list_posts(headers=headers)
    print(response.headers['Content-Encoding'])
    print(response.headers)
    print(response.content)
    # print(response.json())
