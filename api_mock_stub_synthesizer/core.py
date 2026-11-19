"""Core API Mock Stub Synthesizer."""
from typing import Dict, Any, Optional

class MockEndpoint:
    def __init__(self, path: str, method: str, response_status: int, response_body: Any):
        self.path = path
        self.method = method.upper()
        self.response_status = response_status
        self.response_body = response_body

class APIMockStubSynthesizer:
    def __init__(self):
        self.endpoints: Dict[str, MockEndpoint] = {}

    def register_endpoint(self, path: str, method: str, status: int, body: Any):
        key = f"{method.upper()}:{path}"
        self.endpoints[key] = MockEndpoint(path, method, status, body)

    def dispatch(self, method: str, path: str) -> Optional[Dict[str, Any]]:
        key = f"{method.upper()}:{path}"
        ep = self.endpoints.get(key)
        if not ep:
            return None
        return {"status": ep.response_status, "body": ep.response_body}
