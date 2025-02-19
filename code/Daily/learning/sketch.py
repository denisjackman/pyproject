''' sketch.py '''
import cv2
INPUT_IMAGE = "Y:/Pictures/avatars/4504_0230750.jpg"
OUTPUT_IMAGE = "E:/temp/sketch.jpg"


def image_to_sketch(its_input, its_output):
    ''' image to sketch converter'''
    image = cv2.imread(its_input)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = 255-gray_image
    blur = cv2.GaussianBlur(inverted, (21, 21), 0)
    invertedblur = 255-blur
    sketch = cv2.divide(gray_image, invertedblur, scale=256.0)
    cv2.imwrite(its_output, sketch)
    return sketch


def main():
    ''' main function '''
    cv2.imshow("image", image_to_sketch(INPUT_IMAGE, OUTPUT_IMAGE))


if __name__ == "__main__":
    main()
