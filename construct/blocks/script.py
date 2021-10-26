import os
from construct import util
from construct.blocks.resource import Resource, ListResource

class ScriptTypes:
  python = 3
  applescript = 6


class Script(Resource):
  externals = dict(
    id='uid',
    name='name',
    description='description',
    script_config='config',
    type='type',
    version='version'
  )

  def __init__(self, **kwargs):
    self.id = util.generate_id()
    self.name = 'Script'
    self.description = ''
    self.script_config = ScriptConfig()
    self.type = 'alfred.workflow.action.script'
    self.version = 2

    super().__init__(**kwargs)

class ScriptConfig(Resource):
  externals = dict(
    concurrently='concurrently',
    escaping='escaping',
    scriptargtype='scriptargtype',
    script='script',
    scriptfile='scriptfile',
    type='type'
  )

  def __init__(self, **kwargs):
    self.script = ''
    self.concurrently = False
    self.escaping = 68
    self.script = ''
    self.scriptargtype = 1
    self.scriptfile = ''
    self.type = ScriptTypes.applescript

    super().__init__(**kwargs)
