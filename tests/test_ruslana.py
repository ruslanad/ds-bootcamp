
from hypothesis import strategies as st, given, reproduce_failure
from ds_bootcamp.flask_app import MIN_VALUE, MAX_VALUE


def test_get_metadata_ruslana(client):
    res = client.get("/ruslana")
    assert res.status_code == 200


def test_get_metadata_props(client):
    res = client.get("/props")
    assert res.status_code == 200


def test_get_ruslana_model(client):
    res = client.get("/ruslana_model/submodel_1/10")
    assert res.status_code == 200
    assert res.json['score'] == 11


def test_invalid_model(client):
    res = client.get("/ruslana_model/submodel_3/10")
    assert res.status_code == 404


@given(
    x=st.integers(min_value=MIN_VALUE, max_value=MAX_VALUE)
)
def test_ruslana_model_hypothesis(client, x):
    res = client.get(f"/ruslana_model/submodel_1/{x}")
    assert res.status_code == 200
    assert res.json['score'] > x


@given(
    x=st.integers(min_value=MAX_VALUE+1)
)
def test_ruslana_model_hypothesis_low_value(client, x):
    res = client.get(f"/ruslana_model/submodel_1/{x}")
    assert res.status_code == 400


@given(
    x=st.integers(max_value=MIN_VALUE-1)
)
def test_ruslana_model_hypothesis_low_value(client, x):
    res = client.get(f"/ruslana_model/submodel_1/{x}")
    assert res.status_code == 400


def test_ruslana_model_404(client):
    res = client.get("/ruslana_model/submodel_3/10")
    assert res.status_code == 404
