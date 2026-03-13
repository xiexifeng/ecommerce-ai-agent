class ToolResult:
    def __init__(self, success: bool, data: dict = None, error: str = None):
        self.success = success
        self.data = data
        self.error = error

class BaseTool:
    def execute(self, *args, **kwargs) -> ToolResult:
        raise NotImplementedError("Execute method must be implemented in subclasses.")
