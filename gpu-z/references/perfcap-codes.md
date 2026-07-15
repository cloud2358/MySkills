# NVIDIA PerfCap Reason Codes

`PerfCap Reason` is an NVIDIA-specific GPU-Z sensor that reports why the GPU's boost logic is not selecting a higher performance point. GPU-Z represents the reason as a numeric bitmask in sensor data and as short labels in the GUI. The sensor may be absent on unsupported GPUs.

Multiple reasons can be active simultaneously, in which case their bit values combine. For example, `5` represents `1` (Pwr) plus `4` (VRel).

| Value | Label | Meaning |
|-------|-------|---------|
| 0 | None | None of these PerfCap reasons is currently active |
| 1 | Pwr | Performance is limited by the configured power limit |
| 2 | Thrm | Performance is limited by a temperature threshold |
| 4 | VRel | The voltage-frequency curve is limited by the reliability voltage |
| 8 | VOp | Performance is limited by the maximum operating voltage |
| 16 | Util / Idle | Workload utilization is too low to request a higher performance state |

Combined examples include `3` = Pwr + Thrm, `5` = Pwr + VRel, `6` = Thrm + VRel, and `20` = VRel + Util.

## Interpreting Results

Interpret PerfCap values together with GPU load, clocks, temperature, power, workload behavior, and timestamps:

- **Pwr (1)** — reaching the configured power target is common under sustained GPU load and does not by itself indicate a fault. Unexpectedly low clocks or performance at the same time can justify checking the card's power target, power delivery, workload, and cooling.
- **Thrm (2)** — the GPU has reached a thermal policy threshold. Compare the sustained temperature and clock behavior with the vendor's specifications, then inspect cooling, airflow, fan operation, and thermal contact if performance is reduced.
- **VRel (4)** — the current voltage-frequency curve does not permit a higher boost point within its reliability limit. This is a common boost state on many GeForce GPUs and is not a fault by itself.
- **VOp (8)** — the GPU has reached its maximum operating-voltage policy. This can occur during normal boost behavior and should be evaluated with clocks, load, power, and observed performance.
- **Util / Idle (16)** — the workload is not requesting enough GPU work for a higher performance state. During an unexpectedly slow GPU-heavy workload, possible contributors include a frame cap, VSync, CPU or engine limits, intermittent workload demand, or a power-management policy.

Changing power, voltage, clock, or thermal limits affects stability, power consumption, heat, and hardware safety. PerfCap values alone are not sufficient justification for changing those limits.

## Analysis Workflow

1. Locate the time range where the performance problem occurred in `info/sensors_info.csv`.
2. Compare `PerfCap Reason` with GPU load, clocks, temperature, power, and voltage over the same timestamps.
3. Decompose combined numeric values into the bit values above.
4. Look for sustained patterns that coincide with reduced clocks or observed performance rather than treating an isolated PerfCap value as a fault.
