from disutils.core import setup

setup(
    name='Django Aptus',
    version='0.0.2',
    packages=['aptus', ],
    license='LICENSE',
    description='useful django functionality',
    long_description=open('README.md').read(),
    author='Calvin Cheng',
    author_email='calvin@calvinx.com',
    install_requires=['disutils', ]
)
