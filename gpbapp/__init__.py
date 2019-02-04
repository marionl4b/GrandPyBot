from flask import Flask

app = Flask(__name__)

from gpbapp import controler  # bottom import is a workaround to circular imports


