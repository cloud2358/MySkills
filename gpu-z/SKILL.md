---
name: gpu-z
description: Use GPU-Z to capture GPU hardware specs and real-time sensor data. Trigger when the user wants to monitor GPU performance, capture GPU sensor data, diagnose GPU bottlenecks, learn how to use GPU-Z, or know anything about GPU-Z.
---

# Introduction

TechPowerUp GPU-Z is a windows tool that shows detailed information about video cards and GPUs, such as clocks, memory, BIOS and more. It supports NVIDIA, AMD, ATI and Intel graphics devices.

Official website: [https://www.techpowerup.com/gpuz/](https://www.techpowerup.com/gpuz/)

# Scripts

## Find GPU-Z

Locate an existing GPU-Z installation:

```bash
cd skills/gpu-z
python scripts/find_gpuz.py
```

## Download & Install GPU-Z

If GPU-Z is missing, download it with winget and install it silently:

```bash
cd skills/gpu-z
python scripts/download_gpuz.py
```

## Get hardware specs

Export all GPU hardware specifications to `info/gpu_info.xml`:

```bash
cd skills/gpu-z
python scripts/dump_cards.py
```

## Get sensors data

Record sensors for the default 60 seconds, replacing any existing sensor log:

```bash
cd skills/gpu-z
python scripts/log_sensors.py
```

Set the recording duration with `-t` or `--time`:

```bash
cd skills/gpu-z
python scripts/log_sensors.py -t 30
python scripts/log_sensors.py --time 120
```

Append new samples to the existing sensor log:

```bash
cd skills/gpu-z
python scripts/log_sensors.py -a
python scripts/log_sensors.py --append
```

Sensor logs are written to `info/sensors_info.csv`.

> The number passed to `-t` or `--time` controls how long the GPU-Z process runs from startup to termination, **NOT** the exact sensor sampling time. GPU-Z needs several seconds to initialize before collecting data, so the real recording time is slightly shorter. Avoid using a very small value, which may end before the CSV is created or contains valid sensor data.

# Usage

- Whenever this skill is invoked, first run `python scripts/find_gpuz.py`. If GPU-Z is not found, state that clearly and tell the user that you can help install it.
- If the user accepts the Agent's offer to help install GPU-Z or directly asks the Agent to install it, run `python scripts/download_gpuz.py`.
- When the user wants to understand GPU performance, run both `python scripts/dump_cards.py` and `python scripts/log_sensors.py`. Read `info/gpu_info.xml` and `info/sensors_info.csv`, analyze the GPU's operating state, and use [references/perfcap-codes.md](references/perfcap-codes.md) to identify performance bottlenecks.
- The Agent may freely select and combine the `log_sensors.py` command-line parameters without requesting user approval.

# Further Information

Read these references only when the user wants to explore the corresponding GPU-Z details. Do not read them for routine installation, hardware capture, sensor logging, or performance analysis:

- Read [references/cli-guide.md](references/cli-guide.md) when the user wants an in-depth understanding of GPU-Z command-line parameters and behavior.
- Read [references/gui-guide.md](references/gui-guide.md) when the user wants an in-depth understanding of the GPU-Z window, tabs, fields, sensors, validation, or settings.