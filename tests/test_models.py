import pytest

from pypixel.models import OpenAI


class TestOpenAI:
    def test_default_params(self):
        model = OpenAI()
        assert model.engine == "text-davinci-003"
        assert model.max_tokens == 1200
        assert model.temperature == 0
        assert model.top_p == 1
        assert model.frequency_penalty == 0.25
        assert model.presence_penalty == 0
        assert not hasattr(model, "api_key")

    def test_custom_params(self):
        model = OpenAI(
            engine="text-davinci-003",
            max_tokens=600,
            temperature=0.5,
            top_p=0.5,
            frequency_penalty=0.5,
            presence_penalty=0.5,
        )

        assert model.engine == "text-davinci-003"
        assert model.max_tokens == 600
        assert model.temperature == 0.5
        assert model.top_p == 0.5
        assert model.frequency_penalty == 0.5
        assert model.presence_penalty == 0.5
        assert not hasattr(model, "api_key")

    def test_secrets(self):
        model = OpenAI()
        assert hasattr(model, "_secrets")

    def test_representation(self):
        model = OpenAI()
        assert str(model) == "OpenAI"
        assert repr(model) == "OpenAI"

    def test_implementation(self, mocker):
        model = OpenAI()
        with pytest.raises(NotImplementedError):
            model.run("test")

    def test_run(self):
        model = OpenAI()
        assert model.run("test")
