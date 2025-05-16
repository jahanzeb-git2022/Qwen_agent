from qwen_agent.tools.shell import Shell as BaseShell

class ShellTool(BaseShell):
    def run(self, cmd):
        result = super().run(cmd)
        return f"STDOUT:\n{result}\nSTDERR:\n{self.last_stderr}"
