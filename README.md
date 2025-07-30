# 🛡️ Cyber MAS Sim

## Multi Agent System Simulation for CyberSecurity WF

SentinelByte 2025 (DCV)

A lightweight simulation framework for modeling attacker and defender agents in a cybersecurity environment. Built from scratch to support reinforcement learning, automation, and cloud security training scenarios.


## 🚀 Features

- Simulated network with vulnerable nodes
- Attacker and defender agents with pluggable logic
- Logs, patching, and basic interaction tracking
- Designed for future expansion: RL, PettingZoo, AWS/K8s integrations


## 📁 Project Structure

```

cyber-mas-sim/
├── agents/            # Attacker and Defender agents
│   ├── attacker.py
│   └── defender.py
├── core/              # Simulation engine & utilities
│   ├── simulation.py
│   └── utils.py (optional)
├── env/               # Simulated environment (nodes, network)
│   ├── node.py
│   └── network.py (optional)
├── run.py             # Entrypoint to run the simulation
├── requirements.txt   # Python dependencies
|__ README.md

````

---

## 🧪 Quick Start

### 1. Clone and Setup
```bash
git clone https://github.com/SentinelByte/cyberMasSim.git
cd cyberMasSim
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
````

### 2. Run the Simulation

```bash
python run.py
```

---

## ✅ TODO

* [ ] Add lateral movement and network graph
* [ ] Introduce Reinforcement Learning (PettingZoo/Gym)
* [ ] Model AWS or K8s-specific attack/defense behavior
* [ ] Visualization (grid or graph)


## 📜 License

MIT License — free to use and modify.


## 🙋‍♂️ About

Built by SentinelByte. 

Exploring Multi Agent Systems (MAS) for autonomous defense, cloud remediation, and adversarial simulation.

````
gitignore

## Python
__pycache__/
*.pyc
*.pyo
*.pyd
*.log

## Envs
venv/
.env

## IDEs
.vscode/
.idea/
````

---

## 🏷️ GitHub Tags and Topics

Repo Tags:

```
cybersecurity, multi-agent-system, red-team, blue-team, simulation, python, cloud-security, SentinelByte
```
