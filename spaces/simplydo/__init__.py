from construct.blocks.workspace import Workspace
from construct.blocks.script_runner import ScriptRunner

simplydo_workspace = Workspace(__file__, name='Simply Do')

api_launcher = ScriptRunner(name='Launch API')
api_launcher.load_script(simplydo_workspace.get_path('resources/launch_api.applescript'))
simplydo_workspace.add_script(api_launcher)

api_launcher = ScriptRunner(name='Launch Web')
api_launcher.load_script(simplydo_workspace.get_path('resources/launch_web.applescript'))
simplydo_workspace.add_script(api_launcher)

api_launcher = ScriptRunner(name='Open Trello')
api_launcher.load_script(simplydo_workspace.get_path('resources/open_trello.applescript'))
simplydo_workspace.add_script(api_launcher)
