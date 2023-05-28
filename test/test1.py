from pypixel import PyPixel


def main():
    px = PyPixel()
    code = px(
        "Write code to make the image named dog brighter by two times",
        write_to_file="test_output.py",
    )
    print(code)


if __name__ == "__main__":
    main()
