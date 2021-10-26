from construct.blocks.resource import Resource, ListResource
from construct import util

class ConditionalItem(Resource):
  externals = dict(
    inputstring='inputstring',
    matchcasesensitive='matchcasesensitive',
    matchmode='matchmode',
    matchstring='matchstring',
    outputlabel='outputlabel',
    id='uid'
  )

  def __init__(self, **kwargs):
    self.inputstring = '{query}'
    self.matchcasesensitive = False
    self.matchmode = 0
    self.matchstring = ''
    self.outputlabel = 'Run' # decor
    self.id = util.generate_id()

    super().__init__(**kwargs)

class ConditionalConfig(Resource):
  externals = dict(
    conditions='conditions',
    elselabel='elselabel'
  )

  def __init__(self, **kwargs):
    self.conditions = ListResource()
    self.elselabel = 'else'

    super().__init__(**kwargs)


class Conditional(Resource):
  externals = dict(
    config='config',
    type='type',
    version='version',
    id='uid'
  )

  def __init__(self, **kwargs):
    self.config = ConditionalConfig()
    self.type = 'alfred.workflow.utility.conditional'
    self.version = 1
    self.id = util.generate_id()

    super().__init__(**kwargs)

