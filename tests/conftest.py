import pytest
from soccer_application import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from soccer_application.config.config_names import ConfigName

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
