import requests

from app import app


def test_hello_escapes_html():
    r = app.test_client().get("/hello/<b>x</b>")
    assert r.status_code == 200
    assert b"&lt;b&gt;" in r.data


def test_requests_builds_url():
    req = requests.Request("GET", "https://example.com", params={"q": "a b"}).prepare()
    assert req.url == "https://example.com/?q=a+b"
