import subprocess
import sys
import os
import argparse

sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from config import settings

class ModeAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values not in ('mobile', 'desktop'):
            raise ValueError("Not valid value")
        setattr(namespace, self.dest, values)

class LangAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        os.environ["TEST_LANG"] = values
        setattr(namespace, self.dest, values)

parser = argparse.ArgumentParser(description="Run ui-tests")
parser.add_argument("--mode", action=ModeAction, help="Run mode: mobile or desktop")
parser.add_argument("--language", action=LangAction, help="Select localization")

args = parser.parse_args()

pytest_run_arr = ['py.test', 'tests', '-vv', '-l', '--driver', 'Chrome', '--html=report.html','--json=report.json']

tests_proc = subprocess.run(pytest_run_arr)

if tests_proc.returncode != 0:
    raise Exception('Some tests is failed.')
