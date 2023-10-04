import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from soccer_application import db, create_app
from soccer_application.config.config_names import ConfigName
from .csrf_client import FlaskClientWithCSRF

@pytest.fixture(scope='module')
def db_session():
    # Create an in-memory SQLite database for testing
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    db.metadata.create_all(bind=engine)
    session = Session()
    yield session
    session.rollback()
    db.metadata.drop_all(bind=engine)
    session.close()

@pytest.fixture(scope='module')
def app():
    app = create_app(config_name=ConfigName.TESTING)
    with app.app_context():
        yield app

@pytest.fixture(scope='module')
def client(app):
    app.test_client_class = FlaskClientWithCSRF
    yield app.test_client()