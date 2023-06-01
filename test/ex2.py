from pypixel import PyPixel
from pypixel.models import Cohere, OpenAI, Starcoder


def main():
    model = OpenAI()  # choose a model
    px = PyPixel(model)  # initialize PyPixel with the model
    # generate code
    url = px.generate_images("Image of a duck", "256x256", 2, download=True)
    # if code has runtime errors, prompt for a fix


if __name__ == "__main__":
    main()
