#!/usr/bin/env python3

from goon import Goon
from PIL import Image, ImageFilter
import sys
import os.path

class Goonerator:
    def __init__(self, token_id):
        self.token_id = token_id
        #map code to destination
        self.code_dict = {
          'stake': 'wonky'
          }

    def generate(self, code):
        # set image file path and name
        image_file = f'../images/pfp/{code}/{self.token_id}.png'
        # check if image exists
        if os.path.exists(image_file):
            print("Image %s already exists." % code)
            return
        else:
          try:
            destination = self.code_dict[code]
            goon = Goon(destination, self.token_id, 'pfp')
          except KeyError:
            goon = Goon('og', self.token_id, 'pfp')
          except:
            print('fuuuuuck')
            return

          base = goon.get_image()
          layer = Image.open(f'../images/layers/{code}.png')
          final = Image.alpha_composite(base, layer.resize(base.size))
          final.save(image_file)

if __name__ == '__main__':
    token_id = int(sys.argv[1])

    image_generator = Goonerator(token_id)
    image_generator.generate('stake')

