import os
import re
import sys

def load_env(exports_path):
    env = dict(os.environ)
    if os.path.exists(exports_path):
        with open(exports_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("export ") and "=" in line:
                    k, v = line[7:].strip().split("=", 1)
                    env[k.strip()] = v.strip().strip('"\'')
    return env

def render(filepath, env):
    path = os.path.expanduser(filepath)
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    content = re.sub(
        r'\$\{([A-Za-z0-9_]+)\}|\$([A-Za-z0-9_]+)',
        lambda m: env.get(m.group(1) or m.group(2), m.group(0)),
        content
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    exports_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../rc/bash/exports"))
    env = load_env(exports_path)
    for f in sys.argv[1:]:
        render(f, env)
