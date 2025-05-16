from qwen_agent.tools.file import File as BaseFile

class FileTool(BaseFile):
    def __init__(self):
        super().__init__(root_dir='/')  # Full system access
