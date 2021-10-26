from construct.blocks.resource import Resource, ListResource, DictResource


class ConnectionData(Resource):
  externals = dict(
    destinationuid='destinationuid',
    modifiers='modifiers',
    modifiersubtext='modifiersubtext',
    sourceoutputuid='sourceoutputuid',
    vitoclose='vitoclose'
  )
  def __init__(self, **kwargs):
    self.destinationuid = ''
    self.modifiers = 0
    self.modifiersubtext = ''
    self.sourceoutputuid = ''
    self.vitoclose = False

    super().__init__(**kwargs)


class Connections(DictResource):
  def __init__(self, filtering, conditional, workspaces, **kwargs):
    connection_data = {}

    connection_data[filtering.id] = ListResource([ConnectionData(destinationuid=conditional.id)])

    connection_data[conditional.id] = ListResource()

    for (workspace, cond_config) in zip(workspaces, conditional.config.conditions.items):
      scripts = workspace.scripts.items
      space_connection = ConnectionData(destinationuid=scripts[0].id, sourceoutputuid=cond_config.id)
      connection_data[conditional.id].add(space_connection)

      for i, script in enumerate(scripts[:-1]):
        connection_data[script.id] = ListResource([ConnectionData(destinationuid=scripts[i+1].id)])
    super().__init__(connection_data, **kwargs)
