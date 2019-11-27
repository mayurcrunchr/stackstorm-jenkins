from lib import action
from jenkins import JenkinsException


class GetBuildConsoleOutput(action.JenkinsBaseAction):
    def run(self, project, number, config_override=None):
        if config_override is not None:
            self.config_override(config_override)
        try:
            console_output = self.jenkins.get_build_console_output(project, number)
            return console_output
        except JenkinsException as e:
            return False, {'error': str(e)}
