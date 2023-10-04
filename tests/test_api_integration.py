
def check_redirection(response, expected_location):
    assert response.status_code == 302
    assert response.location == expected_location

def check_final_page(response, expected_title):
    assert response.status_code == 200
    expected_html = f"<title>LTK - {expected_title}</title>"
    assert bytes(expected_html, 'utf-8') in response.data

def test_home(client):
    for url in ['/', '/home']:
        response = client.get(url)
        assert response.status_code == 200
        assert b"<title>LTK - home</title>" in response.data

def register(client):
    pwd = "Testpwd#10"

    response = client.post(
        '/register',
        data={
            "username":"test",
            "email":"yossiha93@gmail.com",
            "password":pwd,
            "password_confirmation":pwd,
            "remember": False,
            "csrf_token": client.csrf_token
        },
    )

    check_redirection(response=response, expected_location='/home')
    response = client.get(response.location)
    check_final_page(response=response, expected_title='home')

def login(client):
    pwd = "Testpwd#10"

    response = client.post(
        '/login',
        data={
            "email":"yossiha93@gmail.com",
            "password":pwd,
            "remember": False,
            "csrf_token": client.csrf_token
        },
    )
    check_redirection(response=response, expected_location='/home')
    response = client.get(response.location)
    check_final_page(response=response, expected_title='home')

def logout(client):
    response = client.get('/logout')
    check_redirection(response=response, expected_location='/home')
    response = client.get(response.location)
    check_final_page(response=response, expected_title='home')

def test_registration(client):
    response = client.get('/register')
    check_final_page(response=response, expected_title='Register')
    register(client=client)

def test_login_logout(client):
    logout(client=client)
    login(client=client)


