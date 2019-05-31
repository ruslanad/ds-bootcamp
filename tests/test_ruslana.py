

def test_get_metadata_ruslana(client):
    res = client.get("/ruslana")
    assert res.status_code == 200


def test_get_metadata_props(client):
    res = client.get("/props")
    assert res.status_code == 200


def test_get_ruslana_model(client):
    res = client.get("/ruslana_model/submodel_1/10")
    assert res.status_code == 200
    assert res.json['score'] == 10


def test_invalid_model(client):
    res = client.get("/ruslana_model/submodel_3/10")
    assert res.status_code == 404
