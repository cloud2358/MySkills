# NVIDIA PerfCap Reason Codes

The `PerfCap Reason` reported by GPU-Z comes from NVAPI's `NV_GPU_PERF_POLICY_ID` flags. In the **log file** it is written as a single **numeric bitmask**; in the **Sensors tab** it is shown as the matching short names.

Because it is a bitmask, **multiple limits can be active at once and their values add up**. For example a logged value of `5` = `1` (Pwr) + `4` (VRel).

| Bit value | Name | NVAPI id | Meaning |
|-----------|------|----------|---------|
| 0 | None | — | No performance cap — GPU is running unrestricted |
| 1 | Pwr | `SW_POWER` | Power limit — GPU is hitting the total board power (TBP) cap |
| 2 | Thrm | `SW_THERMAL` | Thermal limit — GPU is throttling to stay below its temperature threshold |
| 4 | VRel | `SW_RELIABILITY` | Reliability voltage — the V/F curve won't allow a higher clock because the auto-set voltage is already at the highest safe level |
| 8 | VOp | `SW_OPERATING` | Operating voltage — GPU is at the maximum operating voltage (hardware limit) |
| 16 | Util | `SW_UTILIZATION` | Utilization — load is too low to justify boosting (also shown as **Idle** in newer GPU-Z versions) |

Combined examples: `3` = Pwr + Thrm; `5` = Pwr + VRel; `6` = Thrm + VRel; `20` = VRel + Util.

## How to Use

1. Start GPU-Z logging at the moment a performance problem occurs:
   ```
   GPU-Z.exe -minimized -log sensors_info.csv
   ```
2. Reproduce the issue.
3. Close GPU-Z.
4. Check the `PerfCap Reason` column around the timestamps when stuttering happened.

## Interpreting Results

First decompose the logged number into its bits, then read each active flag:

- **Pwr (1)** → GPU is power-limited. Consider increasing the power target in an overclocking tool, or this may indicate a firmware-imposed cap (common on laptops and OEM systems).
- **Thrm (2)** → GPU is overheating and throttling. Check fans, airflow, repaste if needed.
- **VRel (4)** → Reliability voltage cap. On modern GeForce cards this is the **normal** state during gaming — the boost algorithm won't clock higher because the auto-set voltage is already at the highest safe level. Not a problem by itself.
- **VOp (8)** → Max operating (hardware) voltage reached. Also typically normal under load.
- **Util (16)** → Low utilization, so the GPU stays at low clocks. **Expected at idle/light load.** It is only a concern if it appears while a game should be fully loading the GPU — that points to a CPU/engine bottleneck or a power policy forcing low clocks (e.g. NVIDIA Control Panel set to "Optimal Power"/"Adaptive" instead of "Prefer Maximum Performance", or Windows PCIe Link State Power Management on "Maximum Power Savings").
