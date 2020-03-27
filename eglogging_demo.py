#!/usr/bin/python3

import traceback

from eglogging import *

if __name__ == '__main__':

  try:
    #logging_load_config_from_file('logger_config_DEFAULT.json')
    INFO('hello')
    WARN("Winter is coming.")

    logging_load_config_from_file('logger_config_ALTERNATE.json')
    DEBUG("is this alternate?")

  except Exception as ex:
    MSG("Exception: {}".format(ex))
    traceback.print_exc()
