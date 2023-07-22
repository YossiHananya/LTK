import pytest
from .conftest import db_session
from soccer_application.models import User

# Define test data as a list of dictionaries
test_user_data = [
    {
        "user_data": {
        "username": "John Doe",
        "email": "johndoe2@gmail.com",
        "password": "Password1!"
        },
        "updated_data": {
            "username": "John1 Doe"
        }
    }
]

#Testing CRUD (Create, Read, Update & Delete) for User table
@pytest.mark.parametrize("test_user_data", test_user_data)
def test_create_user(db_session,test_user_data):
    user_data=test_user_data['user_data']
    # Create a user object
    new_user = User(**user_data)
    db_session.add(new_user)
    db_session.commit()

    # Test that the user was added to the database
    assert db_session.query(User).count() == 1

@pytest.mark.parametrize("test_user_data", test_user_data)
def test_read_user(db_session,test_user_data):
    user_data=test_user_data['user_data']

    # Test that the user can be queried from the database
    fetched_object = db_session.query(User).first()

    for key,value in user_data.items():
        assert getattr(fetched_object, key) == value

@pytest.mark.parametrize("test_user_data", test_user_data)
def test_update_user(db_session,test_user_data):
    updated_data=test_user_data['updated_data']

    fetched_object = db_session.query(User).first()

    #Set the new attributes for the new user
    for key, value in updated_data.items():
        setattr(fetched_object,key,value)
    db_session.commit()

    #Fetch the updated user
    updated_user = db_session.query(User).filter_by(id=fetched_object.id).first()

    # Check if the user's data is updated
    assert updated_user.username == updated_data['username']

@pytest.mark.parametrize("test_user_data", test_user_data)
def test_delete_user(db_session,test_user_data):

    fetched_object = db_session.query(User).first()
    # Test deleting the object
    db_session.delete(fetched_object)
    db_session.commit()

    # Test that the object was removed from the database
    assert db_session.query(User).count() == 0