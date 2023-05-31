import openai
import pytest

from pypixel.models import OpenAI


class TestOpenAI:
    @pytest.fixture(autouse=True)
    def default_model(self):
        return OpenAI()

    def test_default_params(self, default_model):
        assert default_model.engine == "text-davinci-003"
        assert default_model.max_tokens == 1200
        assert default_model.temperature == 0
        assert default_model.top_p == 1
        assert default_model.frequency_penalty == 0.25
        assert default_model.presence_penalty == 0
        assert not hasattr(default_model, "api_key")

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

    def test_type(self, default_model):
        assert default_model.model == "OpenAI"

    def test_secrets(self, default_model):
        assert hasattr(
            default_model, "_secrets"
        ), "Create a secrets.json file with your OpenAI API key"
        assert openai.api_key is not None

    def test_representation(self, default_model):
        assert str(default_model) == "OpenAI"
        assert repr(default_model) == "OpenAI"

    def test_openai_implementation(self, mocker, default_model):
        default_model = OpenAI()
        prompt = "Generate code for histogram equalization."
        expected_text = "# mock results \n import cv2"

        mock = mocker.patch("openai.Completion.create")
        mock.return_value = {"choices": [{"text": expected_text}]}
        response = default_model.run(prompt)
        mock.assert_called_once_with(
            engine=default_model.engine,
            prompt=prompt,
            temperature=default_model.temperature,
            max_tokens=default_model.max_tokens,
            top_p=default_model.top_p,
            frequency_penalty=default_model.frequency_penalty,
            presence_penalty=default_model.presence_penalty,
        )

        assert response == expected_text

    def test_openai_api_error(self, mocker, default_model):
        mock, model, prompt = self.setup_mocker(mocker, default_model)
        mock.side_effect = openai.error.APIError("API Error")
        response = model.run(prompt)
        mock.assert_called_once_with(
            engine=model.engine,
            prompt=prompt,
            temperature=model.temperature,
            max_tokens=model.max_tokens,
            top_p=model.top_p,
            frequency_penalty=model.frequency_penalty,
            presence_penalty=model.presence_penalty,
        )

        assert response is None

    def setup_mocker(self, mocker, default_model):
        default_model = OpenAI()
        prompt = "Generate code for histogram equalization."
        mock = mocker.patch("openai.Completion.create")
        return mock, default_model, prompt

    def test_openai_api_connection_error(self, mocker, default_model):
        mock, model, prompt = self.setup_mocker(mocker, default_model)
        mock.side_effect = openai.error.APIConnectionError("API Connection Error")
        response = model.run(prompt)
        mock.assert_called_once_with(
            engine=model.engine,
            prompt=prompt,
            temperature=model.temperature,
            max_tokens=model.max_tokens,
            top_p=model.top_p,
            frequency_penalty=model.frequency_penalty,
            presence_penalty=model.presence_penalty,
        )

        assert response is None

    def test_openai_api_rate_limit_error(self, mocker, default_model):
        mock, model, prompt = self.setup_mocker(mocker, default_model)
        mock.side_effect = openai.error.RateLimitError("Rate Limit Error")
        response = model.run(prompt)
        mock.assert_called_once_with(
            engine=model.engine,
            prompt=prompt,
            temperature=model.temperature,
            max_tokens=model.max_tokens,
            top_p=model.top_p,
            frequency_penalty=model.frequency_penalty,
            presence_penalty=model.presence_penalty,
        )

        assert response is None