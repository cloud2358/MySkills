"""Export static GPU hardware specs via GPU-Z -dump."""

import subprocess
import time
from pathlib import Path

from find_gpuz import find_gpuz


def dump_cards() -> Path | None:
    """Export GPU hardware specs to info/gpu_info.xml."""
    gpuz = find_gpuz()
    if gpuz is None:
        print("GPU-Z.exe was not found. Run download_gpuz.py first.")
        return None

    output_dir = Path(__file__).resolve().parent.parent / "info"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "gpu_info.xml"
    output_file.unlink(missing_ok=True)

    gpuz_ps = str(gpuz).replace("'", "''")
    output_ps = str(output_file).replace("'", "''")

    command = (
        f"$process = Start-Process -FilePath '{gpuz_ps}' "
        f"-ArgumentList '-dump','{output_ps}' "
        "-Verb RunAs -WindowStyle Hidden -Wait -PassThru; "
        "exit $process.ExitCode"
    )

    print(f"Dumping GPU specs to: {output_file}")
    try:
        subprocess.run(
            ["powershell.exe", "-NoProfile", "-Command", command],
            check=True,
            timeout=60,
        )
    except FileNotFoundError:
        print("PowerShell was not found.")
        return None
    except subprocess.TimeoutExpired:
        print("GPU-Z dump timed out after 60 seconds.")
        return None
    except subprocess.CalledProcessError as error:
        print(f"GPU-Z dump failed with exit code {error.returncode}.")
        return None

    deadline = time.monotonic() + 5
    while time.monotonic() < deadline:
        if output_file.is_file() and output_file.stat().st_size > 0:
            print(f"GPU specs saved to: {output_file}")
            return output_file
        time.sleep(0.2)

    print("GPU-Z did not write any hardware data.")
    output_file.unlink(missing_ok=True)
    return None


if __name__ == "__main__":
    dump_cards()
