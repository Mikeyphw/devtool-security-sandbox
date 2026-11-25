from pathlib import Path
import hashlib
import tomllib

root = Path(__file__).resolve().parent.parent
expected = {'.devtool.toml': '3e254bedea4b678322c455b15bfd643e9a35236f7fffa5ea2a7822eb91ff18f4', 'GA03-FIXTURE.txt': 'cf673f486934b75e4c234edfc3ceff156dbcc2a5c9d29b05f9e1043f07b6a638'}
for rel, digest in expected.items():
    p = root / rel
    if p.is_symlink() or not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != digest:
        raise SystemExit("GA03_FIXTURE_PAYLOAD_MISMATCH " + rel)
config = tomllib.loads((root / ".devtool.toml").read_text())
assert config["project"]["runner"] == "command"
assert config["federation"]["repositories"]["devtool"]["path"] == "~/Code/.worktrees/devtool/ga03-a010a4e32631"
assert config["federation"]["workflows"]["compatibility"]["steps"][0]["ref"] == "devtool::devtool::job:source-syntax"
print("GA03_FIXTURE_REQUIRED_VALIDATION_PASS")
