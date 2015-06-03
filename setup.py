from setuptools import setup


with open('README.rst') as fp:
    long_description = fp.read()

setup(
    name='Flask-OSA',
    version='0.1',
    download_url='https://github.com/marceltschoppch/flask-osa/',
    license='BSD',
    author='Marcel Tschopp',
    author_email='github@marceltschopp.ch',
    description='Integrates the osa SOAP client into Flask',
    long_description=long_description,
    py_modules=['flask_osa'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'osa',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
