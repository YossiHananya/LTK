from soccer_application.models import Users,Games,Teams,Expenses,Courts,Players
from datetime import datetime, timedelta, date

TESTING_DATETIME = datetime.now()

def check_amount_positive(x: int) -> None:
    if x<0:
        raise ValueError("Amount must be a positive number")
    return x

dummy_data = [
    # {
    #     "table_cls": Players,
    #     "origin_data": {
    #     "user_id": 1,
    #     "first_name": "Bob",
    #     "last_name": "Brown",
    #     "date_of_birth": TESTING_DATETIME,
    #     "status": True,
    #     "team_id": 1
    #     },
    #     "updated_data": {
    #     "first_name": "Boby",
    #     "last_name": "Brown1",
    #     "date_of_birth": TESTING_DATETIME - timedelta(days=1),
    #     "status": False
    #     }
    # },
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
        "table_cls": Games,
        "origin_data": {
        "game_date": TESTING_DATETIME,
        "team_id": 1,
        "court_id": 1
        },
        "updated_data": {
        "game_date": TESTING_DATETIME - timedelta(days=1)
        }
    },
    {
        "table_cls": Expenses,
        "origin_data": {
        "date": TESTING_DATETIME,
        "amount": check_amount_positive(100),
        "description": "Total amount for nets",
        "team_id": 1
        },
        "updated_data": {
        "date": TESTING_DATETIME - timedelta(days=1),
        "amount": 110,
        "description": "Extra nets added"
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
    }
]