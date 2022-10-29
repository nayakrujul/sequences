from setuptools import setup, find_packages

long_description = 'A very concise language - read the docs at https://www.github.com/nayakrujul/thon-symbols'

setup(
  name = 'thon-symbols',
  version = '1.15',
  license='Apache',
  description = 'A very concise language',
  author = 'Rujul Nayak',
  author_email = 'rujulnayak@outlook.com',
  url = 'https://github.com/nayakrujul/thon-symbols',
  download_url = 'https://github.com/nayakrujul/thon-symbols/archive/refs/tags/v114.tar.gz',
  keywords = ['golfing', 'code-golf', 'language'],
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  long_description=long_description,
  long_description_content_type='text/x-rst',
  packages = find_packages(),
  entry_points = {
    'console_scripts': [
      'thonsymbols = thon_symbols.main:from_cmdline'
    ]
  }
)
