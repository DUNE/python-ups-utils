from setuptools import setup
setup(name = 'ups-util',
      version = '0.0',
      description = 'UPS Utilities',
      author = 'Brett Viren',
      author_email = 'brett.viren@gmail.com',
      license = 'GPLv2',
      url = 'http://github.com/brettviren/ups-utils',
      package_dir = {'':'python'},
      packages = ['ups'],
      entry_points = {
          'console_scripts': [
              'ups-util = ups.main:main',
              ]
      }
              
  )