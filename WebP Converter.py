import os
import sys
from PIL import Image

# directory containing images
dir_path = 'path/to/dir'

# loop through all files in the directory
for file in os.listdir(dir_path):
  # ignore non-image files
  if not file.endswith('.png') and not file.endswith('.jpg'):
    continue

  # open image file
  img = Image.open(os.path.join(dir_path, file))

  # convert to webp format
  img.save(os.path.join(dir_path, file[:-3] + 'webp'), 'webp')

print('Finished converting images to webp format.')


"This script will loop through all files in the specified dir_path directory, ignore any files that are not png or jpg images, and then convert the images to the webp format and save them in the same directory."