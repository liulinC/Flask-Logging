from distutils.core import setup

setup(
    name='Flask-Logging',
    version='0.1.3',
    packages=['flask_logging',],
    license='MIT',
    url='https://pypi.python.org/pypi/Flask-Logging',
    author='Nathan Cahill',
    author_email='nathan@nathancahill.com',
    long_description=open('README').read(),
    description='Filter certain requests from the Flask log.',
)
