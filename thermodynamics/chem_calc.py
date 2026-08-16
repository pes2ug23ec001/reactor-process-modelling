import numpy as np

R = 8.314 

def equilibrium_analysis(dH, dS, T):
    
    dG = dH - T * dS
    K = np.exp(-dG / (R * T))
    return dG, K


dH_test = -41000  
dS_test = -42.0     
T_test = 500        

dG, K = equilibrium_analysis(dH_test, dS_test, T_test)
print(f"At T={T_test}K: dG = {dG:.1f} J/mol, K = {K:.4f}")

# Checking against published water-gas shift reaction data
# CO + H2O <-> CO2 + H2
dH_wgs = -41000   # J/mol
dS_wgs = -42.0    # J/mol/K

print("\n--- Water-Gas Shift Reaction: CO + H2O <-> CO2 + H2 ---")
for T in [500, 800, 1000]:
    dG, K = equilibrium_analysis(dH_wgs, dS_wgs, T)
    print(f"T={T}K:  dG = {dG:8.1f} J/mol   K = {K:10.4f}")
import matplotlib.pyplot as plt

T_range = np.linspace(400, 1200, 100)
K_values = [equilibrium_analysis(dH_wgs, dS_wgs, T)[1] for T in T_range]
# Second reaction for comparison: Methanation
# CO + 3H2 <-> CH4 + H2O
dH_methanation = -206000   # J/mol
dS_methanation = -214.0    # J/mol/K

print("\n--- Methanation: CO + 3H2 <-> CH4 + H2O ---")
for T in [500, 800, 1000]:
    dG, K = equilibrium_analysis(dH_methanation, dS_methanation, T)
    print(f"T={T}K:  dG = {dG:8.1f} J/mol   K = {K:10.4e}")


K_wgs = [equilibrium_analysis(dH_wgs, dS_wgs, T)[1] for T in T_range]
K_methanation = [equilibrium_analysis(dH_methanation, dS_methanation, T)[1] for T in T_range]

plt.figure(figsize=(8, 5))
plt.plot(T_range, K_wgs, linewidth=2, label="Water-Gas Shift: CO + H2O <-> CO2 + H2")
plt.plot(T_range, K_methanation, linewidth=2, label="Methanation: CO + 3H2 <-> CH4 + H2O")
plt.yscale('log')
plt.xlabel("Temperature (K)")
plt.ylabel("Equilibrium Constant, K (log scale)")
plt.title("Equilibrium Constant vs Temperature — Reaction Comparison")
plt.legend()
plt.grid(True, which="both", alpha=0.3)
plt.savefig("equilibrium_comparison.png", dpi=150)
plt.show()
print("Plot saved as equilibrium_comparison.png")

plt.figure(figsize=(8, 5))
plt.plot(T_range, K_values, linewidth=2)
plt.yscale('log')   # K spans orders of magnitude, log scale makes the trend readable
plt.xlabel("Temperature (K)")
plt.ylabel("Equilibrium Constant, K (log scale)")
plt.title("Water-Gas Shift Reaction: Equilibrium Constant vs Temperature")
plt.grid(True, which="both", alpha=0.3)
plt.savefig("equilibrium_vs_temp.png", dpi=150)
plt.show()
print("Plot saved as equilibrium_vs_temp.png")
