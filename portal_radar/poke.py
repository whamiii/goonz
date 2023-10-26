#!/usr/bin/env python3

from goon import Goon
import sys
from PIL import Image, ImageFilter

def generate(token_id):
  goon = Goon('og', token_id, 'pfp')
  body = goon.get_trait('body')

  base = goon.get_image()
  try:
    finger = Image.open('../images/layers/fingers/%s.png' % body)
  except:
    #probably a backpack or something similar
    finger = Image.open('../images/layers/fingers/regular.png')
  finally:
    final = Image.alpha_composite(base, finger.resize(base.size))
    final.save('../images/pfp/poke/%s.png' % token_id)
