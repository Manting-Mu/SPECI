import pandas as pd
import numpy as np
from basico import *
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "elementary_reactions.csv"
df = pd.read_csv(file_path)

# Calculate K using the formula: K = EXP(-(ΔE * 4184) / (298.15 * 8.314))
df['K'] = np.exp(-(df['dE (kcal/mol)'] * 4184) / (298.15 * 8.314))

# Save the updated file
df.to_csv(file_path, index=False)
print("K column added and file saved.")

# Reload (optional but consistent)
df = pd.read_csv(file_path)

# Define k1 constant
k1 = 1.34e+09

# Calculate k2
df['k2'] = k1 / df['K']

# Save the updated file
df.to_csv(file_path, index=False)
print("k2 column added and file saved.")

# Convert to nested list
elementary_reactions = df[['Reactants', 'Products', 'dE (kcal/mol)', 'K', 'k2']].values.tolist()

# Helper to modify the reaction formula
def modify_reaction_formula(formula):
    tokens = formula.split(' ')
    modified_tokens = []
    for token in tokens:
        if all(part.isdigit() for part in token.split('+')):
            modified_tokens.append('S' + token)
        else:
            modified_tokens.append(token)
    return ' '.join(modified_tokens)

# Create model
new_model(name='auto-MKM')

for i, reaction in enumerate(elementary_reactions, start=1):
    reactants = reaction[0]
    products = reaction[1]
    k2_val = reaction[4]

    raw_formula = f"{reactants} = {products}"
    reaction_formula = modify_reaction_formula(raw_formula)

    print(reaction_formula)

    reaction_id = f"r{i}"
    add_reaction(reaction_id, reaction_formula)

    set_reaction_parameters(f"({reaction_id}).k1", value=k1)
    set_reaction_parameters(f"({reaction_id}).k2", value=k2_val)

#print(get_reaction_parameters('k2'))


set_species('THF', initial_concentration=1000)

# Save model
save_model('auto-MKM.cps')
print("Model saved as 'auto-MKM.cps'")

# Run simulation
result = run_time_course(duration=3600)

# Plot results
ax = result.plot()
ax.set_ylabel('Concentrations')
plt.tight_layout()
plt.savefig('concentration_plot.pdf')
print("Plot saved as 'concentration_plot.pdf'")

# Save result as CSV
result.to_csv('concentration_results.csv', index=False)
print("Simulation results saved as 'concentration_results.csv'")

