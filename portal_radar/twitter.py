import random
import re
import tweepy
import requests
import json
import traceback
import wonky_pfp
import poke
import gm
import bred
from goonerator import Goonerator

from messages import generate_message, generate_face_message
from goon import Goon
from os.path import exists

import goonauth

class TwitterHandler:
  def __init__(self):

    # authenticate the bot using the API keys and access tokens
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    self.api = tweepy.API(auth, wait_on_rate_limit = True)
    self.whami_id = 1458973540099764227

    since_cache = open("since_cache", "r")
    self.since_mention = int(since_cache.read())

  def get_api(self):
    return self.api

  #tweet a simple message
  def tweet(self, message):
    self.api.update_status(message)

  def tweet_body(self, destination, token_id):
    print(destination, token_id)
    file_path = '../images/full_body/%s/%s.png' % (destination, token_id)
    # check if file already exists
    goon = Goon(destination, token_id)
    if not exists(file_path):
      goon.download_image()
    message = generate_message(destination, token_id)
    first_tweet = self.api.update_status_with_media(filename = file_path, status = message)
    # return id for face method
    return first_tweet.id

  def tweet_head(self, destination, token_id, reply_id=None, message=None):
    file_path = '../images/pfp/%s/%s.png' % (destination, token_id)
    if not exists(file_path):
      if destination == 'wonky':
        wonky_pfp.generate_pfp(token_id)
      elif destination == 'poke':
        poke.generate(token_id)
      elif destination == 'gm':
        gm.generate(token_id)
      elif destination == 'dive':
        bred.generate(token_id)
      else:
        generator = Goonerator(token_id)
        generator.generate(destination)
    #generate unless overridden
    if message is None:
      message = generate_face_message()
    tweet = self.api.update_status_with_media(filename = file_path, status = message, in_reply_to_status_id=reply_id)

  # a function to check for mentions and handle them
  def check_mentions(self):
    for tweet in tweepy.Cursor(self.api.mentions_timeline, since_id = self.since_mention).items():
      self.since_mention = max(tweet.id, self.since_mention)
      if tweet.in_reply_to_status_id is not None:
        continue
      txt = tweet.text.lower()
      response = re.search('^[^!]*!wonky\D*(\d+).*', txt)
      if response:
        try:
          token_id = int(response.group(1))
          message = generate_face_message()
          message = '@%s %s' % (tweet.user.screen_name , message)
          self.tweet_head('wonky', token_id, tweet.id_str, message)
        except Exception as e:
          #self.send_dm('gone rogue')
          print(e)
          traceback.print_exc()

      response = re.search('^[^!]*!poke\D*(\d+).*', txt)
      if response:
        try:
          token_id = int(response.group(1))
          message = 'poke! :)'
          message = '@%s %s' % (tweet.user.screen_name , message)
          self.tweet_head('poke', token_id, tweet.id_str, message)
        except Exception as e:
          print(e)
          traceback.print_exc()

      response = re.search('^[^!]*!gm\D*(\d+).*', txt)
      if response:
        try:
          token_id = int(response.group(1))
          message = 'goon morning :)'
          message = '@%s %s' % (tweet.user.screen_name , message)
          self.tweet_head('gm', token_id, tweet.id_str, message)
        except Exception as e:
          print(e)
          traceback.print_exc()


      response = re.search('^[^!]*!toke\D*(\d+).*', txt)
      if response:
        try:
          token_id = int(response.group(1))
          print(token_id)
          message = 'toke?!?'
          message = '@%s %s' % (tweet.user.screen_name , message)
          self.tweet_head('toke', token_id, tweet.id_str, message)
        except Exception as e:
          print(e)
          traceback.print_exc()

      response = re.search('^[^!]*!octagoonz\D*(\d+).*', txt)
      if response:
        try:
          token_id = int(response.group(1))
          print(token_id)
          message = 'protect yourself at all times :)'
          message = '@%s %s' % (tweet.user.screen_name , message)
          self.tweet_head('octagoonz', token_id, tweet.id_str, message)
        except Exception as e:
          print(e)
          traceback.print_exc()

      response = re.search('^[^!]*!cageside\D*(\d+).*', txt)
      if response:
        try:
          token_id = int(response.group(1))
          print(token_id)
          message = 'there we go, we like that. well done!'
          message = '@%s %s' % (tweet.user.screen_name , message)
          self.tweet_head('cageside', token_id, tweet.id_str, message)
        except Exception as e:
          print(e)
          traceback.print_exc()

      response = re.search('^[^!]*!bucks\D*(\d+).*', txt)
      if response:
        try:
          token_id = int(response.group(1))
          print(token_id)
          message = 'mo money mo problems'
          message = '@%s %s' % (tweet.user.screen_name , message)
          self.tweet_head('bucks', token_id, tweet.id_str, message)
        except Exception as e:
          print(e)
          traceback.print_exc()

      response = re.search('^[^!]*!champ\D*(\d+).*', txt)
      if response:
        try:
          token_id = int(response.group(1))
          print(token_id)
          message = 'lets go champ!'
          message = '@%s %s' % (tweet.user.screen_name , message)
          self.tweet_head('champ', token_id, tweet.id_str, message)
        except Exception as e:
          print(e)
          traceback.print_exc()

      response = re.search('^[^!]*!bred\D*(\d+).*', txt)
      if response:
        try:
          token_id = int(response.group(1))
          print(token_id)
          message = 'lets get this bread'
          message = '@%s %s' % (tweet.user.screen_name , message)
          if random.random() > .9:
            self.tweet_head('dive', token_id, tweet.id_str, message)
          else:
            self.tweet_head('bred', token_id, tweet.id_str, message)
        except Exception as e:
          print(e)
          traceback.print_exc()

      response = re.search('^[^!]*!gang\D*(\d+).*', txt)
      if response:
        try:
          token_id = int(response.group(1))
          print(token_id)
          message = 'more wild than wu-tang'
          message = '@%s %s' % (tweet.user.screen_name , message)
          if random.random() < .9:
            self.tweet_head('gang', token_id, tweet.id_str, message)
          else:
            self.tweet_head('gangtats', token_id, tweet.id_str, message)
        except Exception as e:
          print(e)
          traceback.print_exc()

      response = re.search('^[^!]*!usa\D*(\d+).*', txt)
      if response:
        try:
          token_id = int(response.group(1))
          print(token_id)
          if random.random() > .1778:
            message = 'america, fuck yeah!'
            message = '@%s %s' % (tweet.user.screen_name , message)
            self.tweet_head('america', token_id, tweet.id_str, message)
          else:
            message = 'GOD SAVE THE KING'
            message = '@%s %s' % (tweet.user.screen_name , message)
            self.tweet_head('uk', token_id, tweet.id_str, message)
        except Exception as e:
          print(e)
          traceback.print_exc()

    return self.since_mention

  def send_dm(self, message):
    recipient_id = self.whami_id
    direct_message = self.api.send_direct_message(recipient_id, message)

