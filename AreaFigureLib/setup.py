from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r' ) as f:
        return f.read()


setup(
    name='areafigure',
    version='0.0.1',
    author='OlegBaronov',
    author_email='alik2408@gmail.com',
    discriptioon='This module calculates the area of a figure',
    long_description=readme(),
    long_diskription_content_type='text/markdown',
    url='your_url',
    packages=find_packages(),
    install_requires=['requests>=2.25.1'],
    classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
    ],
    keywords='files speedfiles ',
    project_urls={
    'GitHub': 'your_github'
  },
  python_requires='>=3.6'



    )