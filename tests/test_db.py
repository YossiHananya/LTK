import pytest
from .conftest import app 
from .conftest import client
from soccer_application.models import User
from soccer_application import db

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
def test_create_user(client, test_user_data):
    user_data=test_user_data['user_data']
    # Create a user object
    new_user = User(**user_data)
    db.session.add(new_user)
    db.session.commit()

    # Test that the user was added to the database
    assert User.query.count() == 1

@pytest.mark.parametrize("test_user_data", test_user_data)
def test_read_user(client,test_user_data):
    user_data=test_user_data['user_data']
    # Create a user object
    new_user = User(**user_data)
    db.session.add(new_user)
    db.session.commit()

    # Test that the user can be queried from the database
    fetched_object = User.query.first()

    for key,value in user_data.items():
        assert getattr(fetched_object, key) == value

@pytest.mark.parametrize("test_user_data", test_user_data)
def test_update_user(client, test_user_data):
    user_data=test_user_data['user_data']
    updated_data=test_user_data['updated_data']
    # Create a user object
    new_user = User(**user_data)
    db.session.add(new_user)
    db.session.commit()

    #Set the new attributes for the new user
    for key, value in updated_data.items():
        setattr(new_user,key,value)
    db.session.commit()

    #Fetch the updated user
    updated_user = User.query.filter_by(id=new_user.id).first()

    # Check if the user's data is updated
    assert updated_user.username == "John1 Doe"

@pytest.mark.parametrize("test_user_data", test_user_data)
def test_delete_user(client, test_user_data):
    user_data=test_user_data['user_data']
    # Create a user object
    new_user = User(**user_data)
    db.session.add(new_user)
    db.session.commit()

    # Test deleting the object
    db.session.delete(new_user)
    db.session.commit()

    # Test that the object was removed from the database
    assert User.query.count() == 0

    





    




    # # Test fetching the object from the database
    # fetched_object = YourModel.query.first()
    # for key, value in data.items():
    #     assert getattr(fetched_object, key) == value
 
