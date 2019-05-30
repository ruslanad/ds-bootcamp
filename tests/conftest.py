from ds_bootcamp.flask_app import create_app
import pytest


@pytest.fixture
def app():
    ''' runs the funtions and returns its output '''
    app = create_app()
    return app
