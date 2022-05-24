#!/usr/bin/env python3
import os
import sys

VERSION_PLACEHOLDER = '@version@'

def main():
  existing_tags = os.popen("git --no-pager tag").read().strip()
  print("Last repository tags:")
  print(existing_tags)
  new_version = input("Define new tag using semantic versioning (major.minor.patch): ")

  if new_version in existing_tags:
    sys.exit("version already exists")

  new_setup_file = ""
  with open("setup.template.py", "r") as f:
    new_setup_file = f.read()

  new_setup_file = new_setup_file.replace(VERSION_PLACEHOLDER, new_version)

  print("Writing new file...")
  with open("setup.py", "w") as f:
    f.write(new_setup_file)

  print("Commiting new changes...")
  r = os.popen("git add setup.py").read()
  if r:
    sys.exit("fail adding to stage: {}".format(r))
  r = os.popen('git commit -m "preparing for version {}"'.format(new_version)).read()

  print("Creating new tag...")
  r = os.popen("git tag {}".format(new_version)).read()
  if r:
    sys.exit("fail tagging: {}".format(r))

  print("Pushing new version...")
  r = os.popen("git push origin {}".format(new_version)).read()
  if r:
    sys.exit("fail pushing: {}".format(r))
  r = os.popen("git push").read()
  if r:
    sys.exit("fail pushing: {}".format(r))

main()