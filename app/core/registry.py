from typing import Dict, Callable, Any

NODE_REGISTRY: Dict[str, Callable[[dict, dict], dict]] = {}
TOOLS: Dict[str, Callable[..., Any]] = {}