# wrapper around python's logging module

import logging
import logging.config
import json
import inspect
import os

# set what will get imported when someone writes "from eglogging import *"
__all__ = ['MSG', 'INFO', 'DEBUG', 'WARN', 'ERROR', 'CRITICAL', 'LOG',
           'logging_load_config_from_file']

DEFAULT_CONFIG_FILENAME = 'logger_config_DEFAULT.json'
DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   DEFAULT_CONFIG_FILENAME)

# some shorthand accessors
def MSG(m):
  Eglogging._log(logging.INFO, m)
  return

def INFO(m):
  Eglogging._log(logging.INFO, m)
  return

def DEBUG(m):
  Eglogging._log(logging.DEBUG, m)
  return

def WARN(m):
  Eglogging._log(logging.WARNING, m)
  return

def ERROR(m):
  Eglogging._log(logging.ERROR, m)
  return

def CRITICAL(m):
  Eglogging._log(logging.CRITICAL, m)
  return

def LOG(m, level = logging.NOTSET):
  Eglogging._log(level, m)
  return

def logging_load_config_from_file(filename):
  Eglogging.load_config_from_file(filename)
  return



class Eglogging(object):
  """wrapper around python's logging module"""

  # make the logger variable static
  logger = None


  @staticmethod
  def load_config_from_file(filename):
    'load logging config from a json file'

    with open(filename, 'r') as f:
      config_dict = json.load(f)

    logging.config.dictConfig(config_dict)

    # get the logger
    Eglogging.logger = logging.getLogger(__name__) # __name__ is eglogging
    return


  @staticmethod
  def _log(level, m):
    # log message m at the info level
    myfields = { 'line': Eglogging._line_info() }
    Eglogging.logger.log(level, m, extra = myfields)


  @staticmethod
  def _line_info():
    '''
    get the file and line number from which stuff is getting logged
    formatted like filename:NN
    '''
    try:
      stack = inspect.stack()
      frame = stack[3]

      # filename: only show the last part
      fn = frame[1]
      slash = fn.rfind('/')
      if slash != -1:
        fn = fn[slash + 1 :]

      return "{}:{}".format(fn, frame[2])

    except Exception as e:
      print("Exception encountered in line_info(): {}".format(e))
      return "ERROR"



########################## INITIALIZE THE LOGGER ###############################
Eglogging.load_config_from_file(DEFAULT_CONFIG_PATH)
