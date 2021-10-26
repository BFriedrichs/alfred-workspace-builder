from os import mkdir
import subprocess
import os

from construct import make_package, export_package
from spaces import workspaces

def export(path='output'):
  os.makedirs(path, exist_ok=True)
  package = make_package(workspaces,
                         name='Workspaces',
                         bundleid='dev.bjornf.workspaces',
                         webaddress='https://bjornf.dev',
                         createdby='Björn Friedrichs',
                         description='Workspace opener')

  export_package(package, f'{path}/workspaces.json', dense=True)

  workflow_dir = f'{path}/user.workflow.{package.id}'
  os.makedirs(workflow_dir, exist_ok=True)
  subprocess.Popen(['plutil', '-convert', 'xml1', f'{path}/workspaces.json', '-o', f'{workflow_dir}/info.plist'])
  return workflow_dir, package

if __name__ == '__main__':
  export()
