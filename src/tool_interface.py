from abc import ABC, abstractmethod
from typing import Any, Dict, Type

class BaseTool(ABC):
    @abstractmethod
    def execute(self, *args: Any, **kwargs: Any) -> Any:
        pass

@dataclass
class ToolParameter:
    name: str
    type: Type
    required: bool

@dataclass
class ToolResult:
    result: Any
    error: str = ''

    def is_success(self) -> bool:
        return not self.error