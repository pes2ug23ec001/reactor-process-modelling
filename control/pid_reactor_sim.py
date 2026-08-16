import numpy as np
import matplotlib.pyplot as plt

#example parameters
C = 500.0
k_loss = 2.0
T_ambient = 25.0
dt = 1.0
steps = 2000
T_setpoint = 80.0

def reactor_step(T, Q_in, dt):
    Q_loss = k_loss * (T - T_ambient)
    dT = (Q_in - Q_loss) / C * dt
    return T + dT

def run_pid_sim(Kp, Ki, Kd):
    T = T_ambient
    integral = 0.0
    prev_error = T_setpoint - T
    temps = []

    for i in range(steps):
        error = T_setpoint - T
        integral += error * dt
        derivative = (error - prev_error) / dt

        Q_in = Kp * error + Ki * integral + Kd * derivative
        Q_in = max(0, Q_in)

        T = reactor_step(T, Q_in, dt)
        temps.append(T)
        prev_error = error

    return np.array(temps)

def analyze_response(temps):
    steady_state_error = T_setpoint - temps[-1]
    peak = np.max(temps)
    overshoot_pct = ((peak - T_setpoint) / (T_setpoint - T_ambient)) * 100
    tolerance = 0.02 * (T_setpoint - T_ambient)
    settled_index = None
    for i in range(len(temps)):
        if np.all(np.abs(temps[i:] - T_setpoint) <= tolerance):
            settled_index = i
            break
    settling_time = settled_index * dt if settled_index else None
    return steady_state_error, overshoot_pct, settling_time

# Three tuning scenarios
gain_sets = {
    "Aggressive (Kp=15, Ki=0.5, Kd=5)":   (15.0, 0.5, 5.0),
    "Heavily Damped (Kp=15, Ki=0.5, Kd=20)": (15.0, 0.5, 20.0),
    "Gentle (Kp=8, Ki=0.3, Kd=5)":        (8.0, 0.3, 5.0),
}

plt.figure(figsize=(9, 6))
for label, (Kp, Ki, Kd) in gain_sets.items():
    temps = run_pid_sim(Kp, Ki, Kd)
    sse, overshoot, settling = analyze_response(temps)
    print(f"{label}")
    print(f"  Steady-state error: {sse:.3f} C | Overshoot: {overshoot:.2f}% | Settling time: {settling} s\n")
    plt.plot(temps, label=label)

plt.axhline(T_setpoint, color='black', linestyle='--', label="Setpoint", alpha=0.6)
plt.xlabel("Time (s)")
plt.ylabel("Temperature (C)")
plt.title("PID Tuning Comparison — Reactor Temperature Response")
plt.legend()
plt.grid(alpha=0.3)
plt.savefig("pid_tuning_comparison.png", dpi=150)
plt.show()
