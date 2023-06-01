from pypixel import PyPixel
from pypixel.models import Cohere, OpenAI, Starcoder


def main():
    model = OpenAI()  # choose a model
    px = PyPixel(model, retries=3)  # initialize PyPixel with the model
    # generate code
    code = px.generate_images("Blank white image", num_images=2, download=True)
    print(code)
    # if code has runtime errors, prompt for a fix


if __name__ == "__main__":
    main()
