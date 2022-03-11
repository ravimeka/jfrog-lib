from setuptools import setup

setup(
    name='mylib',
    version='1.0.0',
    description='A Python library example',
    python_requires='>=3.8,<4.0',
    author='Author name',
    author_email='test@test.com',
    packages=[
        'mylib',
        'mylib.divers'
    ]
)