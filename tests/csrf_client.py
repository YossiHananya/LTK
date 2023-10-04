# Taken from https://gist.github.com/singingwolfboy/2fca1de64950d5dfed72
import typing as t
import flask
from flask.testing import FlaskClient
from flask_wtf.csrf import generate_csrf

class RequestShim(object):
    """
    A fake request that proxies cookie-related methods to a Flask test client.
    """
    def __init__(self, client):
        self.client = client

    def set_cookie(self, key, value='', *args, **kwargs):
        "Set the cookie on the Flask test client."
        server_name = flask.current_app.config["SERVER_NAME"] or "localhost"
        return self.client.set_cookie(
            server_name, key=key, value=value, *args, **kwargs
        )

    def delete_cookie(self, key, *args, **kwargs):
        "Delete the cookie on the Flask test client."
        server_name = flask.current_app.config["SERVER_NAME"] or "localhost"
        return self.client.delete_cookie(
            server_name, key=key, *args, **kwargs
        )

class FlaskClientWithCSRF(FlaskClient):
    @property
    def csrf_token(self):
        request = RequestShim(self)
        environ_overrides = {}
        # self.cookie_jar.inject_wsgi(environ_overrides)
        with flask.current_app.test_request_context(
                "/login", environ_overrides=environ_overrides,
            ):
            csrf_token = generate_csrf()
            return csrf_token