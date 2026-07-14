---

## name: gpu-z
description: Use GPU-Z to capture GPU hardware specs and real-time sensor data. Trigger when the user wants to monitor GPU performance, capture GPU sensor data, diagnose GPU bottlenecks, learn how to use GPU-Z, or know anything about GPU-Z.

# Introduction

TechPowerUp GPU-Z is a free tool that shows detailed information about video cards and GPUs, such as clocks, memory, BIOS and more. It supports NVIDIA, AMD, ATI and Intel graphics devices. Official website: [https://www.techpowerup.com/gpuz/](https://www.techpowerup.com/gpuz/)

GPU-Z supports Windows 11 / Windows 10 / Windows 8 / Windows 7 / Vista / Windows XP (both 32 and 64 bit versions are supported).

# Download

Official website download: [https://www.techpowerup.com/download/techpowerup-gpu-z/](https://www.techpowerup.com/download/techpowerup-gpu-z/)

Download the latest **Standard Version** (`GPU-Z.<version>.exe`) from the page above. GPU-Z is portable — run the `.exe` directly with no installation required. 

# Usage

GPU-Z can be driven two ways. For **capturing data**, default to the CLI — it is headless, scriptable, and needs no user interaction. Use the GUI guide when the task centers on the on-screen window or on **teaching the user** how GPU-Z works.

## GPU-Z CLI Guide

Read [references/cli-guide.md](references/cli-guide.md) **before running any GPU-Z command**. This is the default path for almost every task. Use it when the user wants to:

- capture **static hardware specs** (GPU model, BIOS/driver version, VRAM, PCIe link);
- get **real-time GPU performance data** (clocks, temps, load, power);
- diagnose GPU bottlenecks / throttling.



## GPU-Z GUI Guide

Read [references/gui-guide.md](references/gui-guide.md) when the task centers on the **on-screen window** or on **teaching the user**. Use it when the user:

- wants to **interpret the meaning of fields/parameters** shown in the GUI (including reading a GPU-Z screenshot they share);
- wants to be **guided through learning / using GPU-Z** — what each tab, sensor, or the settings page is for;
- explicitly asks to **open / launch the GPU-Z window**.

Do **not** launch the GUI just to collect data — use CLI instead.