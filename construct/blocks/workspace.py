import os
from construct import util
from construct.blocks.resource import Resource, ListResource
from construct.blocks.script_runner import CleanupRunner

class Workspace(Resource):
  externals = dict(
    id='id',
    name='name',
    description='description',
    scripts='scripts',
    note='note'
  )

  def __init__(self, dir_path, cleanup=True, **kwargs):
    self.dir = os.path.dirname(dir_path)

    self.id = util.generate_id()
    self.name = 'Workspace'
    self.description = 'Open this workspace'
    self.scripts = ListResource()
    self.note = ''

    super().__init__(**kwargs)

    if cleanup:
      cleanup_runner = CleanupRunner()
      self.add_script(cleanup_runner)

  def add_script(self, script):
    self.scripts.add(script)

  def get_path(self, path):
    return os.path.join(self.dir, path)

  def construct(self):
      return self.scripts.construct()

  def full_construct(self):
      return super().construct()
