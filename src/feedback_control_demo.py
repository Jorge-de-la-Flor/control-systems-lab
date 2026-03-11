"""
Closed-loop feedback control demonstration.

Simulates a simple proportional controller driving a system output
toward a constant target value.
"""

import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    target = 5.0
    value = 0.0

    history: list[float] = []

    for _ in range(80):
        error = target - value

        # Proportional control: u = Kp * e.
        control = 0.4 * error

        value += control
        history.append(value)

    plt.plot(history, label="Response")
    plt.axhline(target, color="r", linestyle="--", label="Target")

    plt.title("Closed-loop feedback control")
    plt.xlabel("Step")
    plt.ylabel("System output")
    plt.legend()

    # plt.show()  # In WSL we don't have UI
    plt.savefig("../assets/feedback_control.png")
