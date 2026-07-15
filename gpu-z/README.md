# GPU-Z Skill

一个供 AI Agent 使用的 [GPU-Z](https://www.techpowerup.com/gpuz/) 教程和技能包（Skill）。它教会 Agent 通过命令行或图形界面驱动 GPU-Z，用于**采集 GPU 硬件规格、监控实时传感器数据、诊断 GPU 性能瓶颈**。

## 目录结构

```
gpu-z/
├── SKILL.md                    # 技能入口：简介、下载、使用时机分流
├── README.md                   # 本文件
├── scripts/
│   ├── find_gpuz.py            # 定位 GPU-Z
│   ├── download_gpuz.py        # 下载并安装 GPU-Z
│   ├── dump_cards.py           # 导出硬件规格 XML
│   └── log_sensors.py          # 定时记录传感器 CSV
├── info/
│   ├── gpu_info.xml            # 静态硬件规格
│   └── sensors_info.csv        # 实时传感器数据
└── references/
    ├── cli-guide.md            # 命令行指南（默认路径）
    ├── gui-guide.md            # 图形界面指南（4 个 Tab + 设置页）
    └── perfcap-codes.md        # PerfCap Reason 位掩码含义与解读
```

## 安装

```bash
python scripts/find_gpuz.py
python scripts/download_gpuz.py
```

也可从官方页面下载最新 **Standard Version**：<https://www.techpowerup.com/download/techpowerup-gpu-z/>，将 `GPU-Z.exe` 放到 `C:\Program Files\GPU-Z\` 或本 skill 目录下。

将本 Skill 目录放到你的 skills 目录下（例如 `~/.claude/skills/gpu-z/` 或 `.cursor/skills/gpu-z/`），Agent 即可发现并使用。

### 脚本（推荐）

```bash
python scripts/dump_cards.py              # → info/gpu_info.xml
python scripts/log_sensors.py             # → info/sensors_info.csv（默认 60 秒）
python scripts/log_sensors.py --time 120  # 记录 120 秒
```

### 命令行

详见 [`references/cli-guide.md`](references/cli-guide.md)。适用于：

- 导出**静态硬件规格**（型号、BIOS/驱动版本、显存、PCIe 链路）为 XML；
- 记录**实时传感器数据**（频率、温度、负载、功耗）；
- 通过采集传感器日志诊断 GPU 瓶颈 / 降频。

### 图形界面

详见 [`references/gui-guide.md`](references/gui-guide.md)。适用于：

- 解读图形界面中各种参数的含义；
- 引导用户学习，了解使用GPU-Z

## 许可与来源

GPU-Z 由 [TechPowerUp](https://www.techpowerup.com/) 开发并保留其版权，本 Skill 仅为使用说明文档，不包含 GPU-Z 程序本体。
