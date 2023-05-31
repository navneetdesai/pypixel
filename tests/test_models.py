import openai
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

    def test_type(self):
        model = OpenAI()
        assert model.model == "OpenAI"

    def test_secrets(self):
        model = OpenAI()
        assert hasattr(
            model, "_secrets"
        ), "Create a secrets.json file with your OpenAI API key"
        assert openai.api_key is not None

    def test_representation(self):
        model = OpenAI()
        assert str(model) == "OpenAI"
        assert repr(model) == "OpenAI"

    def test_openai_implementation(self, mocker):
        model = OpenAI()
        prompt = "Generate code for histogram equalization."
        expected_text = "# mock results \n import cv2"

        mock = mocker.patch("openai.Completion.create")
        mock.return_value = {"choices": [{"text": expected_text}]}
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

        assert response == expected_text

    def test_openai_api_error(self, mocker):
        model = OpenAI()
        prompt = "Generate code for histogram equalization."
        expected_text = "# mock results \n import cv2"

        mock = mocker.patch("openai.Completion.create")
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

    def test_openai_api_connection_error(self, mocker):
        model = OpenAI()
        prompt = "Generate code for histogram equalization."
        expected_text = "# mock results \n import cv2"

        mock = mocker.patch("openai.Completion.create")
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

    def test_openai_api_rate_limit_error(self, mocker):
        model = OpenAI()
        prompt = "Generate code for histogram equalization."
        expected_text = "# mock results \n import cv2"

        mock = mocker.patch("openai.Completion.create")
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
