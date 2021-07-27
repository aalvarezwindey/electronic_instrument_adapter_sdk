#!/usr/bin/env python3
import os
import sys



def main():
  existing_tags = os.popen("git --no-pager tag").read().strip()
  print("Last repository tags:")
  print(existing_tags)
  new_version = input("Define new tag using semantic versioning (major.minor.patch): ")

  if new_version in existing_tags:
    sys.exit("version already exists")


  setup_file = f"""
from distutils.core import setup

setup(
  name = 'electronic_instrument_adapter_sdk',         # How you named your package folder (MyLib)
  packages = ['electronic_instrument_adapter_sdk'],   # Chose the same as "name"
  version = '{new_version}',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'SDK for Electronic Instrument Adapter',   # Give a short description about your library
  author = 'Ariel Alvarez Windey & Gabriel Robles',                   # Type in your name
  author_email = 'ajalvarez@fi.uba.ar',      # Type in your E-Mail
  url = 'https://github.com/aalvarezwindey/electronic_instrument_adapter_sdk',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/aalvarezwindey/electronic_instrument_adapter_sdk/archive/refs/tags/{new_version}.tar.gz',
  keywords = ['SDK', 'ELECTRONIC', 'INSTRUMENT', 'ADAPTER', 'FIUBA'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',      #Specify which pyhton versions that you want to support
  ],
)
"""

  with open("setup.py", "w") as f:
    print("Writing new setup file . . .")
    f.write(setup_file)

  print("New setup file generated")

  print("Commiting new changes...")
  os.popen("git add setup.py dist/")
  os.popen('git commit -m "preparing for version {}"'.format(new_version))
  os.popen("git tag {}".format(new_version))

main()