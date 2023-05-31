import cohere
import openai
import pytest

from pypixel.models import Cohere


class TestOpenAI:
    @pytest.fixture(autouse=True)
    def model(self):
        return Cohere()

    def test_default_params(self, model):
        assert model.engine == "command"
        assert model.max_tokens == 1200
        assert model.temperature == 0.2
        assert model.k == 0
        assert model.stop_sequences == []
        assert model.return_likelihoods == "NONE"
        assert hasattr(model, "client")

    def test_custom_params(self):
        model = Cohere(
            engine="command-nightly",
            max_tokens=600,
            temperature=0.5,
            k=0.5,
            stop_sequences=["\n"],
            return_likelihoods="NONE",
        )

        assert model.engine == "command-nightly"
        assert model.max_tokens == 600
        assert model.temperature == 0.5
        assert model.k == 0.5
        assert model.stop_sequences == ["\n"]
        assert model.return_likelihoods == "NONE"

    def test_type(self, model):
        assert model.model == "Cohere"

    def test_secrets(self, model):
        assert hasattr(
            model, "_secrets"
        ), "Create a secrets.json file with your OpenAI API key"
        assert hasattr(model, "client") and model.client is not None

    def test_representation(self, model):
        assert str(model) == "Cohere"
        assert repr(model) == "Cohere"

    def test_cohere_implementation(self, mocker, model):
        prompt = "Generate code for histogram equalization."
        expected_text = "# mock results \n import cv2"

        mock = mocker.patch.object(model.client, "generate")
        mock.return_value = {"generations": [{"text": expected_text}]}
        response = model.run(prompt)
        mock.assert_called_once_with(
            model=model.engine,
            prompt=prompt,
            max_tokens=model.max_tokens,
            temperature=model.temperature,
            k=model.k,
            stop_sequences=model.stop_sequences,
            return_likelihoods=model.return_likelihoods,
        )

        assert response == expected_text

    def setup_mocker(self, mocker, model):
        prompt = "Generate code for histogram equalization."
        mock = mocker.patch("openai.Completion.create")
        return mock, model, prompt
