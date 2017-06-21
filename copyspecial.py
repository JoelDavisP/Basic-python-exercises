#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""
def get_spec_paths(dirct):
  fnames = os.listdir(dirct)
  fl_ls = []
  for f in fnames:
   match = re.search(r'(_\w+_)', f)
   if match:
     spec_file = os.path.abspath(os.path.join(dirct,f))
     fl_ls.append(spec_file)
  return fl_ls

def copy_to(paths,dirct):
  for i in paths:
   path_base = os.path.basename(i)    #Returns the basename of a specific path.
   new_path = os.path.join(dirct,path_base)
   shutil.copy(i,new_path)


def zip_to(paths, zipfile):
  cmnd = 'zip-j' + zipfile + ' ' + ' ' .join(paths)
  (status,output) = commands.getstatusoutput(cmnd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)

def main():
  path_list = []
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself. 
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
   

  for dirname in args:
   path_list.extend(get_spec_paths(dirname))

  if todir:
    copy_to(path_list, todir)
  elif tozip:
    zip_to(path_list, tozip)
  else:
    print '\n' 'Nothing to print'
  
if __name__ == "__main__":
  main()
