from setuptools import setup

setup(
    name='social-auth-liu',
    version='0.0.4',
    py_modules=['social_liu'],
    url='https://github.com/Baljan/python-social-auth-liu',
    license='MIT',
    author='Olle Vidner',
    author_email='olle@vidner.se',
    description='',
    install_requires=[
        'social-auth-core==4.*',
        'PyJWT==2.*',
        'cryptography==3.*',
    ]
)
