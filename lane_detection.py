import cv2
import matplotlib.pyplot as plt
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blank_image, (x1,y1), (x2,y2), (0,255,0), 2)
    img = cv2.addWeighted(img, 0.8, blank_image, 0.2, 0)
    return img

# def draw_lines(img, lines):
#     for line in lines:
#         x1, y1, x2, y2 = line[0]
#         cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 3)
#     return img

img = cv2.imread('media/road.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

region_of_interest_vertices = [(400, 667), (480,400),(1000,640)]

gray_roi = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
canny = cv2.Canny(gray_roi, 100, 200)
cropped_image = region_of_interest(canny, np.array([region_of_interest_vertices], np.int32))
lines = cv2.HoughLinesP(cropped_image, 6, np.pi/60, 160, np.array([]), minLineLength=0, maxLineGap=25)

image_with_lines = draw_lines(img, lines)
plt.imshow(image_with_lines)
plt.show()