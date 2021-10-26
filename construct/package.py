from typing import List
from construct.blocks.resource import DictResource, Resource, ListResource
from construct.ui import UIData
from construct.conditional import Conditional, ConditionalConfig, ConditionalItem
from construct.filtering import Filter
from construct.connection import Connections
from construct.util import generate_id

class Package(Resource):
  externals = dict(
    bundleid='bundleid',
    connections='connections',
    created_by='createdby',
    description='description',
    disabled='disabled',
    name='name',
    objects='objects',
    readme='readme',
    uidata='uidata',
    webaddress='webaddress'
  )

  def __init__(self, **kwargs):
    self.id = generate_id()
    self.bundleid = ''
    self.connections = DictResource({})
    self.created_by = ''
    self.description = ''
    self.disabled = False
    self.name = ''
    self.objects = ListResource()
    self.readme = ''
    self.uidata = DictResource({})
    self.webaddress = ''

    self.workspaces = []

    super().__init__(**kwargs)

  def add_workspace(self, workspace):
    self.workspaces.append(workspace)
    self.update()

  def update(self):
    cond_items = ListResource()
    for workspace in self.workspaces:
      name = workspace.name
      cond_item = ConditionalItem(matchstring=workspace.id, outputlabel=f'Run {name}')
      cond_items.add(cond_item)
    cond_config = ConditionalConfig(conditions=cond_items)
    conditional = Conditional(config=cond_config)
    filtering = Filter(self)

    self.uidata = UIData(filtering, conditional, self.workspaces)
    self.objects = ListResource([*self.workspaces, conditional, filtering], unravel=True)
    self.connections = Connections(filtering, conditional, self.workspaces)
