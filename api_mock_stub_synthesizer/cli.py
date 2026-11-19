"""CLI for Mock Synthesizer."""
import argparse
from .core import APIMockStubSynthesizer

def main():
    parser = argparse.ArgumentParser(description="API Mock Stub Synthesizer CLI")
    parser.add_argument("--demo", action="store_true", help="Run mock synthesizer demo")
    args = parser.parse_args()

    synth = APIMockStubSynthesizer()
    synth.register_endpoint("/api/v1/user", "GET", 200, {"id": 1, "username": "alice"})
    resp = synth.dispatch("GET", "/api/v1/user")
    print(f"Mock response: {resp}")

if __name__ == "__main__":
    main()
