import inspect
from construct.blocks.resource import Resource, ListResource
from construct import util

class ArgTypes:
  required = 0
  optional = 1
  not_required = 2

def filter_func(workspaces):
  import sys
  import json

  query = ''
  if len(sys.argv) > 1:
    query = sys.argv[1]
  query = query.lower()

  items = []
  for workspace in workspaces:
    short_name = workspace['name'].replace(' ', '').lower()
    if query not in short_name:
      continue
    items.append({
      'title': workspace['name'],
      'subtitle': workspace['description'],
      'arg': workspace['id']
    })

  sys.stdout.write(json.dumps({'items': items}))

def make_filter(json):
  lines = inspect.getsource(filter_func)
  lines += '\nfilter_func({})'.format(json)
  return lines

class Filter(Resource):
  externals = dict(
    config='config',
    type='type',
    id='uid',
    version='version'
  )
  def __init__(self, package, **kwargs):
    workspaces = [workspace.full_construct() for workspace in package.workspaces]
    self.config = FilterConfig(workspaces)
    self.type = 'alfred.workflow.input.scriptfilter'
    self.id = util.generate_id()
    self.version = 3

    super().__init__(**kwargs)

class FilterConfig(Resource):
  externals = dict(
    alfredfiltersresults='alfredfiltersresults',
    alfredfiltersresultsmatchmode='alfredfiltersresultsmatchmode',
    argumenttreatemptyqueryasnil='argumenttreatemptyqueryasnil',
    argumenttrimmode='argumenttrimmode',
    argumenttype='argumenttype',
    escaping='escaping',
    keyword='keyword',
    queuedelaycustom='queuedelaycustom',
    queuedelayimmediatelyinitially='queuedelayimmediatelyinitially',
    queuedelaymode='queuedelaymode',
    queuemode='queuemode',
    runningsubtext='runningsubtext',
    script='script',
    scriptargtype='scriptargtype',
    scriptfile='scriptfile',
    subtext='subtext',
    title='title',
    type='type',
    withspace='withspace'
  )
  def __init__(self, workspaces, **kwargs):
    self.alfredfiltersresults = False
    self.alfredfiltersresultsmatchmode = 0
    self.argumenttreatemptyqueryasnil = True
    self.argumenttrimmode = 0
    self.argumenttype = ArgTypes.optional
    self.escaping = 68
    self.keyword = 'ws'
    self.queuedelaycustom = 3
    self.queuedelayimmediatelyinitially = True
    self.queuedelaymode = 0
    self.queuemode = 0
    self.runningsubtext = ''
    self.script = make_filter(workspaces)
    self.scriptargtype = 1
    self.scriptfile = ''
    self.subtext = ''
    self.title = ''
    self.type = 3
    self.withspace = True

    super().__init__(**kwargs)
