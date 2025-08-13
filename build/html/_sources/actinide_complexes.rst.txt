Actinide Complexes: Example Case Study
======================================

This case study demonstrates how to use SPECI for speciation analysis of actinide complexes, specifically a uranium–tert-butoxide system. The example follows the workflow in the `CASE2_UOtbu` folder and illustrates the use of input files, structure generation, and output analysis.

Directory Overview
------------------

The example folder (`CASE2_UOtbu`) contains:

- `components-data.csv` — Main input describing the fragments in the system.
- `ct/` — ChemDraw structure files for each component (in `.ct` format).
- `xyz/` — Generated 3D structures for all enumerated species (in `.xyz` format).
- `com/` — Gaussian input files for quantum chemical optimization of selected structures.
- `atom_energy_index_combined_output.csv` — Parsed energy output file summarizing computed energies for each structure.
- `logfile.rtf` — Execution log and summary.
- Additional `.ct` files for each fragment in the root folder.

Input Preparation
-----------------

**1. Edit the `components-data.csv` file:**

This CSV specifies the building blocks (fragments), their charge, bonding atoms, and roles. For the uranium–tert-butoxide case, the file looks like:

.. code-block:: csv

    components,charge,connectivity allowed,donor atom,type
    OtBu,0,"0, 1, 2, 3",O,ligand
    U,0,"0, 4",U,metal
    OtBu,0,"0, 1, 2, 3",O,ligand

**2. Place ChemDraw `.ct` files**  
Ensure all fragments listed in the CSV have a matching `.ct` file, stored in `ct/` and/or the root folder (e.g., `U.ct`, `OtBu.ct`).

Running the Workflow
--------------------

**3. Run the SPECI workflow using your Jupyter notebook or Python script:**  
Adjust your advanced settings (see the documentation for options like `charge_specified`, `monomers`, etc.) as appropriate for your system.

**4. Structure Generation:**  
SPECI will enumerate all possible complexes based on your input, generating `.xyz` files for each unique species in the `xyz/` directory.  
- Each file (e.g., `speciation11.xyz`) contains atomic coordinates in standard XYZ format and can be visualized with tools like Avogadro or Jmol.

**5. Preparing for Quantum Chemical Optimization:**  
For each selected structure, SPECI automatically generates a Gaussian input file (e.g., `speciation2.com`) in the `com/` directory, including resource directives and geometry.

Example `.com` file excerpt:

.. code-block:: none

    %chk=speciation2.chk
    %nprocshared=16
    %mem=32GB
    #p opt=loose PM7 scf=xqc 

     speciation study

    -1 1
    O         -0.13084        1.40090        0.09222
    C          0.45868        2.66483        0.40627
    ...

**Note:** Edit the Gaussian input as needed for your cluster, memory, or computational method.

Analyzing Output
----------------

**6. Viewing 3D Structures:**  
Open any `.xyz` file in the `xyz/` folder to inspect the generated actinide complex geometries.

**7. Reviewing Energies and Results:**  
After quantum calculations and parsing, SPECI outputs `atom_energy_index_combined_output.csv`, containing energy values and associated structure indices. This allows rapid ranking and comparison of possible complexes.

Example excerpt:

.. code-block:: csv

    85_energy,85_index,114_energy,114_index,...
    524.68,0,1173.75,1,...

Each column pair gives the computed energy for a structure and its index. Use this file to identify the most stable complexes.

Tips & Best Practices
---------------------

- **Fragment matching:** Names in your CSV and `.ct` files must match exactly.
- **Visualization:** Inspect `.xyz` files to verify bonding and coordination.
- **Computation:** Adjust Gaussian settings for your hardware and use appropriate quantum chemical methods.
- **Result analysis:** Use the energy CSV to guide further kinetic or thermodynamic modeling.

References & Further Reading
----------------------------

- See the [General Input Files](general_input_files.html) and [General Output Files](general_ouput_files.html) documentation for more information about file formats.
- For troubleshooting or more complex systems (e.g., polynuclear actinide clusters), consult the SPECI [README](https://github.com/Manting-Mu/OLIGO) and example notebooks.


