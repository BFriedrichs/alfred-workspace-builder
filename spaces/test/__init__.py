from construct.blocks.workspace import Workspace
from construct.blocks.script_runner import ScriptRunner

test_workspace = Workspace(__file__, name='Test')

test_launcher = ScriptRunner(name='Launch API')
test_launcher.load_script(test_workspace.get_path('resources/launch_iterm.applescript'))
test_workspace.add_script(test_launcher)
