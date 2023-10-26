#!/usr/bin/env python3

from goon import Goon
from PIL import Image, ImageFilter
import sys

IMAGE_SIZE = (2048,2048)
CROP_SIZE = (200,-50,2100,1850)

def generate(token_id):
  # create goon object and get traits
  goon = Goon("og",token_id, 'pfp')
  goon.download_head('og')

  #load images
  base = Image.open('../images/layers/bred_dive.png').convert('RGBA')

  head= Image.open('../images/layers/og_heads/%d.png' % token_id)

  #resize & crop if necessary
  base = base.resize(IMAGE_SIZE)
  crop = head.crop(CROP_SIZE)
  crop = crop.resize(IMAGE_SIZE, Image.LANCZOS).rotate(6.9)

  #generate image
  final = Image.alpha_composite(base, crop)
  final.resize((1024,1024)).save('../images/pfp/dive/%d.png' % token_id)

if __name__ == '__main__':
  token_id = int(sys.argv[1])
  generate(token_id)
