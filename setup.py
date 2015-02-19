import pyyts

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name=pyyts.__app_name__,
    version=pyyts.__version__,
    description=pyyts.__description__,
    author=pyyts.__author__,
    author_email=pyyts.__author_email__,
    packages=['pyyts'],
    install_requires=['requests'],
    url=pyyts.__app_url__,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'License :: Freeware',
    ),
    download_url=pyyts.__download_url__,
)