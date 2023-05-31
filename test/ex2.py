from pypixel import PyPixel
from pypixel.models import Cohere, OpenAI, Starcoder


def main():
    model = Starcoder()  # choose a model
    px = PyPixel(model)  # initialize PyPixel with the model
    # generate code
    code = px(
        "Use the image dog.jpg, generate histograms for each color channel, and save the histograms to a file named histograms.jpg.",
        write_to_file="test_output.py",
        run_code=False,
    )
    # if code has runtime errors, prompt for a fix


if __name__ == "__main__":
    main()
