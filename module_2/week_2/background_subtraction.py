import numpy as np
import cv2

bg1_image = cv2.imread('./image/GreenBackground.png')
bg1_image = cv2.resize(bg1_image, (678, 381))

ob_image = cv2.imread('./image/Object.png')
ob_image = cv2.resize(ob_image, (678, 381))

bg2_image = cv2.imread('./image/NewBackground.jpg')
bg2_image = cv2.resize(bg2_image, (678, 381))


def compute_difference(bg_img, input_img):
    return cv2.absdiff(bg_img, input_img)


def compute_binary_mask(difference_img):
    gray_diff = cv2.cvtColor(difference_img, cv2.COLOR_BGR2GRAY)
    _, binary_mask = cv2.threshold(gray_diff, 50, 255, cv2.THRESH_BINARY)
    return binary_mask


def replace_background(bg1_image, bg2_image, ob_image):
    difference_img = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_img)
    
    binary_mask_3ch = cv2.cvtColor(binary_mask, cv2.COLOR_GRAY2BGR)
    
    output = np.where(binary_mask_3ch == 255, ob_image, bg2_image)
    return output


output_image = replace_background(bg1_image, bg2_image, ob_image)

cv2.imshow('Final Output', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()