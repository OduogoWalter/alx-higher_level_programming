#!/usr/bin/python3
import dis
import importlib.util
import sys

if __name__ == "__main__":
    # Load the compiled module
    spec = importlib.util.spec_from_file_location("hidden_4", "hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get all attributes of the module
    attributes = [attr for attr in dir(module) if not attr.startswith("__")]

    # Print one name per line in alphabetical order
    for attr in sorted(attributes):
        print(attr)
