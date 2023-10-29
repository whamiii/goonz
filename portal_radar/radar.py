#!/usr/bin/python3
import time
import random
import logging
import sys
import os
from twitter import TwitterHandler
from contract import ContractHandler
from sales import SalesHandler

logging.basicConfig(filename='log/radar.log', format='%(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

# a class for the radar
class Radar:
  def __init__(self):
    self.twitter = TwitterHandler()
    self.contract = ContractHandler()

  # a function to check for mentions and handle them
  def scan(self):
    new_goonz = self.contract.check_for_goonz()
    for goon in new_goonz:
      # is it the first time the goon has been portaled
      if len(goon) == 3:
        destination, token_id, new = goon
        print(goon)
      else:
        destination, token_id = goon
      reply_id = self.twitter.tweet_body(destination, token_id)
      self.twitter.tweet_head(destination, token_id, reply_id)
    return new_goonz


if __name__ == '__main__':
  logger.info('booting up the radar...')
  radar = Radar()
  while True:
    try:
      #radar.scan()
      since_id= radar.twitter.check_mentions()

      print('checking... beep.... %s' % str(since_id)[-3:])
    except KeyboardInterrupt:
      cache = 'echo %s > since_cache' % since_id
      os.system(cache)
      logger.info('exiting safely')
      sys.exit()
    except Exception as e:
      logger.error(e)
    finally:
      time.sleep(69)
else:
  logger.info('radar is being imported for testing')
  radar = Radar()
  radar.twitter.send_dm('test')
  #radar.twitter.check_mentions()
