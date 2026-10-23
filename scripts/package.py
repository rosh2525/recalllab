"""Package an explicit allowlist, excluding runtime data and all credentials."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
root=Path(__file__).resolve().parents[1]
files=[root/p for p in ['README.md','CONTRIBUTING.md','LICENSE','run.sh','.gitignore','.env.example','backend/requirements.txt','backend/requirements-dev.txt','backend/requirements.lock.txt','backend/pyproject.toml','backend/evaluate.py','frontend/package.json','frontend/package-lock.json','frontend/tsconfig.json','frontend/vite.config.ts','frontend/index.html']]
for folder in ['backend/recalllab','backend/tests','frontend/src','frontend/dist','docs','evaluation','scripts','.github']:
 files.extend(p for p in (root/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in ('.pyc','.sqlite3') and not p.name.endswith('-report.json'))
out=root/'output'/'recalllab-source.zip';out.parent.mkdir(exist_ok=True)
with ZipFile(out,'w',ZIP_DEFLATED) as z:
 for p in sorted(set(files)):
  if p.exists():z.write(p,Path('recalllab')/p.relative_to(root))
with ZipFile(out) as z:
 assert z.testzip() is None
 assert not any('/data/' in n or '/.venv/' in n or '/node_modules/' in n or n.endswith('/.env') for n in z.namelist())
 print(f'Packaged {len(z.namelist())} files; {out.stat().st_size:,} bytes.')
print(out)
