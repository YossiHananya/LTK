import pytest
from soccer_application import create_app, db
from soccer_application.config.config_names import ConfigName

@pytest.fixture()
def app():
    app = create_app(config_name=ConfigName.TESTING)
    with app.app_context():
        yield app

@pytest.fixture()
def client(app):
    return app.test_client()
