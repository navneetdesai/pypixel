from pypixelai import PyPixel
from pypixelai.models import OpenAI


def main():
    model = OpenAI()
    px = PyPixel(
        model
        #  debug=True       # print debug messages, default: False
        # retries=3        # number of times to retry code default=1
    )
    code = px(
        "Increase the brightness of the image by 50%",
        #  write_to_file="test_output.py",    # write code to file
        #  run_code=True,                     # run code
    )
    print(code)


if __name__ == "__main__":
    main()
