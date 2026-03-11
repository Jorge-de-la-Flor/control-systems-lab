"""
PID controller simulation.

Regulates a simple first-order system toward a target value using a
discrete-time PID controller.
"""

import numpy as np
import matplotlib.pyplot as plt


class PIDController:
    """Discrete-time PID controller.

    Computes a control signal based on the proportional, integral, and
    derivative of the error between a setpoint and a measurement.
    """

    def __init__(self, kp: float, ki: float, kd: float) -> None:
        """Initialize PID controller gains and state.

        Args:
            kp: Proportional gain.
            ki: Integral gain.
            kd: Derivative gain.
        """
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.integral = 0.0
        self.prev_error = 0.0

    def update(self, setpoint: float, measurement: float) -> float:
        """Compute the PID control output for the current measurement.

        Args:
            setpoint: Desired target value.
            measurement: Current measured value of the system.

        Returns:
            float: Control signal to be applied to the system.
        """
        error = setpoint - measurement

        self.integral += error
        derivative = error - self.prev_error

        output = (
            self.kp * error
            + self.ki * self.integral
            + self.kd * derivative
        )

        self.prev_error = error

        return output


if __name__ == "__main__":
    pid = PIDController(0.6, 0.1, 0.05)

    setpoint = 10.0
    value = 0.0

    history: list[float] = []

    for _ in range(100):
        control = pid.update(setpoint, value)

        # Simple first-order system integrator.
        value += control * 0.1
        history.append(value)

    plt.plot(history, label="Response")
    plt.axhline(setpoint, color="r", linestyle="--", label="Setpoint")
    plt.title("PID control response")
    plt.legend()
    # plt.show()  # In WSL we don't have UI
    plt.savefig("../assets/pid_controller.png")
