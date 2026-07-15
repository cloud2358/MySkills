from pathlib import Path
import os

# 列出 GPU-Z 可能的存放位置
def candidate_paths() -> list[Path]:
    paths: list[Path] = []
    # ProgramFiles 和 ProgramFiles(x86) 列入查找清单
    for key in ("ProgramFiles", "ProgramFiles(x86)"):
        root = os.environ.get(key)
        if root is not None:
            paths.append(Path(root) / "GPU-Z" / "GPU-Z.exe")
    # skill 文件夹列入查找清单
    skill_root = Path(__file__).resolve().parent.parent
    paths.append(skill_root / "GPU-Z.exe")
    return paths

# 在可能的存放位置中查找 GPU-Z.exe，返回文件存放路径或 None
def find_gpuz(debug: bool = False) -> Path | None:
    gpuz = None
    for path in candidate_paths():
        if path.is_file():
            gpuz = path
            break
    if gpuz is not None:
        if debug:
            print(f"GPU-Z.exe found at: {gpuz}")
        return gpuz
    if debug:
        print("Checked paths:")
        for path in candidate_paths():
            print(f"  - {path}")
        print("Cannot find GPU-Z.exe.")
    return None

if __name__ == "__main__":
    find_gpuz(debug=True)