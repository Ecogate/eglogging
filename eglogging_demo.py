#!/usr/bin/python3

import traceback

from eglogging import *

if __name__ == '__main__':

  try:
    #logging_load_config_from_file('logger_config_DEFAULT.json')
    INFO('hello')
    WARN("Winter is coming.")

    DEBUG("Loading a more human-friendly config")
    logging_load_config_from_file('logger_config_HUMAN.json')
    ERROR("This isn't an error, but it should easier to read")

  except Exception as ex:
    MSG("Exception: {}".format(ex))
    traceback.print_exc()
