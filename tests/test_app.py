import sys, os
# Add the project root (A.I.P) to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
def test_placeholder():
    assert True
import pytest
import runpy

def test_app_runs():
    # Simply checks if app.py executes without ImportError
    runpy.run_module("app.app", run_name="__main__")
