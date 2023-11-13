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
    attributes = dir(module)

    # Filter and print attributes that do not start with "__"
    for attr in sorted(attributes):
        if not attr.startswith("__"):
            print(attr)
