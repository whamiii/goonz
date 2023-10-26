import random

# a function to generate messages for goonz entering the portal, returns an array
def generate_message(world='wonky', token_id=69, event='portal'):
  if event == 'portal':
    messages = ['goon #%d goes through the portal and comes out feeling %s!',
                'the portal takes goon #%d on a %s trip!',
                'goon #%d gets a taste of the %s side...',
                'goon #%d hopped into the portal, lets get %s baby!',
                'whoa! goon #%d is the newest visitor to %s world...']
  elif event == 'new':
    messages = ['goon #%d got %s on their first trip through the portal!',
                'goon #%d\'s first trip through the portal is a %s one!',
                'goon #%d is off on their first %s adventure!',
                'the portal takes goon #%d on their first ever %s trip!',
                'first time traveler! goon #%d just touched down in %s world...']
  return random.choice(messages) % (token_id, world)

def generate_face_message():
  #finally get a face message
  messages = ['nice face >:)',
              'say cheese :)',
              'i\'m the wonky school photographer!',
              'can the sales bot do this?!?',
              'boom, headshot',
              'smile for the camera :)',
              'ready for your close-up?']
  return random.choice(messages)


def hello_message():
  messages = ['Hello, world!', 'Hi, world!', 'Hey, world!', 'Welcome, world!', 'Greetings, world!',
              'Salutations, world!', 'Bonjour, world!', 'Hola, world!', 'Ni hao, world!', 'Ciao, world!']
  return random.choice(messages)


