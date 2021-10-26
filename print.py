import pprint
from construct import start_construct, filter
from spaces import workspaces

if __name__ == '__main__':
  pprint.pprint(start_construct(workspaces))
