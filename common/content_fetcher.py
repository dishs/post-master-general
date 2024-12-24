import requests
import signal
from contextlib import contextmanager

class TimeoutException(Exception): pass

@contextmanager
def time_limit(seconds):
  def signal_handler(signum, frame):
    raise TimeoutException

  signal.signal(signal.SIGALRM, signal_handler)
  signal.alarm(seconds)

  try:
    yield
  finally:
    signal.alarm(0)

def get_response(url):
  hdr = {'User-Agent':'Mozilla/5.0'}
  while True:
    try:
      # Waiting for 30 seconds to receive a response object
      with time_limit(120):
        content	= requests.get(url, headers=hdr).content
        break
    except Exception as e:
      print('Request Timeout!!')
      raise e
    pass
  return content

def post(url, data):
  try:
    response = requests.post(url, data=data)
  except Exception as e:
    print('POST Timeout!!')
    raise e  
  return response
