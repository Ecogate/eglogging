#!/usr/bin/python3

import traceback

from eglogging import *

if __name__ == '__main__':

  try:
    #logging_load_config_from_file('logger_config_DEFAULT.json')
    print("----------- Using the default, machine-friendly config ------------")
    INFO('Hello')
    WARN("Winter is coming.")

    print("\n----------- Using a more human-friendly config --------------------")
    logging_load_human_config()
    # equivalent to logging_load_config_from_file('logger_config_HUMAN.json')

    INFO("This should be easier to read.")
    WARN("The night is dark and full of terror.")
    ERROR("They were dead, but now they walk! It's the white walkers!")

    # shows how to override the default color
    INFO("Arya's got this. See how I overwrote the default color?",
         color = LOG_COLORS['GREEN'])

  except Exception as ex:
    MSG("Exception: {}".format(ex))
    traceback.print_exc()
