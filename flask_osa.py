from flask import current_app
from osa.client import Client


class OSA(object):
    """
    A thin wrapper around osa.client.Client()
    """
    def __init__(self, app=None, **kwargs):
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app, **kwargs):
        # using the app factory pattern _app_ctx_stack.top is None so what
        # do we register on? app.extensions looks a little hackish (I don't
        # know flask well enough to be sure), but that's how it's done in
        # flask-pymongo so let's use it for now.
        app.extensions['OSA'] = \
            Client(app.config['OSA_URL'], **kwargs)

    def __getattr__(self, item):
        if not 'OSA' in current_app.extensions.keys():
            raise Exception(
                'not initialised, did you forget to call init_app?')
        return getattr(current_app.extensions['OSA'], item)
