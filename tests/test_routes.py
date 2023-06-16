def test_playersapi_players_route(client):
    """
    GIVEN a Flask API Application Is Running 
    WHEN The '/playeraapi/players' Page Is Requested (GET)
    THEN Check The Response Is Valid 
    """
    response = client.get('/playersapi/players')
    assert response.status_code == 200
    assert response.json['Players'][0]['first_name']=='Assaf'
    assert response.json['Players'][1]['id']==2

def test_playersapi_players_route_post_data(client):
    """
    GIVEN a Flask API Application Is Running 
    WHEN The '/playeraapi/players' Page Is Send POST Requeste With Data
    THEN Check The Response Is Valid 
    """
    response = client.post('/playersapi/players',json={"first_name":"Tal","id":3,"last_name":'Bitton'})
    assert response.status_code == 201
    assert response.json["message"] == "Player added successfully"

def test_playersapi_players_by_id(client):
    """
    GIVEN a Flask API Application Is Running 
    WHEN The '/playeraapi/players/(number)' Is Requested (GET)
    THEN Check The Response Is Valid 
    """
    response = client.get('/playersapi/players/1')
    assert response.status_code == 200
    assert response.json["Player_Details"]["id"]==1

def test_playersapi_players_by_id_that_not_in_list(client):
    """
    GIVEN a Flask API Application Is Running 
    WHEN The '/playeraapi/players/(number not in list)' Is Requested (GET)
    THEN Check The Response Is Valid 
    """
    response = client.get('/playersapi/players/8')
    assert response.status_code == 500
