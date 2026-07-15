# GPU-Z CLI Reference

GPU-Z is fundamentally a Windows GUI application with a small command-line interface for startup selection, hardware export, sensor logging, and installation. **Because direct CLI usage and parameter combinations may behave inconsistently, use the wrapper scripts under `scripts/` instead of invoking GPU-Z commands directly to avoid unexpected errors**.

## Executable Locations

GPU-Z is portable and usually is not registered on `PATH`. Common locations include:

- `C:\Program Files\GPU-Z\GPU-Z.exe`
- `C:\Program Files (x86)\GPU-Z\GPU-Z.exe`

## CLI Parameters

| Flag | Purpose |
|------|---------|
| `-install` | Interactive installation |
| `-installSilent` | Silent installation |
| `-help` | Show help window |
| `-tab <index>` | Select startup TAB |
| `-card <index>` | Select startup GPU |
| `-minimized` | Start minimized |
| `-dump <file>` | Export hardware XML |
| `-log <file>` | Log sensors to CSV |

`-tab` and `-card` use one-based indices.

## Command Behavior

### `-install`

`-install` opens the integrated GPU-Z installer. The only user-configurable option is whether to create a desktop shortcut. `GPU-Z.exe` is typically installed in either `C:\Program Files\GPU-Z\` or `C:\Program Files (x86)\GPU-Z\` depending on the system.

### `-installSilent`

`-installSilent` runs the integrated installer without installer interaction. It will create a desktop shortcut by default. Same as `-install`, `GPU-Z.exe` is typically installed in either `C:\Program Files\GPU-Z\` or `C:\Program Files (x86)\GPU-Z\` depending on the system.

### `-help`

`-help` shows a help window listing only `-install`, `-installSilent`, `-help`, `-tab`, `-card`, `-minimized`, and `-dump`; it does not list `-log`.

### `-tab <index>`

`-tab` selects the initially displayed tab using a one-based index: `1` for Graphics Card, `2` for Sensors, `3` for Advanced, and `4` for Validation. Any value outside the range `1`–`4` defaults to the Graphics Card tab.

### `-card <index>`

`-card` selects a GPU using a one-based index. `1` corresponds to GPU0, `2` to GPU1, and so on. An index beyond the available range selects the nearest available card. For example, if GPU7 is the highest-indexed card, `-card 8` selects GPU7, and any value greater than `8` also defaults to GPU7.

### `-minimized`

`-minimized` start GPU-Z with minimized. GPU-Z remains a GUI application rather than becoming a console or headless service.

### `-dump <file>`

`-dump` creates one `<file>` XML document and then exits. The document contains one `<card>` element per detected GPU and includes model identity, BIOS and driver versions, VRAM, clock information, and PCIe link data etc.

### `-log <file>`

`-log` opens GPU-Z and continuously appends sensor samples to the selected `<file>` CSV file at approximately 1 Hz. GPU-Z has no documented duration or runtime stop parameter. Logging ends when it is disabled in the GUI or when the GPU-Z process exits.