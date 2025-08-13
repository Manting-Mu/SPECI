General Output Files
====================

SPECI generates a range of output files throughout the speciation, graph enumeration, structure generation, and microkinetic modeling workflow. These outputs allow users to analyze the predicted speciation, view generated structures, and prepare for further computational modeling.

Output File Types
-----------------

1. **Speciation Summary CSV Files**
   - Main results file summarizing all generated species, their formulas, abundances, charges, and calculated energies.
   - Example output file: ``species_summary.csv``
   - **Typical columns:**
     - `species` — Name or formula of the species (e.g., `[UO2(L1)2(NO3)2]`)
     - `abundance` — Relative or absolute abundance predicted
     - `energy` — Calculated energy (e.g., from DFT or semi-empirical method)
     - `charge` — Net charge
     - Additional information such as number of atoms/fragments, or SMILES strings may be included.

2. **Generated Structure Files**
   - For each enumerated species, 3D Cartesian coordinate files are created (XYZ format), typically named after the species.
   - Example: ``speciation42.xyz``
   - These files store the atomic coordinates and can be visualized using molecular visualization software (e.g., Jmol, Avogadro).

3. **Structure Optimization Input/Output**
   - If quantum chemical optimizations are performed, SPECI will generate:
     - **Gaussian input files** (``.com``): Files ready to be submitted to Gaussian or similar programs for geometry optimization and frequency analysis.
     - **Gaussian output/log files** (``.log``): Results of the quantum chemical calculations, containing optimized energies, frequencies, and thermodynamic data.
   - The script supports automated parsing of these log files to extract Gibbs free energies and other properties.

4. **Energy Data CSV Files**
   - After parsing the quantum chemistry outputs, SPECI generates CSV files summarizing the calculated energies for each species.
   - Example: ``DFT_Energies.csv``
   - **Columns:**
     - `species` — Name or index of the species
     - `Gibbs_energy` — Gibbs free energy (extracted from frequency calculation)
     - `other thermochemical data` — May include enthalpy, entropy, etc.

5. **Microkinetic Modeling Output**
   - If using the automated microkinetic modeling features (e.g., with AUTOCOPASI), SPECI generates:
     - **Reaction network files** — List of all generated reactions with stoichiometry and predicted rate constants.
     - **Simulation input files** — Input for downstream kinetic modeling software.
   - These are typically stored as CSV or TXT files.

6. **IIP (Interacting Ion Pair) Generation Output**
   - When using the IIP protocol, SPECI outputs new XYZ files for each generated ion pair combination.
   - Results are stored in the ``generated_xyz`` folder within your working directory.

Output File Locations
---------------------

- By default, output files are written to the same directory as your script or notebook, or to subfolders such as `outputs/`, `examples/`, or `generated_xyz/`.
- File naming conventions are consistent and based on species name or index (e.g., ``speciation1.xyz``, ``speciation1.com``, etc.).
- Gaussian input/output files and parsed energy CSVs are typically kept together for ease of analysis.

Interpreting Output Files
--------------------------

- **Species summary CSVs**: High-abundance species are the most likely/thermodynamically favorable under your input conditions.
- **3D structures**: Visualize XYZ files with molecular viewers to check geometry and binding modes.
- **Gaussian/computed energy data**: Use energy CSVs to compare stabilities or for further kinetic modeling.
- **Microkinetic outputs**: Import reaction network and simulation input files into kinetic modeling programs (e.g., AUTOCOPASI) for dynamic simulations.
- **IIP outputs**: Generated XYZs represent different spatial arrangements and distances of cation-anion pairs.

Typical Workflow Example
------------------------

1. Run SPECI to generate ``species_summary.csv`` and ``speciationXX.xyz`` files.
2. (Optional) Optimize selected XYZ files with Gaussian, producing ``.com`` and ``.log`` files.
3. Parse Gaussian logs to extract Gibbs energies, save to ``DFT_Energies.csv``.
4. Use outputs as input for downstream kinetic modeling or further analysis.

Troubleshooting and Tips
------------------------

- Always check that all expected files are generated—missing output often means an error occurred in structure generation or computation.
- File paths and naming conventions are customizable; adjust scripts as needed for your own folder structure.
- For more advanced automation or integration with other programs, adapt the output parsing scripts provided in SPECI.

For more details and example outputs, refer to the ``examples/`` folder or the SPECI Jupyter notebook (``SPECI.ipynb``).


