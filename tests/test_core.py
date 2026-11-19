"""Tests for Mock Synthesizer."""
import unittest
from api_mock_stub_synthesizer.core import APIMockStubSynthesizer

class TestAPIMockStubSynthesizer(unittest.TestCase):
    def test_mock_dispatch(self):
        s = APIMockStubSynthesizer()
        s.register_endpoint("/items", "POST", 201, {"created": True})
        res = s.dispatch("POST", "/items")
        self.assertIsNotNone(res)
        self.assertEqual(res["status"], 201)
        self.assertEqual(res["body"]["created"], True)
