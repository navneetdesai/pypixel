import pytest

from pypixel.constants import STARCODER_API_KEY
from pypixel.models import Starcoder


class TestStarcoder:
    @pytest.fixture(autouse=True)
    def model(self):
        return Starcoder()

    def test_model(self, model):
        assert model.model == "starcoder"

    def test_representation(self, model):
        assert str(model) == "Starcoder"
        assert repr(model) == "Starcoder"

    def test_secrets(self, model):
        assert hasattr(
            model, "_secrets"
        ), "Create a secrets.json file with your Starcoder API key"
        assert model._secrets.get(STARCODER_API_KEY) is not None
