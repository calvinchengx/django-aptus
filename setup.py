from setuptools import setup

setup(
    name='Django Aptus',
    version='0.0.4',
    packages=['aptus', ],
    license='LICENSE',
    description='useful django functionality',
    long_description=open('README.md').read(),
    author='Calvin Cheng',
    author_email='calvin@calvinx.com',
    install_requires=['distribute', ]
)
