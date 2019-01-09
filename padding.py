import cv2
import os
import glob
from datetime import datetime

# Get images
imgs = glob.glob('*.jpg')
imgs.extend(glob.glob('*.jpeg'))

WHITE = [255,255,255]

print('Found files:')
print(imgs)

folder = 'resized'

if not os.path.exists(folder):
    os.makedirs(folder)
for img in imgs:
    im = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    target_size = 256

    old_size = im.shape[:2]
    #print(old_size)

    ratio = float(target_size)/max(old_size)
    #print(ratio)

    new_size = tuple([int(x*ratio) for x in old_size])
    #print(new_size)

    im = cv2.resize(im, (new_size[1], new_size[0]))

    beda_w = target_size - new_size[1]
    beda_h = target_size- new_size[0]
    top, bottom = beda_h//2, beda_h-(beda_h//2)
    left, right = beda_w//2, beda_w-(beda_w//2)

    new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,value=WHITE)
    #cv2.imshow("image", new_im)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    cv2.imwrite(folder + '/' + img, new_im)
