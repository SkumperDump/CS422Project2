"""
Author:               Scotty Wallace
Team:                 DUX D-Zine
Class:                CS 422
Professor:            Juan Flores, Kartikeya Sharma
Date Created:         11/12/2022
Date Last Modified:   11/12/2022

Description: This initializes our flask app
"""

import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    # binary secret key
    app.secret_key = b'goducks'
    app.config['UPLOAD_FOLDER'] = 'gbiv/static/images/'
    app.config['SITE_LOGO'] = 'gbiv/templates/logo_capture.PNG'

    # manually pushing app context
    with app.app_context():
        from . import gbiv
        app.register_blueprint(gbiv.bp)
        app.add_url_rule('/', endpoint='index')


    return app
