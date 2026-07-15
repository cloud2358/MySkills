"""Record GPU-Z sensor data for a fixed duration."""

import argparse
import subprocess
import time
from pathlib import Path

from find_gpuz import find_gpuz


def create_logging_process(gpuz: Path | str, output_file: Path | str) -> int:
    """Start a minimized GPU-Z logging process and return its process ID."""
    gpuz_ps = str(gpuz).replace("'", "''")
    output_ps = str(output_file).replace("'", "''")
    command = (
        f"$process = Start-Process -FilePath '{gpuz_ps}' "
        f"-ArgumentList '-minimized','-log','{output_ps}' "
        "-Verb RunAs -WindowStyle Minimized -PassThru; "
        "$process.Id"
    )
    result = subprocess.run(
        ["powershell.exe", "-NoProfile", "-Command", command],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return int(result.stdout.strip())


def kill_process_by_pid(process_id: int) -> None:
    """Force-stop a process by PID with administrator privileges."""
    if process_id <= 0:
        raise ValueError("process_id must be greater than zero")

    command = (
        "$process = Start-Process -FilePath 'taskkill.exe' "
        f"-ArgumentList '/PID','{process_id}','/F' "
        "-Verb RunAs -WindowStyle Hidden -Wait -PassThru; "
        "exit $process.ExitCode"
    )
    subprocess.run(
        ["powershell.exe", "-NoProfile", "-Command", command],
        check=True,
    )


def log_sensors(duration: int = 60, append: bool = False) -> Path | None:
    """Record GPU-Z sensors for duration seconds and return the CSV path."""
    if duration <= 0:
        raise ValueError("duration must be greater than zero")

    gpuz = find_gpuz()
    if gpuz is None:
        print("GPU-Z.exe was not found. Run download_gpuz.py first.")
        return None

    output_dir = Path(__file__).resolve().parent.parent / "info"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "sensors_info.csv"
    initial_size = output_file.stat().st_size if output_file.is_file() else 0
    if not append:
        output_file.unlink(missing_ok=True)
        initial_size = 0

    try:
        process_id = create_logging_process(gpuz, output_file)
    except (FileNotFoundError, subprocess.CalledProcessError, ValueError) as error:
        print(f"Could not start GPU-Z logging: {error}")
        if not append:
            output_file.unlink(missing_ok=True)
        return None

    print(f"Recording GPU sensors for {duration} seconds (PID: {process_id})...")
    try:
        time.sleep(duration)
    finally:
        kill_process_by_pid(process_id)

    if not output_file.is_file() or output_file.stat().st_size <= initial_size:
        print("GPU-Z did not write any sensor data.")
        if not append:
            output_file.unlink(missing_ok=True)
        return None

    print(f"Sensor data saved to: {output_file}")
    return output_file


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Record GPU-Z sensor data to info/sensors_info.csv."
    )
    parser.add_argument(
        "-t",
        "--time",
        type=int,
        default=60,
        dest="duration",
        metavar="SECONDS",
        help="recording duration in seconds (default: 60)",
    )
    parser.add_argument(
        "-a",
        "--append",
        action="store_true",
        help="append new sensor data to the existing CSV",
    )
    args = parser.parse_args()

    if args.duration <= 0:
        parser.error("--time must be greater than zero")

    return 0 if log_sensors(args.duration, append=args.append) else 1


if __name__ == "__main__":
    raise SystemExit(main())
