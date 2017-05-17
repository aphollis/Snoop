import sys
from flask import Flask
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/SnoopProj/Snoop/")

from snoop import app as application
application.secret_key = 'gin&juice'
