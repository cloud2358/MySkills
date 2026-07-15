# GPU-Z GUI Guide

GPU-Z presents graphics adapter identity, live sensors, API capabilities, and validation information through a tabbed Windows interface.

The main window has four tabs: `Graphics Card`, `Sensors`, `Advanced`, and `Validation`. A GPU selector at the bottom of the window determines which adapter is displayed on multi-GPU systems. The title-bar menu opens GPU-Z settings.

## Tab 1 — Graphics Card

The Graphics Card tab summarizes relatively static adapter information assembled from the detected hardware, VBIOS, graphics driver, and Windows.

Key fields include:

- **Name** — detected GPU model, with a `Lookup` button that opens the corresponding TechPowerUp GPU database page.
- **GPU / Revision** — GPU codename and silicon revision.
- **Technology / Die Size** — manufacturing process and die area when known.
- **Release Date / Transistors** — reference specifications when available.
- **BIOS Version** — detected VBIOS version; the adjacent icon can save a copy of the VBIOS on supported cards.
- **Device ID / Subvendor** — PCI device identity and board vendor.
- **Bus Interface** — supported and currently negotiated PCIe link information. The adjacent render test can place load on the GPU so the active link state can be observed.
- **Shaders / TMUs / ROPs** — detected processing-resource counts.
- **Memory Type / Size / Bus Width / Bandwidth** — detected video-memory characteristics.
- **Driver Version / Driver Date** — metadata for the installed graphics driver.
- **GPU Clock / Memory Clock / Boost** — reported default and boost clock specifications; live clocks are shown on the Sensors tab.
- **Computing** — support indicators such as OpenCL, CUDA, DirectCompute, and DirectML, depending on the GPU and driver.
- **Technologies** — support indicators such as Vulkan, Ray Tracing, PhysX, and OpenGL, depending on the GPU and driver.

Available fields vary by GPU vendor, architecture, driver, and GPU-Z version. Hovering over many fields displays an explanatory tooltip.

## Tab 2 — Sensors

The Sensors tab displays live readings as numeric values and small history graphs. The default refresh interval is approximately one second and can be changed in sensor settings. Available sensors depend on the GPU, driver, and monitoring hardware.

Common sensors include:

- **GPU Clock / Memory Clock** — current operating clocks.
- **GPU Temperature** — reported core temperature.
- **Hot Spot / Memory Junction Temperature** — hottest reported die sensor or memory-junction temperature when supported.
- **Fan Speed** — fan duty percentage and/or RPM when exposed by the card.
- **GPU Load** — reported graphics-engine utilization. Values near 100% are common in GPU-bound uncapped workloads; frame limits, VSync, workload variation, CPU limits, and other constraints can produce lower values.
- **Memory Controller Load / Bus Interface Load** — memory-controller and PCIe activity.
- **Board Power Draw / GPU Chip Power Draw** — board-level or GPU-package power measurements when supported.
- **GPU Voltage** — reported GPU voltage.
- **PerfCap Reason** — NVIDIA performance-policy reason that currently limits additional boosting. This sensor is hardware-specific; see [perfcap-codes.md](perfcap-codes.md).

The **Log to file** option writes sensor samples to a CSV file. Sensor controls can expose current, minimum, maximum, or average display modes, depending on the GPU-Z version.

## Tab 3 — Advanced

The Advanced tab provides read-only driver, firmware, operating-system, and graphics-API details selected from a dropdown. Available pages depend on the GPU, driver, Windows version, and GPU-Z version.

Common pages include:

- **General** — device location, driver registry path, ECC status, and other adapter or driver details.
- **BIOS** — VBIOS information.
- **WDDM** — Windows Display Driver Model capabilities.
- **DirectX** — feature levels, Shader Model, DirectX Raytracing, Mesh Shaders, and related capabilities.
- **Vulkan / OpenCL / CUDA** — API versions, extensions, and device capabilities when supported.
- **PCIe Resizable BAR** — Resizable BAR status and relevant requirements on supported systems.

Hardware-Accelerated GPU Scheduling and other Windows graphics capabilities may also appear in Advanced pages.

## Tab 4 — Validation

The Validation tab submits the detected GPU configuration to TechPowerUp when the user chooses to submit it. A successful submission returns a validation ID and a web page that can be shared for comparison or troubleshooting.

The submitted record reflects the configuration reported by the system at submission time. Validation entries are useful for sharing detected specifications and diagnostic context. The tab can also provide fields for bug-report submissions, depending on the GPU-Z version.

## Settings

The title-bar menu opens settings for GPU-Z behavior and sensor monitoring. Common controls include startup behavior, update checks, the initial tab, minimize behavior, sensor refresh rate, temperature units, background refresh, active sensors, display mode, and logging preferences.

ASIC Quality is a legacy reading available only on certain older GPU architectures and may not appear on modern cards.
