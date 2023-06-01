import openai
import pytest

from pypixel.exceptions import *
from pypixel.models import OpenAI
from pypixel.prompts import *


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

    def test_generate_image(self):
        with pytest.raises(InvalidPromptException):
            OpenAI().generate_images()

    def test_generate_image_with_str_prompt(self):
        with pytest.raises(InvalidPromptException):
            OpenAI().generate_images(prompt="prompt")

    def test_generate_image_with_invalid_size(self, caplog):
        model = OpenAI()
        with pytest.raises(InvalidAttributeException):
            model.generate_images(
                prompt=GenerateImagePrompt("prompt"), size=200, num_images=2
            )

        with pytest.raises(InvalidAttributeException):
            model.generate_images(
                prompt=GenerateImagePrompt("prompt"), size="256x256", num_images=20
            )

    def test_generate_image_with_default_params(self, caplog):
        model = OpenAI()
        model.generate_images(prompt=GenerateImagePrompt("prompt"))
        assert len(caplog.records) == 2
        assert caplog.records[0].levelname == "WARNING"
        assert "No size specified. Defaulting to 256x256" in caplog.records[0].message
        assert (
            "No number of images specified. Defaulting to 1"
            in caplog.records[1].message
        )

    def test_generate_images_run(self, mocker):
        model = OpenAI()
        prompt = GenerateImagePrompt("Generate wallpaper for engineers.")
        expected_value = ["test_url1", "test_url2", "test_url3"]

        mock = mocker.patch("openai.Image.create")
        mock.return_value = {
            "data": [
                {"url": "test_url1"},
                {"url": "test_url2"},
                {"url": "test_url3"},
            ]
        }
        response = model.generate_images(prompt, num_images=3)
        mock.assert_called_once_with(
            prompt=str(prompt),
            n=3,
            size="256x256",
        )

        assert response == expected_value

    def test_edit_images_run(self, mocker):
        model = OpenAI()
        prompt = EditImagePrompt("Generate wallpaper for engineers.")
        expected_value = ["test_url1", "test_url2", "test_url3"]

        mock = mocker.patch("openai.Image.create_edit")
        mock.return_value = {
            "data": [
                {"url": "test_url1"},
                {"url": "test_url2"},
                {"url": "test_url3"},
            ]
        }
        image = mask = None  # dummy
        response = model.edit_images(
            image=image, mask=mask, prompt=prompt, num_images=3
        )
        mock.assert_called_once_with(
            image=image,  # dummy data
            mask=mask,
            prompt=str(prompt),
            n=3,
            size="256x256",
        )

        assert response == expected_value
