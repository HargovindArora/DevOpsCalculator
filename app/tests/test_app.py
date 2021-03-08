import json
import flask


def test_index_route(app, client):
    res = client.get("/")
    assert res.status_code == 200


def test_root_route(app, client):
    res = client.get("/root")
    assert res.status_code == 200


def test_factorial_route(app, client):
    res = client.get("/factorial")
    assert res.status_code == 200


def test_log_route(app, client):
    res = client.get("/log")
    assert res.status_code == 200


def test_power_route(app, client):
    res = client.get("/power")
    assert res.status_code == 200


def test_root_negative(app, client):
    res = client.post("/root", 
                    data = dict(root_number=-4)
    )

    with client.session_transaction() as session:
        flash_message = dict(session['_flashes']).get('danger')

    assert flash_message == "Square root of negative numbers is not defined"


def test_root_positive(app, client):
    res = client.post("/root", 
                    data = dict(root_number=4)
    )

    with client.session_transaction() as session:
        flash_message = dict(session['_flashes']).get('success')

    assert flash_message == "2.0 is the square root of 4"


def test_factorial_negative(app, client):
    res = client.post("/factorial", 
                    data = dict(fact_number=-4)
    )

    with client.session_transaction() as session:
        flash_message = dict(session['_flashes']).get('danger')

    assert flash_message == "Factorial of negative numbers is not defined"


def test_factorial_positive(app, client):
    res = client.post("/factorial", 
                    data = dict(fact_number=4)
    )

    with client.session_transaction() as session:
        flash_message = dict(session['_flashes']).get('success')

    assert flash_message == "24 is the Factorial of 4"


def test_log_negative(app, client):
    res = client.post("/log", 
                    data = dict(log_number=-99)
    )

    with client.session_transaction() as session:
        flash_message = dict(session['_flashes']).get('danger')

    assert flash_message == "Natural logarithm of non-positive numbers is not defined"


def test_log_zero(app, client):
    res = client.post("/log", 
                    data = dict(log_number=0)
    )

    with client.session_transaction() as session:
        flash_message = dict(session['_flashes']).get('danger')

    assert flash_message == "Natural logarithm of non-positive numbers is not defined"


def test_log_positive(app, client):
    res = client.post("/log", 
                    data = dict(log_number=4)
    )

    with client.session_transaction() as session:
        flash_message = dict(session['_flashes']).get('success')

    assert flash_message == "1.3862943611198906 is the Natural logarithm of 4"


def test_power(app, client):
    res = client.post("/power", 
                    data = dict(number=4, power=2)
    )

    with client.session_transaction() as session:
        flash_message = dict(session['_flashes']).get('success')

    assert flash_message == "Power of 4 raised to 2 is 16"


