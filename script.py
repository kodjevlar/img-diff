import cv2
from cv2 import cv
import sys
from subprocess import call
import numpy as np

def intersection(a,b):
    x = max(a[0], b[0])
    y = max(a[1], b[1])
    w = min(a[0]+a[2], b[0]+b[2]) - x
    h = min(a[1]+a[3], b[1]+b[3]) - y
    if w<0 or h<0: return () # or (0,0,0,0) ?
    return (x, y, w, h)

true = sys.argv[1] # The considered "true" image
comp = sys.argv[2] # The image to compare with
dst = sys.argv[3]  # Resulting image of differences

img1 = cv2.imread(comp)
img2 = cv2.imread(true)

i1x,i1y = img1.shape[:2]
i2x,i2y = img2.shape[:2]

print "Loaded images (%sx%s), (%sx&%s)" % (i1x, i1y, i2x, i2y)

result = cv2.matchTemplate(img1, img2, cv.CV_TM_SQDIFF_NORMED)

# We want the minimum squared difference
mn,_,match,_ = cv2.minMaxLoc(result)


# Extract the coordinates of our best match
mx,my = match

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = img1.shape[:2]

isect = ((mx,my), (mx+tcols,my+trows))
print "Found match of img1 in img2 at (%sx%s) to (%sx%s)" % (match[0], match[1], isect[1][0], isect[1][1])

# Step 3: Draw the rectangle on img2
# cv2.rectangle(img2, isect[0],isect[1],(0,255,0),3)

intersecting_img = img2[my:my+trows, mx:mx+tcols]

# Compare intersecting_img with img1 for differences

# dst = cv2.addWeighted(cropped_big,0.5,img1,0.5,0)

cv2.imwrite('/tmp/intersecting.png', intersecting_img)

call([
    'compare',
    # '-fuzz', '50%',
    # '-metric', 'rmse',
    '-compose', 'Src',
    '-highlight-color', 'red',
    '-lowlight-color', 'black',
    comp,
    '/tmp/some.png',
    dst
])

def highlights(src):
    img = cv2.imread(src)

    print type(img)

    return
    for x in img:
        for y in x:
            if np.sum(img[x][y]) != 0:
                print x, y

highlights(dst)

#cv2.imshow('output', intersecting_img)

#cv2.waitKey(0)
