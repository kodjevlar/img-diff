# Titta
Image diff service

Use case: When making a pull request, a bot should be able to compare a screenshot from the original design

## Dependencies
- OpenCV for image manipulation

## What?

- Show what parts of the image that diffs (circles, arrows)
- Percentage of how well the images matches
- Color diffs
- Diffs in green/red GIT-style? (http://www.imagemagick.org/discourse-server/viewtopic.php?t=26105)

## How?

- Find the smallest / largest image
- Search for the best fit for the smaller image inside the bigger image
- Crop by the smallest image size (inside the big)
- Make a comparison between the two images to find the diffs.


- Search for the "test" image inside the "true" image
- Use these coordinates to place the test image onto the true image
- Crop by the intersection
- Point out the differences <- Epic
 - Shapes
 - Colors
