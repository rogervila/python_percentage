from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='python_percentage',
    packages=['python_percentage'],
    version='1.0.0',
    license='MIT',
    description='Calculate percentages without worrying about ZeroDivision errors',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Roger Vilà',
    author_email='rogervila@me.com',
    url='https://github.com/rogervila/python_percentage',
    download_url='https://github.com/rogervila/python_percentage/archive/1.0.0.tar.gz',
    keywords=['calculate percentages', 'python percentage',
              'float percentage', 'zerodivision', 'zero division'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)
