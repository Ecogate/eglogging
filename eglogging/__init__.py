import os

from .eglogging import *

# eglogging version
__version__ = ''
version_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'VERSION')
with open(version_filepath, 'r') as fp:
  __version__ = fp.read()

# set what will get imported when someone writes "from eglogging import *"
__all__ = [ 'MSG', 'INFO', 'DEBUG', 'WARN', 'ERROR', 'CRITICAL', 'LOG',
            'logging_load_config_from_file', 'logging_load_human_config',
            'LOG_COLORS', '__version__' ]
