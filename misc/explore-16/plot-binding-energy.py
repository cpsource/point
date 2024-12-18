import pandas as pd
import matplotlib.pyplot as plt

# Define ten random elements with approximate nuclear binding energy values (in MeV per nucleon)
elements_data = [
    {"Element": "Hydrogen", "BindingEnergy": 0.0, "GravityInfluence": 0.1},  # Simplified gravity influence scale
    {"Element": "Helium", "BindingEnergy": 7.1, "GravityInfluence": 0.5},
    {"Element": "Sodium", "BindingEnergy": 5.1, "GravityInfluence": 0.9},
    {"Element": "Carbon", "BindingEnergy": 7.7, "GravityInfluence": 1.5},
    {"Element": "Oxygen", "BindingEnergy": 7.6, "GravityInfluence": 1.8},
    {"Element": "Silicon", "BindingEnergy": 8.2, "GravityInfluence": 2.1},
    {"Element": "Iron", "BindingEnergy": 8.8, "GravityInfluence": 3.5},
    {"Element": "Gold", "BindingEnergy": 7.9, "GravityInfluence": 4.5},
    {"Element": "Lead", "BindingEnergy": 7.9, "GravityInfluence": 4.8},
    {"Element": "Uranium", "BindingEnergy": 7.6, "GravityInfluence": 5.2},
    ]
 

# Convert to DataFrame
df = pd.DataFrame(elements_data)

# Display the DataFrame
print("Nuclear Binding Energy and Gravity Influence")
print(df)

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(df["Element"], df["BindingEnergy"], color="blue", alpha=0.7, label="Binding Energy (MeV/nucleon)")
plt.plot(df["Element"], df["GravityInfluence"], color="red", marker="o", label="Gravity Influence (arbitrary scale)")
plt.xlabel("Element")
plt.ylabel("Value")
plt.title("Nuclear Binding Energy vs Gravity Influence")
plt.legend()
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()

