import os
import shutil
import time

from export import export

pref_path = "/Users/{}/Documents/AlfredPreferences/Alfred.alfredpreferences/workflows".format(os.environ['USER'])

def install():
  workflow_path, package = export()
  workflow_dir = os.path.basename(workflow_path)
  print(f'Installing {package.name} at {workflow_dir}')

  full_pref = os.path.join(pref_path, workflow_dir)
  if os.path.exists(full_pref):
    shutil.rmtree(full_pref)
  time.sleep(2)
  shutil.copytree(workflow_path, full_pref)

if __name__ == '__main__':
  install()
