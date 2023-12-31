from setuptools import setup, find_packages

setup(
    name='fast_logger',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='A fast and simple logging decorator for Python functions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ron Meck',
    author_email='ronmeck@gmail.com',
    url='https://github.com/dad2jrn/fast_logger',
    install_requires=[
        # Dependencies, if any
    ],
)
