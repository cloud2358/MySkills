# GPU-Z CLI Guide

This is a manual for Agent to drive GPU-Z from the command line — to observe GPU parameters and performance, know how the GPU is running, and pinpoint GPU bottlenecks. 

## Find GPU-Z

GPU-Z is portable and its path is usually **not** on the system `PATH` / environment variables, so locate the executable before invoking it:

1. Check the common install locations:
   - `C:\Program Files\GPU-Z`
   - `C:\Program Files (x86)\GPU-Z`
2. If not found there, search the current workspace for a `GPU-Z*.exe`.
3. If it still cannot be found, ask the user for the path to GPU-Z.

```bash
# Probe the default install locations
ls "/c/Program Files/GPU-Z"/*.exe 2>/dev/null # 32 bit version
ls "/c/Program Files (x86)/GPU-Z"/*.exe 2>/dev/null # 64 bit version
```

Throughout the rest of this guide, the resolved GPU-Z directory is referred to as `<gpuz_path>` (e.g. `C:\Program Files\GPU-Z`). The executable is invoked as `<gpuz_path>\GPU-Z.exe`.

## CLI Parameters

| Flag | Purpose |
|------|---------|
| `-dump <file>` | Export static hardware specs as XML, then quit |
| `-log <file>` | Continuously log real-time sensor data (CSV) at ~1 Hz |
| `-minimized` | Start with window minimized to taskbar |
| `-tab <n>` | Open to tab *n* (1=Graphics Card, 2=Sensors, 3=Advanced, 4=Validation). Index is **1-based** |
| `-card <n>` | Select GPU *n* (1=GPU0, 2=GPU1). Index is **1-based** |
| `-install` | Launch the integrated installer |
| `-installSilent` | Silent install, no user interaction |
| `-help` | Show CLI Parameters (exclude `-log`) |

## Invoke from Bash

From Git Bash, route through PowerShell.

> **Note:** you **dont** need to run this command to launch GPU-Z, since `-dump` and `-log` start GPU-Z on their own. Only run when the user explicitly asks to do so.

**Default** — minimized (runs in background):

```bash
powershell.exe "& '<gpuz_path>\GPU-Z.exe' -minimized"
```

GUI (runs in desktop):

```bash
powershell.exe "& '<gpuz_path>\GPU-Z.exe'"
```

## Get Hardware Information

`-dump` launches GPU-Z, captures a snapshot of the **Graphics Card** tab, and silently quits.

```bash
powershell.exe "& '<gpuz_path>\GPU-Z.exe' -dump '$GPU_INFO'"
```

Output is a single `<gpu_info>` XML document with one `<card>` element per GPU.

Use `-dump` when you need to verify hardware identity, driver versions, or PCIe link speed etc.

## Get Real-Time GPU Performance

`-log` launches GPU-Z and writes sensor readings to a text file every second. **Stops when GPU-Z is closed** or "Log to file" is unchecked in the GUI.

### ⚠️ Process Lifecycle Rules (MUST Follow)

The GPU-Z `-log` process is **conversation-scoped**. You MUST obey these two rules:

| Rule | Requirement |
|------|-------------|
| **Single process** | At most ONE GPU-Z `-log` instance per conversation. Before starting a new `-log`, always check for and kill any existing GPU-Z process first. |
| **Kill on done** | When the monitoring goal is met, the user signals they are finished, or the conversation is wrapping up — you MUST kill the GPU-Z process. Never leave it running past the conversation end. |

### Pre-Launch Check (Always Run First)

```bash
# Check if GPU-Z is already running BEFORE launching -log
tasklist 2>/dev/null | grep -i "GPU-Z" && echo "GPU-Z IS RUNNING — kill it first" || echo "No GPU-Z running"
```

```bash
# Kill any existing GPU-Z before starting a new log session
powershell.exe "Start-Process -Verb RunAs taskkill '/f /im GPU-Z.exe'"
```

If GPU-Z was running, kill it, wait 1 second, then proceed.

### Start Logging

> **Note:** Use `Start-Process` (not `&` call operator) to launch GPU-Z as an independent process that survives the PowerShell session.

```bash
# Start logging minimized (runs in background)
powershell.exe "Start-Process '<gpuz_path>\GPU-Z.exe' -ArgumentList '-minimized', '-log', '<cwd>\sensor_info.csv'"
```

### Stop Logging (Kill Process)

```bash
# Stop logging — GPU-Z process terminates immediately
powershell.exe "Start-Process -Verb RunAs taskkill '/f /im GPU-Z.exe'"
```

> **Important:** The log file starts recording the moment `-log` runs and **keeps appending indefinitely** — it never stops on its own. You **must** kill the process when done. At conversation end, verify no GPU-Z remains with `tasklist | grep GPU-Z`.

The output is a CSV with these columns (varies by GPU):

| Column | Description |
|--------|-------------|
| Date | Timestamp (local) |
| GPU Clock [MHz] | Core clock (`-` when reading failed) |
| Memory Clock [MHz] | VRAM clock |
| GPU Temperature [°C] | Core temp |
| Hot Spot [°C] | Hottest sensor |
| Memory Used [MB] | VRAM in use |
| GPU Load [%] | Core utilization |
| Memory Controller Load [%] | VRAM controller activity |
| Bus Interface Load [%] | PCIe bandwidth utilization |
| Board Power Draw [W] | Total board power |
| GPU Chip Power Draw [W] | Core-only power |
| **PerfCap Reason []** | **Why GPU is throttling (numeric code)** |
| GPU Voltage [V] | Core voltage |
| CPU Temperature [°C] | CPU package temp |
| System Memory Used [MB] | Host RAM in use |

The `PerfCap Reason` is the most important argument for diagnosing where GPU meets its bottleneck. See [perfcap-codes.md](perfcap-codes.md) for the code mapping.

## Output Files

**Never write output in `<gpuz_path>`**. Always write the output files to the **current working directory**:

- `<gpu_info>` — the `-dump` XML file, written to `<cwd>\gpu_info.xml`
- `<sensor_info>` — the `-log` CSV file, written to `<cwd>\sensor_info.csv`