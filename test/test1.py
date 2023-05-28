from pypixel import PyPixel


def main():
    px = PyPixel()
    code = px(
        "Increase the brightness of the image by 50%",
        write_to_file="test_output.py",
    )
    print(code)


if __name__ == "__main__":
    main()
