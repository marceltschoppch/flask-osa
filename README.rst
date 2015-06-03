Flask-OSA
=============

Integrates the osa SOAP client `GitHub <https://github.com/marceltschoppch/osa>`_ into Flask.

Installation
------------

Flask-osa is pip installable:

	$ pip install Flask-osa

Configure
---------

The only configuration is ``OSA_URL`` and must be set. You can pass any kwargs to ``OSA()`` for further configuration. The kwargs will be passed to ``osa.client.Client()``.

Usage
-----

Import the extension into your Flask project and initialize:

	from flask.ext.osa import OSA

	osa = OSA(app)

Development
-----------

Source code is hosted on `GitHub <https://github.com/marceltschoppch/flask-osa>`_ (contributions are welcome).
