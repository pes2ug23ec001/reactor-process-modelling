# reactor-process-modelling
Two Python simulations exploring reactor process engineering: a thermodynamic equilibrium calculator validated against published reaction data, and a PID reactor temperature control simulation exploring tuning tradeoffs including integral windup. These are done in reference to the ongoing research into reactor engineering and thermal process control.
**thermodynamics/chem_calc.py — Equilibrium Calculator
**
Computes Gibbs free energy (ΔG = ΔH − TΔS) and the equilibrium constant (K = exp(−ΔG/RT)) for any reversible reaction, given its enthalpy and entropy change. Validated against two real, published reactions — water-gas shift and methanation — confirming the expected Le Chatelier's-principle behavior: equilibrium constant decreases as temperature rises, since both reactions are exothermic.

Prints equilibrium constants at several temperatures and saves a comparison plot showing how reaction favorability shifts with temperature for both reactions.

**control/pid_reactor_sim.py — PID Reactor Temperature Control
**
Models a reactor as a simple thermal system (temperature rises with heat input, loses heat proportionally to how much hotter it is than ambient), then applies a PID controller to drive it to a target setpoint. Runs three different gain configurations side by side to compare tuning tradeoffs.
