Solvent Coordination: Example Case Study (LiTMP/THF)
====================================================

This case study demonstrates how to use SPECI for exploring the speciation and coordination of lithium tetramethylpiperidide (LiTMP) with tetrahydrofuran (THF) solvent. The files in `CASE1_LiTMP-THF` showcase the input setup, structure enumeration, and energy output typical for solvent coordination chemistry problems.

Directory Overview
------------------

The `CASE1_LiTMP-THF` example includes:

- `components-data.csv` — Describes all system fragments, including lithium, TMP ligand, and THF as a coordinating solvent.
- `ct/` — Contains ChemDraw `.ct` structure files for each fragment.
- `PM7Gibbs_Energies.csv` — Output file summarizing PM7 Gibbs energies for all enumerated species.
- `logfile.rtf` — Execution log for the run.
- Additional folders (e.g., `xyz/`, `com/`) for 3D structure files and quantum chemistry input files if generated.

Input Preparation
-----------------

**1. Edit the `components-data.csv` file:**

This CSV specifies the building blocks for SPECI. For LiTMP/THF, it might look like:

.. code-block:: csv

   components,charge,connectivity allowed,donor atom,type
   TMP,-1,"0, 1, 2",N,ligand
   Li,1,"0, 1, 2, 3, 4",Li,metal
   DonorTHFO1,0,"0, 1",O,ligand
   DonorTHFO1,0,"0, 1",O,ligand

- **TMP** is the tetramethylpiperidide anion.
- **Li** is the metal center.
- **DonorTHFO1** represents THF molecules acting as monodentate donor ligands.
- The number and identity of fragments control the degree of coordination and aggregation SPECI will explore.

**2. Place ChemDraw `.ct` files**  
Ensure that for each component in the CSV, a matching `.ct` file exists in the `ct/` directory (e.g., `TMP.ct`, `Li.ct`, `THF.ct`).

Running the Workflow
--------------------

**3. Run the SPECI workflow:**
- Launch the Jupyter notebook or run your Python workflow script.
- Adjust any relevant advanced settings (see documentation for parameters such as `charge_specified`, `monomers`, or `num_cores`).

**4. Structure Generation:**
- SPECI will enumerate all unique species formed by different possible combinations and connectivities of Li, TMP, and THF.
- 3D coordinates (if generated) will be saved as `.xyz` files in the `xyz/` directory.
- Quantum chemical input files (e.g., for PM7, UFF, or DFT) may be generated in the `com/` directory.

Analyzing Output
----------------

**5. Reviewing Energies:**
- After the calculation, the main result is the `PM7Gibbs_Energies.csv` file, which contains Gibbs free energies for each enumerated structure.

Example excerpt:

.. code-block:: csv

    13_index,13_energy,29_index,29_energy,...
    THF,0.002637,105.0,0.156997,...

- Each pair of columns (`_index`, `_energy`) refers to a particular structure and its calculated energy.
- Use these energies to identify the most stable species and to compare relative stability of different coordination motifs.

**6. Interpreting Results:**
- Lower energy structures are more likely to dominate in solution.
- Differences in THF coordination number, TMP aggregation state, or Li–ligand connectivity will be reflected in the list of enumerated species and their energies.

Tips & Best Practices
---------------------

- **Fragment definition:** The level of detail (e.g., how you split THF or TMP into donors/fragments) affects the range of structures generated.
- **Solvent effects:** THF can be included as an explicit ligand or as part of the environment, depending on your modeling goal.
- **Post-processing:** The energies from PM7 or DFT can be used for further thermodynamic or kinetic modeling (see the `MKM` folder for microkinetic modeling examples, if provided).

References & Further Reading
----------------------------

- See [General Input Files](general_input_files.html) and [General Output Files](general_ouput_files.html) for more information about input and output formats.
- For advanced use, consult the [README](https://github.com/Manting-Mu/OLIGO) and example Jupyter notebooks.


