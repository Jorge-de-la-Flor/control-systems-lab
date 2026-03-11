English | [Español](README.es.md)

# Control Systems Lab

Minimal experiments illustrating feedback control and system dynamics in control systems.

This repository explores simple simulations of control system behaviour commonly encountered in robotics, automation, and cyber-physical systems.

The examples demonstrate how feedback control mechanisms can regulate system behaviour and maintain stability in dynamic environments.

## Contents

The `src/` directory contains three minimal experiments:

* `pid_controller_sim.py`

  Implements a simple proportional–integral–derivative (PID) controller regulating a simulated system.

* `system_response_sim.py`

  Demonstrates the step response of a simple dynamic system.

* `feedback_control_demo.py`

  Simulates closed-loop feedback control regulating a system toward a target value.

## Purpose

These experiments illustrate engineering concepts relevant to:

* control systems engineering
* feedback control
* robotics control architectures
* cyber-physical systems

## Motivation

Control systems are fundamental to robotics, automation, and mechatronic systems.

Most real-world machines rely on feedback control mechanisms to regulate motion, maintain stability, and respond to disturbances.

Understanding how dynamic systems behave under feedback control is essential for designing reliable cyber-physical systems.

## Method

The repository implements simplified simulations of control system behaviour.

The experiments include:

* PID control for regulating system output
* dynamic system response to step inputs
* closed-loop feedback control

These implementations are intentionally minimal and focus on illustrating the conceptual behaviour of feedback control systems rather than full industrial control implementations.

## Running the examples

Clone the repository and run any of the scripts:

```bash
git clone https://github.com/Jorge-de-la-Flor/control-systems-lab
cd control-systems-lab
python src/pid_controller_sim.py
```

Each script simulates system behaviour and prints the resulting control process in the console.

## Project tree

```bash
control-systems-lab
├─ .python-version
├─ LICENSE
├─ README.es.md
├─ README.md
├─ pyproject.toml
├─ src
│  ├─ feedback_control_demo.py
│  ├─ pid_controller_sim.py
│  └─ system_response_sim.py
└─ uv.lock
```

## Requirements

The examples use:

* Python 3.12+
* NumPy
* Matplotlib

## Installation

Install the required dependencies:

* using `pip`

```bash
pip install numpy matplotlib
```

* using `uv`

```bash
uv add numpy matplotlib
```

## References

* Åström, K. J., & Murray, R. M. (2008).
  *Feedback Systems.*

* Ogata, K. (2010).
  *Modern Control Engineering.*
