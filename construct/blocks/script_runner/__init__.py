import os
from construct.blocks.script import Script
from construct.blocks.script_runner import applescript, python

script_wrappers = {
  applescript.extension: applescript.wrapper,
  python.extenson: python.wrapper
}
user = os.environ['USER']
self_path = os.path.dirname(__file__)


class ScriptRunner(Script):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def load_script(self, path):
    script_data = None
    if not os.path.exists(path):
      raise FileNotFoundError(path)
    with open(path, encoding="utf-8") as fh:
      script_data = fh.read()

    for ext in script_wrappers:
      if path.endswith(ext):
        script_data = script_data.format(user=user)
        script_data = script_wrappers[ext].format(script=script_data, brackets='{}', user=user)
        break

    self.script_config.script = script_data

class CleanupRunner(ScriptRunner):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.name = 'Cleanup Previous'
    self.load_script(os.path.join(self_path, 'cleanup.applescript'))
