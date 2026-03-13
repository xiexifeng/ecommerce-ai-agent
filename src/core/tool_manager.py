class ToolManager:
    def __init__(self):
        self.tools = {}

    def register_tool(self, name, tool):
        """Register a new tool with a unique name."""
        if name in self.tools:
            raise ValueError(f"Tool {name} is already registered.")
        self.tools[name] = tool

    def execute_tool(self, name, *args, **kwargs):
        """Execute a registered tool by name with provided arguments."""
        if name not in self.tools:
            raise ValueError(f"Tool {name} not found.")
        tool = self.tools[name]
        return tool(*args, **kwargs)