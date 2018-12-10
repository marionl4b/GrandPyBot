from flask import Flask

app = Flask(__name__)

from gpbapp import views  # bottom import is a workaround to circular imports


