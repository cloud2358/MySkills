# GPU-Z Skill

这是一个供 AI Agent 使用的 [TechPowerUp GPU-Z](https://www.techpowerup.com/gpuz/) 技能包，用于定位或安装 GPU-Z、导出 GPU 静态硬件信息、定时记录实时传感器数据，以及结合 PerfCap Reason 分析 NVIDIA GPU 的性能瓶颈。

GPU-Z 本质上是 Windows GUI 应用，命令行参数的组合行为并不总是一致。本项目通过 `scripts/` 中的 Python 脚本封装已验证的操作流程，不建议直接拼接 GPU-Z CLI 指令。

## 运行环境

- Windows 10 或 Windows 11
- Python 3.10+
- Windows PowerShell
- `winget`，仅自动下载安装 GPU-Z 时需要

运行 GPU-Z、安装程序或终止提升权限的 GPU-Z 进程时，Windows 可能显示 UAC 管理员确认窗口。

## 项目结构

```text
gpu-z/
├── SKILL.md
├── README.md
├── scripts/
│   ├── find_gpuz.py
│   ├── download_gpuz.py
│   ├── dump_cards.py
│   └── log_sensors.py
├── info/
│   ├── gpu_info.xml
│   └── sensors_info.csv
└── references/
    ├── cli-guide.md
    ├── gui-guide.md
    └── perfcap-codes.md
```

将本 Skill 目录放到 skills 目录下（例如 `~/.claude/skills/gpu-z/` 或 `.cursor/skills/gpu-z/`），Agent 即可发现并使用。

## 查找 GPU-Z

```bash
cd skills/gpu-z
python scripts/find_gpuz.py
```

脚本会检查 `C:\Program Files\GPU-Z\GPU-Z.exe`、`C:\Program Files (x86)\GPU-Z\GPU-Z.exe` 和当前 Skill 目录下的 `GPU-Z.exe`。

## 下载并安装 GPU-Z

仅在 GPU-Z 未找到并且用户明确要求或同意安装时运行：

```bash
cd skills/gpu-z
python scripts/download_gpuz.py
```

脚本通过 `winget` 下载官方 `TechPowerUp.GPU-Z` 包，并使用 GPU-Z 自带的 `-installSilent` 完成安装。

## 导出硬件信息

```bash
cd skills/gpu-z
python scripts/dump_cards.py
```

结果固定写入 `info/gpu_info.xml`，旧文件会被覆盖。该脚本不接受命令行参数，因为 GPU-Z 的 `-dump` 与其他参数组合时可能无法正常工作。

## 记录传感器数据

默认记录 60 秒，并覆盖原有 CSV：

```bash
cd skills/gpu-z
python scripts/log_sensors.py
```

使用 `-t` 或 `--time` 设置 GPU-Z 进程的运行时间：

```bash
cd skills/gpu-z
python scripts/log_sensors.py -t 30
python scripts/log_sensors.py --time 120
```

使用 `-a` 或 `--append` 将新数据追加到已有 CSV，也可以与时间参数组合：

```bash
cd skills/gpu-z
python scripts/log_sensors.py -a
python scripts/log_sensors.py --time 120 --append
```

结果固定写入 `info/sensors_info.csv`。时间参数控制的是 GPU-Z 从启动到终止的总时长，初始化会占用数秒，因此实际传感器采样时间略短；设置过小可能导致文件未生成或没有有效数据。

## 性能分析

分析 GPU 性能时，同时运行 `dump_cards.py` 和 `log_sensors.py`，然后读取 `info/gpu_info.xml` 与 `info/sensors_info.csv`。对于包含 PerfCap Reason 的 NVIDIA 传感器日志，可参考 [`references/perfcap-codes.md`](references/perfcap-codes.md)，并结合负载、频率、温度、功耗和时间戳判断限制因素。

## 参考文档

- [`references/cli-guide.md`](references/cli-guide.md)：GPU-Z 命令行参数及行为，仅在需要深入了解 CLI 时阅读。
- [`references/gui-guide.md`](references/gui-guide.md)：GPU-Z 窗口、标签页、字段、传感器、验证和设置，仅在需要深入了解 GUI 时阅读。
- [`references/perfcap-codes.md`](references/perfcap-codes.md)：NVIDIA PerfCap Reason 位值、含义与分析方法。

## 许可与来源

GPU-Z 由 [TechPowerUp](https://www.techpowerup.com/) 开发并保留其版权。本项目仅包含 Agent Skill、辅助脚本和使用文档，不包含 GPU-Z 程序本体。
