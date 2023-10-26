#!/usr/bin/env python3

from goon import Goon
from PIL import Image, ImageFilter
import sys

body_type = "regular"
IMAGE_SIZE = (2048,2048)
CROP_SIZE = (200,0,1669,1469)
CROP_OFFSET = (-300,123)

def generate_pfp(token_id, bg=True):
  # create goon object and get traits
  goon = Goon("wonky",token_id)
  goon.download_head()
  background = goon.get_trait('background')
  body_type = goon.get_trait('body')

  #load images
  if not bg:
    background = 'trans'
  base = Image.open('../images/layers/wonky_bg/%s.png' % background)

  try:
    body = Image.open('../images/layers/wonky_bodies/%s.png' % body_type)
  except:
    print(body)
    return
    #body = Image.open('../images/layers/wonky_bodies/regular.png')

  head= Image.open('../images/layers/wonky_heads/%d.png' % token_id)

  #resize & crop if necessary
  base = base.resize(IMAGE_SIZE)
  crop = head.crop(CROP_SIZE)
  crop = crop.resize((2420,2420), Image.LANCZOS).rotate(-6.9)
  crop = crop.crop((300,-148,2348,1900))

  #generate image
  final = Image.alpha_composite(base,body)
  final = Image.alpha_composite(final, crop)
  final.crop((100,200,1948,2048)).resize((1048,1048)).save('../images/pfp/wonky/%d.png' % token_id)

if __name__ == '__main__':
  print('being run...')
  token_id = int(sys.argv[1])
  print(token_id)
  generate_pfp(token_id)
