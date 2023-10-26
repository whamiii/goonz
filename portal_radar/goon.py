import json
import requests
from PIL import Image
from os.path import exists

#class to handle goon and images
class Goon:
  def __init__(self, destination, token_id, version='full_body'):
    # example path, ../images/full_body/og/67.png
    path_template = "../images/%s/%s/%d.png"
    self.file_path = path_template % (version, destination, token_id)
    self.ipfs_gateway = 'https://ipfs.cryptoongoonz.com/ipfs/'

    #set metadata url depending on destination
    if destination == 'og':
      if version == 'pfp':
        meta_url = self.ipfs_gateway + 'QmWrwrTVwN1tRwHvbeV3eCMxYC5RLNyMvBx5HCEXujHMGH/%d.json'
      else:
        meta_url = self.ipfs_gateway + 'QmVJZ8bGovrbt9ZBx9GXfB4Ji17GvcKC2bMfFeAej5kFdM/%d.json'
    else:
      meta_url = 'https://portal-metadata-api.cryptoongoonz.com/metadata/%d.json'
    self.meta_url = meta_url % token_id

    self.metadata = json.loads(requests.get(self.meta_url).text)
    self.token_id = token_id

    if not exists(self.file_path):
      self.download_image()
    self.image = Image.open(self.file_path)

  def get_trait(self, trait):
    #list of dicts
    attributes = self.metadata['attributes']
    result = list(filter(lambda attributes: attributes['trait_type'] == trait, attributes))
    return result[0]['value']


  def get_image(self):
    return self.image

  def write_image(self, image_data, path_override=None):
    #write to disk
    if path_override is not None:
      file_path = path_override
    else:
      file_path = self.file_path
    with open(file_path, 'wb') as handler:
      handler.write(image_data)

  #the resolution of these images is too damn high
  def resize_image(self, quality):
    image = self.get_image()
    #discard alpha channel
    rgb_image = self.image.convert('RGB')
    rgb_image.save(self.file_path, quality=quality)

  def download_image(self):
    ipfs_url = self.metadata['image']
    #trim the ipfs:// to get the useful bit
    image_url = self.ipfs_gateway + ipfs_url[7:]
    image_data = requests.get(image_url).content
    #save the image to file
    self.write_image(image_data)

  def layer_image(self, file_to_layer):
      img = self.get_image().convert('RGBA')
      layer = Image.open(file_to_layer)
      img = Image.alpha_composite(img, layer)
      return img

  #may be wonky exclusive
  def download_head(self, destination = 'wonky'):
    if destination == 'wonky':
      HEAD_AND_CHAIN = 0
      ipfs_url = self.metadata['extraAssets'][HEAD_AND_CHAIN]['value']
      image_url = self.ipfs_gateway + ipfs_url[7:]
    elif destination == 'og':
      ipfs_url = 'QmZ4aX1xokHXGFmvZTZLzUbRELA7hnoEtQ677DiVGczsFY/%d.png' % self.token_id
      image_url = self.ipfs_gateway + ipfs_url
    image_data = requests.get(image_url).content
    self.write_image(image_data, '../images/layers/%s_heads/%d.png' % (destination, self.token_id))


