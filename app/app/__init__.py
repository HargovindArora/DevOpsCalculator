from flask import Flask

app = Flask(__name__)

import logging
import logging.config
 
logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app.config.from_object("config.Config")

from app import views