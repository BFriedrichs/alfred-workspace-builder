from construct.blocks.workspace import Workspace
from construct.blocks.script_runner import ScriptRunner

phd_workspace = Workspace(__file__, name='PhD')

api_launcher = ScriptRunner(name='Start Wrapper')
api_launcher.load_script(phd_workspace.get_path('resources/start_wrapper.applescript'))
phd_workspace.add_script(api_launcher)
