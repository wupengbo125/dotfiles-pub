import os
import sys

def merge_yaml(src_path, dst_path):
    dst = os.path.expanduser(dst_path)
    src = os.path.expanduser(src_path)
    if not os.path.exists(dst) or not os.path.exists(src):
        return

    with open(src, "r", encoding="utf-8") as f:
        src_lines = f.readlines()

    new_keys = {}
    in_model = False
    for line in src_lines:
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("model:"):
            in_model = True
            continue
        if in_model and ":" in s:
            k, v = s.split(":", 1)
            new_keys[k.strip()] = v.strip()

    if not new_keys:
        return

    with open(dst, "r", encoding="utf-8") as f:
        dst_lines = f.readlines()

    updated_lines = []
    found_model = False
    in_target_model = False
    keys_updated = set()

    for line in dst_lines:
        stripped = line.strip()
        if stripped == "model:" or stripped.startswith("model:"):
            found_model = True
            in_target_model = True
            updated_lines.append(line)
            continue

        if in_target_model:
            if line and not line[0].isspace() and not stripped.startswith("#"):
                for k, v in new_keys.items():
                    if k not in keys_updated:
                        updated_lines.append(f"  {k}: {v}\n")
                        keys_updated.add(k)
                in_target_model = False
            elif ":" in stripped and not stripped.startswith("#"):
                key_part = stripped.split(":", 1)[0].strip()
                if key_part in new_keys:
                    indent = line[:len(line) - len(line.lstrip())]
                    if not indent:
                        indent = "  "
                    updated_lines.append(f"{indent}{key_part}: {new_keys[key_part]}\n")
                    keys_updated.add(key_part)
                    continue

        updated_lines.append(line)

    if in_target_model:
        for k, v in new_keys.items():
            if k not in keys_updated:
                updated_lines.append(f"  {k}: {v}\n")
                keys_updated.add(k)
    elif not found_model:
        if updated_lines and not updated_lines[-1].endswith("\n"):
            updated_lines.append("\n")
        updated_lines.append("model:\n")
        for k, v in new_keys.items():
            updated_lines.append(f"  {k}: {v}\n")

    with open(dst, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        merge_yaml(sys.argv[1], sys.argv[2])
