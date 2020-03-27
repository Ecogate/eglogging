# eglogging
Super-simple wrapper around python's logging library

To use it, import everything: `from eglogging import *`

You can then log a message `m` using these functions,
in order of increasing importance:

    DEBUG(m), INFO(m), MSG(m), WARN(m), ERROR(m), CRITICAL(m)

Note that `MSG(m)` is actually exactly the same as `INFO(m)`; it's provided for backwards-compatibility.

By default, configuration is loaded from `logger_config_DEFAULT.json`

In this default, the output will be formatted to
[logfmt](https://brandur.org/logfmt).

To load another configuration, just call `logging_load_config_from_file(fn)`,
where `fn` is the path to a json file containing a valid configuration.
For more info on how to set up the configuration, look
[here](https://docs.python.org/3.6/library/logging.config.html#logging-config-dictschema).
