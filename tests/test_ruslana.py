

def test_get_metadata(client):
    res = client.get("/")
    assert res.status_code == 200
