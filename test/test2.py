from pypixel import PyPixel
from pypixel.models import OpenAI


def main():
    model = OpenAI()
    px = PyPixel(model)
    code = px(
        "Use the image dog.jpg, generate histograms for each color channel, and save the histograms to a file named histograms.jpg.",
        write_to_file="test_output.py",
    )
    print(code)


if __name__ == "__main__":
    main()
