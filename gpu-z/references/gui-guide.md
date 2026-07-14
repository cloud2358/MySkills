# GPU-Z GUI Guide

This is a manual for Agent to understand the GPU-Z window — what each tab shows and where to click. Use it to **interpret the meaning of on-screen fields/parameters** (e.g. reading a screenshot the user shares) and to **guide the user through learning and using GPU-Z**, as well as when the user interacts with the GUI directly (launch without `-minimized`).

Launch the full window with:

```bash
powershell.exe "& '<gpuz_path>\GPU-Z.exe'"
```

> **Note:** you **dont** need to run this command to open the window. Only launch the GUI when the user explicitly asks to do so.

The window has **four tabs** — `Graphics Card`, `Sensors`, `Advanced`, `Validation` — plus a **settings page** reached from the title-bar menu. A GPU selector dropdown sits at the **bottom-left** of every tab; on multi-GPU systems, switch cards there.

## Tab 1 — Graphics Card

The GPU's "identity card": **static** hardware facts that do not change while running. Sourced directly from GPU firmware and PCIe configuration space, so this is the most reliable tab.

Key fields:

- **Name** — the GPU model, with a `Lookup` button that opens the TechPowerUp GPU database page.
- **GPU / Revision** — the chip codename (e.g. `AD104`) and revision.
- **Technology / Die Size** — manufacturing process (nm) and die area.
- **Release Date / Transistors**.
- **BIOS Version** — with an adjacent icon to **save (back up) the graphics BIOS** to a `.rom` file. Back up the stock BIOS before any BIOS mod/overclock.
- **Device ID / Subvendor**.
- **Bus Interface** — PCIe link (e.g. `PCIe x16 4.0`), showing current vs. maximum negotiated speed.
- **Shaders / TMUs / ROPs**.
- **Memory Type / Size / Bus Width / Bandwidth** — e.g. `GDDR6X`, `12 GB`, `192 bit`.
- **Driver Version / Driver Date** — the installed driver; compare against the vendor site to decide if an update is needed.
- **GPU Clock / Memory Clock / Boost** — the **default/rated** clocks (live clocks live on the Sensors tab).
- **Computing** — supported compute APIs: `OpenCL`, `CUDA`, `PhysX`, `DirectCompute`, `Vulkan`, `Ray Tracing`.

Hovering over any field box shows a tooltip describing it.

## Tab 2 — Sensors

**Live, real-time** readings, updated ~once per second. This is the tab that matters for performance troubleshooting and monitoring under load. Each row is *Name → numeric value → a small graph*.

Common sensors (varies by GPU/vendor):

- **GPU Clock / Memory Clock** — actual live clocks.
- **GPU Temperature** — core temperature. Often the single most-watched value.
- **Hot Spot / Memory Junction Temperature** — hottest on-die sensor / VRAM temp.
- **Fan Speed** — in `%` and/or `RPM`.
- **GPU Load** — core utilization %. Should sit near 95–100% when a game is GPU-bound; a persistently low value under load points to a bottleneck elsewhere.
- **Memory Controller Load / Bus Interface Load** — VRAM controller activity / PCIe bandwidth utilization.
- **Board Power Draw / GPU Chip Power Draw** — total board power vs. GPU-package-only power.
- **GPU Voltage (VDDC)**.
- **PerfCap Reason** — why the GPU is throttling (power / thermal / voltage / idle). The key field for diagnosing bottlenecks; see [perfcap-codes.md](perfcap-codes.md).

At the bottom of this tab:

- **Log to file** checkbox — writes sensor readings to a CSV over time (the GUI equivalent of the `-log` CLI flag).
- Right-clicking a reading offers **Copy Value / Copy All**; each sensor can be switched to show highest / lowest / average reading.

## Tab 3 — Advanced

Deep, low-level technical detail for advanced troubleshooting and API/feature verification. Content is chosen from a **dropdown at the top of the tab**; it is read-only (GPU-Z does not edit these values).

Dropdown sections include:

- **General** — driver details, including the graphics driver registry path, and features like **Resizable BAR** and **Hardware-Accelerated GPU Scheduling** status.
- **BIOS** — VGA BIOS details and settings.
- **WDDM** — Windows Display Driver Model version (e.g. WDDM 2.7+).
- **DirectX** — feature levels and capabilities: Shader Model, DirectX Raytracing (DXR) tier, Mesh Shaders, per-version DX9/10/11/12 details.
- **Vulkan** — supported Vulkan version, extensions, and device capabilities.
- **OpenCL** — OpenCL platform/device capabilities.
- **CUDA** — CUDA compute capability and features (NVIDIA).
- **ASIC Quality** — leakage/quality estimate on supported cards.

Use this tab to confirm the latest drivers are active and to check which API features the card exposes.

## Tab 4 — Validation

Generates a unique **hash of your GPU configuration** for verification and sharing. Hashing happens locally; nothing is uploaded unless you explicitly submit it.

Uses:

- **Verify authenticity** — prove a card's real specs against TechPowerUp's database (useful when buying used, or for warranty claims with a timestamped screenshot).
- **Share settings** — publish an overclock/config so owners of the same card can reference safe settings.
- **Report bugs** — submit configuration data to the developers.

## Settings Page

Opened from the small **menu / gear icon in the title bar** (top-right). It configures how GPU-Z itself behaves rather than showing GPU data. Typical options:

- **General** — startup behavior (start minimized, minimize to tray, start with Windows), update checks, and window-on-top.
- **Sensors** — the **refresh/polling interval** (e.g. every 1–2 s), which sensors are active/visible, continue-refreshing-while-in-background and while-minimized options, and default log file settings.
- **ASIC Quality** — database submission options.
- **About** — version number, credits, and links.

For scripted/automated use, prefer the CLI flags in [cli-guide.md](cli-guide.md) over clicking through this page.
