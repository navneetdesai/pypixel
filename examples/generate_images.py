from pypixel import PyPixel
from pypixel.models import OpenAI


def main():
    model = OpenAI()  # choose a model
    px = PyPixel(model, retries=3)  # initialize PyPixel with the model
    code = px.generate_images("Blank white image", num_images=2, download=True)
    print(code)


if __name__ == "__main__":
    main()
