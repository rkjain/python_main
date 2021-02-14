#!/usr/bin/env python3

import logging
logging.basicConfig(level=logging.DEBUG, filename="app.log")

logging.critical("critical")
logging.error("error")
logging.warning("warning")
logging.info("info")
logging.debug("debug")
