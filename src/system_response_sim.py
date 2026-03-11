"""
Dynamic system step response simulation.

Computes and plots the unit-step response of a first-order system
with time constant equal to 1.
"""

import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    time = np.linspace(0, 10, 100)

    # First-order unit step response: y(t) = 1 - exp(-t).
    response = 1 - np.exp(-time)

    plt.plot(time, response)

    plt.title("Step response of first-order system")
    plt.xlabel("Time")
    plt.ylabel("System output")

    # plt.show()  # In WSL we don't have UI
    plt.savefig("../assets/step_response_simulation.png")
