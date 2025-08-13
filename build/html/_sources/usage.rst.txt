
User Configuration Guide
========================

This guide explains how to modify key parameters in both the SPECI notebook and the `auto-MKM.py` script.

SPECI (Primary Tool)
--------------------

**Key Parameters to Modify:**

- **Input Fragment Property Table**:  
  Edit the filename/path in the variable (typically `components-data.csv`).  
  Make sure the file contains required molecular fragment information.

- **User Inputs for Construction**:
  - Number of monomers
  - Charge states to include
  - Dummy atoms or ghost atoms for reactivity
  - Core-specific customizations
  - Pathway pruning or filtering options

- **Manual Filtering Steps**:
  SPECI includes user-directed steps where you must manually accept or reject bonding combinations or structures.

- **Saving Results**:
  Some cells involve saving CSV files or visual structures — filenames can be modified by changing the output string.

- **Execution**:
  Run each notebook cell in sequence. Comments near user input cells explain what to edit.

auto-MKM (Optional Script)
--------------------------

**Editable Parameters in `auto-MKM.py`:**

- **CSV Input File**:  
  Edit `file_path` to point to your list of elementary reactions.

- **Initial Concentration of Species (e.g., THF)**:  
  Modify `set_species('THF', initial_concentration=1000)`.

- **Simulation Duration**:  
  Edit `run_time_course(duration=3600)` to set time (in seconds).

- **Rate Constant**:  
  Change `k1 = 1.34e+09` to alter the base rate constant.

- **Output Files**:
  - COPASI model: `save_model("output_model.cps")`
  - Plot: `plt.savefig("output.png")`
  - CSV results: `result.to_csv("results.csv")`

Input CSV Format (Required)
---------------------------
The CSV used by `auto-MKM.py` must include:

- `Reactants`
- `Products`
- `dE (kcal/mol)`

The script computes equilibrium constants and reverse rate constants automatically.

