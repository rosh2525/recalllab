"""Run local release checks. No AWS calls, credentials or learner-data mutations."""
import os
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
env = {**os.environ, 'RECALLLAB_ENABLE_BEDROCK': '0', 'PYTHONPATH': str(root / 'backend')}
commands = [
    [sys.executable, '-m', 'pip', 'check'],
    [sys.executable, '-m', 'pytest', 'backend/tests', '-q'],
    ['npm', '--prefix', 'frontend', 'run', 'build'],
    ['npm', '--prefix', 'frontend', 'audit', '--omit=dev', '--audit-level=high'],
    [sys.executable, 'backend/evaluate.py'],
    [sys.executable, 'scripts/package.py'],
]
for command in commands:
    print('Checking: ' + ' '.join(command), flush=True)
    subprocess.run(command, cwd=root, env=env, check=True)
print('Local release checks passed. Live model and participant evidence remain separate.')
