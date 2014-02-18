import os
from isso import make_app
from isso.core import Config
application = make_app(Config.load("/etc/isso.conf"))
