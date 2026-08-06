import json
import time
import urllib.request
import urllib.error
import os

def get_api_key():
    exports = os.path.join(os.path.dirname(__file__), "../../rc/bash/exports")
    with open(os.path.abspath(exports), encoding="utf-8") as f:
        for line in f:
            if line.startswith("export AI_API_KEY_2=") and "=" in line:
                return line.split("=", 1)[1].strip().strip('"\'')
    return os.environ.get("AI_API_KEY_2", "")

def load_models():
    cfg = os.path.join(os.path.dirname(__file__), "config.yaml")
    models = []
    with open(os.path.abspath(cfg), encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("- "):
                models.append(line[2:].strip())
    return models

def test_model(key, model, timeout=15):
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": "hi"}],
        "max_tokens": 5,
        "stream": False,
    }).encode()
    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }, method="POST")
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout):
            return round(time.time() - t0, 2)
    except urllib.error.HTTPError as e:
        return f"ERR {e.code}"
    except Exception:
        return "TIM"

if __name__ == "__main__":
    key = get_api_key()
    models = load_models()
    print(f"Testing {len(models)} models...\n")
    results = []
    for m in models:
        r = test_model(key, m)
        status = f"{r}s" if isinstance(r, float) else r
        print(f"{status:>8}  {m}")
        if isinstance(r, float):
            results.append((r, m))

    print("\n# Copy below to exports:")
    for idx, (latency, m) in enumerate(sorted(results), 1):
        print(f'export MODEL_2_{idx}="{m}"')
