from construct.blocks.resource import Resource, ListResource, DictResource


class UIDataPos(Resource):
  externals = dict(
    xpos='xpos',
    ypos='ypos'
  )
  def __init__(self, **kwargs):
    self.xpos = 0
    self.ypos = 0

    super().__init__(**kwargs)


class UIData(DictResource):
  def __init__(self, filtering, conditional, workspaces, **kwargs):
    ui_data = {}

    x = 0
    y = 0
    for i, workspace in enumerate(workspaces):
      for j, script in enumerate(workspace.scripts.items):
        x = j * 150 + 500
        y = i * 150 + 20

        ui_data[script.id] = UIDataPos(xpos=x, ypos=y)

    ui_data[filtering.id] = UIDataPos(xpos=20, ypos=y / 2)
    ui_data[conditional.id] = UIDataPos(xpos=270, ypos=y / 2)

    super().__init__(ui_data, **kwargs)
