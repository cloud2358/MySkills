"""Download and silently install GPU-Z."""

import subprocess
import tempfile
from pathlib import Path
from find_gpuz import find_gpuz

# 下载并静默安装 GPU-Z
# 参数 timeout 表示下载和安装的超时时间，单位为秒
def download_gpuz(timeout: int = 180) -> bool:
    # 如果 GPU-Z 已经安装，则返回安装路径
    installed = find_gpuz()
    if installed:
        print(f"GPU-Z already installed: {installed}")
        return True

    print("Downloading GPU-Z via winget...")
    try:
        with tempfile.TemporaryDirectory(prefix="gpuz-") as temp_dir:
            result = subprocess.run(
                [
                    "winget",
                    "download",
                    "--exact",
                    "--id",
                    "TechPowerUp.GPU-Z",
                    "--download-directory",
                    temp_dir,
                    "--accept-package-agreements",
                    "--accept-source-agreements",
                ],
                check=True,
                timeout=timeout,
            )
            
            source = next(Path(temp_dir).glob("*.exe"))
            print(f"Installing GPU-Z from: {source}")
            source_ps = str(source).replace("'", "''")
            install_command = (
                f"$process = Start-Process -FilePath '{source_ps}' "
                "-ArgumentList '-installSilent' -Verb RunAs -Wait -PassThru; "
                "exit $process.ExitCode"
            )
            subprocess.run(
                ["powershell.exe", "-NoProfile", "-Command", install_command],
                check=True,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout,
            )
    except FileNotFoundError:
        print("winget or PowerShell was not found.")
        return False
    except subprocess.TimeoutExpired:
        print(f"Download or installation timed out after {timeout} seconds.")
        return False
    except subprocess.CalledProcessError as error:
        stderr = (error.stderr or "").strip()
        print(stderr or f"Command failed with exit code {error.returncode}.")
        return False

    installed = find_gpuz()
    if not installed:
        print("GPU-Z installer completed, but GPU-Z.exe was not found.")
        return False

    print(f"GPU-Z installed to: {installed}")
    return True


if __name__ == "__main__":
    download_gpuz()