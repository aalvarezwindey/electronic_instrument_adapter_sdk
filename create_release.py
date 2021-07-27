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

  print("Commiting new changes...")
  os.popen("git add setup.py dist/")
  os.popen('git commit -m "preparing for version {}"'.format(new_version))
  os.popen("git tag {}".format(new_version))

main()