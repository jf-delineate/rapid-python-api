from behave import given, when, then
import requests
import json


@given(u"with path {path}")
def domain_with_path(context, path):

    url = "http://localhost:8000" + path
    context.request_url = url
    print("url: " + context.request_url)


@given(u"header {key} as {value}")
def header_key_as_value(context, key, value):

    if not hasattr(context, "request_headers"):
        context.request_headers = {}

    context.request_headers[key] = value
    print("header: " + context.request_headers[key])


@given(u"request {body}")
def request_body(context, body):

    context.request_body = json.loads(body)
    print("body: " + body)


@when(u"method {verb}")
def method_verb(context, verb):

    context.request_method = verb
    print("method: " + context.request_method)

    if not hasattr(context, "request_headers"):
        context.request_headers = {}

    if not hasattr(context, "request_body"):
        context.request_body = None

    if context.request_method == "GET":
        response = requests.get(
            context.request_url,
            headers=context.request_headers,
            json=context.request_body,
        )

    if context.request_method == "POST":
        response = requests.post(
            context.request_url,
            headers=context.request_headers,
            json=context.request_body,
        )

    context.response_body = response.text
    context.response_code = response.status_code
    print("actual: " + str(context.response_code))


@then(u"status {code}")
def status_code(context, code):

    print("expected: " + str(code))
    assert str(context.response_code) == str(code)
