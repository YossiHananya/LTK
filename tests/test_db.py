import pytest
from .conftest import db_session
from soccer_application.models import Users,Games,Teams,Courts
from datetime import datetime, timedelta, date

# Define test data as a list of dictionaries
test_data = [
    {
        "table_cls": Users,
        "origin_data": {
        "username": "John Doe",
        "password": "Password1!"
        },
        "updated_data": {
            "username": "John1 Doe"
        }
    },
    {
        "table_cls": Teams,
        "origin_data": {
        "name": "LTK"
        },
        "updated_data": {
            "name": "LTK1"
        }
    },
    {
        "table_cls": Courts,
        "origin_data": {
        "name": "Mekif",
        "address": "Hahistadrot 7"
        },
        "updated_data": {
        "name": "Mekif1",
        "address": "Hahistadrot 8"
        }
    },
    {
        "table_cls": Games,
        "origin_data": {
        "game_date": date.today(),
        "team_id": 
        },
        "updated_data": {
            "game_date": date.today() - timedelta(days=1)
        }
    }
]

#Testing CRUD (Create, Read, Update & Delete) for Generic table
@pytest.mark.parametrize("test_data", test_data)
def test_create_db_object(db_session, test_data):
    obj_data = test_data['origin_data']
    db_obj_cls = test_data['table_cls']
    
    # Create a db object
    new_obj = db_obj_cls(**obj_data)
    db_session.add(new_obj)
    db_session.commit()

    # Test that the db object was added to the database
    assert db_session.query(db_obj_cls).count() == 1

@pytest.mark.parametrize("test_data", test_data)
def test_read_db_obj(db_session, test_data):
    obj_data = test_data['origin_data']
    db_obj_cls = test_data['table_cls']

    # Test that the db object can be queried from the database
    fetched_object = db_session.query(db_obj_cls).first()

    for key,value in obj_data.items():
        assert getattr(fetched_object, key) == value

@pytest.mark.parametrize("test_data", test_data)
def test_update_db_object(db_session, test_data):
    updated_data = test_data['updated_data']
    db_obj_cls = test_data['table_cls']
    
    fetched_object = db_session.query(db_obj_cls).first()

    # Set the new attributes for the new db object
    for key, value in updated_data.items():
        setattr(fetched_object, key, value)

    db_session.commit()

    # Fetch the updated db object
    updated_object = db_session.query(db_obj_cls).filter_by(id = fetched_object.id).first()

    # Check if the object's data is updated
    for key in updated_data.keys():
        assert getattr(updated_object, key) == updated_data[key]

@pytest.mark.parametrize("test_data", test_data)
def test_delete_db_object(db_session, test_data):
    db_obj_cls = test_data['table_cls']
    
    fetched_object = db_session.query(db_obj_cls).first()
    # Test deleting the object
    db_session.delete(fetched_object)
    db_session.commit()

    # Test that the object was removed from the database
    assert db_session.query(db_obj_cls).count() == 0