import json
from construct.package import Package

def make_package(workspaces, **args):
  package = Package(**args)
  for workspace in workspaces:
    package.add_workspace(workspace)
  return package

def export_package(package, path, dense=False):
  out = package.construct()
  with open(path, 'w+') as fh:
    if dense:
      json.dump(out, fh, indent=None, separators=(',', ':'))
    else:
      json.dump(out, fh, indent=2)
