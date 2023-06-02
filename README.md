# pypixel
[![Code Quality](https://github.com/navneetdesai/pypixel/actions/workflows/code-quality.yml/badge.svg)](https://github.com/navneetdesai/pypixel/actions/workflows/code-quality.yml)
[![Code coverage](https://img.shields.io/badge/codecoverage-73%25-green.svg)](#)
![Tests](https://img.shields.io/badge/Tests-40-blue)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


Pypixel is an NLP-powered code generation tool for image processing.
With Pypixel, you can generate Python code snippets for a wide range
of image processing tasks, such as applying filters, performing transformations,
extracting features, and more. Harness the power of natural language prompts
to automate image processing workflows effortlessly.
Additionally, Pypixel enables you to generate new images from scratch and edit 
existing ones, allowing for creative experimentation and customization. 



## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Natural language code generation**: Generate Python code snippets for image processing tasks using natural language prompts.
- **Image generation**: Generate new images from scratch using natural language prompts.
- **Image editing**: Edit existing images using natural language prompts.
- **Image processing**: Perform a wide range of image processing tasks, such as applying filters, performing transformations, extracting features, and more.
- **Flexible APIs**: Use Pypixel's APIs to integrate image processing into your own applications.


## Installation
`pip install pypixelai` \
`vim .env`  # add your API key to the .env file . \

```
OPENAI_KEY="" 
COHERE_KEY=""
STARCODER_KEY="
```


## Examples
- Generate code snippets for image processing tasks
  ```python
  from pypixelai import PyPixel # Import PyPixel
  from pypixelai.models import OpenAI # choose a model
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
  ```
Output:
```python

import cv2
import numpy as np

img = cv2.imread('image.jpg')
img = np.int16(img)
img = img + (50/100)*img
img = np.clip(img, 0, 255)
img = np.uint8(img)
cv2.imwrite('image_brightened.jpg', img)

```

- Generate new images from scratch
  ```python
    model = OpenAI()  # choose a model
    px = PyPixel(model, retries=3)  # initialize PyPixel with the model
    urls = px.generate_images("Blank white image", num_images=2, download=True)
    print(urls)
  ```


- Edit existing images
  ```python
    image = open("image.jpg", "rb")
    mask = open("mask.png", "rb")
    prompt = "A sunlit indoor lounge area with a pool containing a flamingo"
    urls = px.edit_images(image, mask, prompt, n=None, size=None, download=False)
    print(urls)
  ```


## Contributing

If you have any suggestions or would like to contribute in any way, please raise an [issue](https://github.com/navneetdesai/pypixel/issues).


## License

This project is licensed under the [MIT License](LICENSE).

