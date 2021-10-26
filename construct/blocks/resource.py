import json

class Resource:
  externals = dict()

  def __init__(self, **kwargs):
    for in_arg, ex_arg in self.externals.items():
      if ex_arg in kwargs:
        setattr(self, in_arg, kwargs[ex_arg])

  def construct(self):
    result = dict()
    for in_arg, ex_arg in self.externals.items():
      arg = getattr(self, in_arg)
      if isinstance(arg, Resource):
        arg = arg.construct()
      result[ex_arg] = arg

    return result

class ListResource(Resource):
  externals = dict(
    items='items'
  )

  def __init__(self, items=[], unravel=False, **kwargs):
    self.items = items[:]
    self.unravel = unravel
    super().__init__(**kwargs)

  def construct(self, unravel=False):
    result = [item.construct() for item in self.items]
    if self.unravel or unravel:
      result = [item for sublist in result for item in (sublist if type(sublist) == list else [sublist])]

    return result

  def add(self, element):
    self.items.append(element)


class DictResource(Resource):
  def __init__(self, externals, **kwargs):
    self.externals = {**self.externals, **{k: k for k in externals.keys()}}

    for k, v in externals.items():
      setattr(self, k, v)

    super().__init__(**kwargs)
