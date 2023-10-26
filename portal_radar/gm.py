#!/usr/bin/env python3

from goon import Goon
import sys
from PIL import Image, ImageFilter

def generate(token_id):
  goon = Goon('og', token_id, 'pfp')
  body = goon.get_trait('body')

  base = goon.get_image()
  try:
    arm = Image.open('../images/layers/gm/%s.png' % body)
  except:
    #probably a backpack or something similar
    arm = Image.open('../images/layers/gm/regular.png')
  finally:
    final = Image.alpha_composite(base, arm.resize(base.size))
    final.save('../images/pfp/gm/%s.png' % token_id)
