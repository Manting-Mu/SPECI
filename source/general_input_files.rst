General Input Files
===================

SPECI uses structured input files to define chemical systems for automated speciation analysis. The main input file format is CSV, typically located in the `inputs_template/` directory or provided as examples in the `examples/` folder.

Input File Types
----------------

- **Component Data (`components-data.csv`):**
  - Contains the list of all components (e.g., metals, ligands, solvents) and their relevant properties.
  - **Required columns:**
    - `components` — Unique name/label for each fragment. Fragments should be defined so that no bonds are broken or formed within a fragment. For multidentate ligands, specify each donor atom with `Donor` + ligand name + bonding atom (e.g., `DonorLN2N1`). The code recognizes multidentate ligands if `Donor` is present in the name.
    - `charge` — Net charge of the component, or (for multidentate ligands) the charge contributed by the bonding atom.
    - `connectivity allowed` — List the allowed number of connectivities for the bonding atom with other fragments (e.g., `"0, 1, 2"`). If `0` is included, the component may be omitted from some molecules.
    - `donor atom` — The element type of the bonding atom (e.g., N, O, C).
    - `type` — The role of the component (e.g., metal, ligand). If a ligand is multidentate, type it as `ligand`. Neutral monodentate ligands should also be marked as donor ligands.

- **Structure Files (.ct):**
  - For each component, a ChemDraw `.ct` file is required, showing explicit H atoms.
  - Bonding atoms in ChemDraw must be labeled as `Node` for metals/ligands, and as `Nod1`, `Nod2`, etc. for multidentate donor ligands.

Example: Component Data CSV
---------------------------

.. code-block:: csv

   components,charge,connectivity allowed,donor atom,type
   Mg,2,"0, 1, 2, 3, 4",Mg,metal
   OEt2,0,"0, 1",O,ligand
   R,-1,"0, 1",C,ligand
   DonorLN2N1,-1,"0, 1",N,ligand
   DonorLN2N2,-1,"0, 1, 2",N,ligand

(Your file may contain additional components and columns as needed.)

Tips for Creating Input Files
-----------------------------

- Copy an example CSV from the `inputs_template/` or `examples/` folder.
- Ensure all required columns are filled for each component.
- Check for correct naming, charge, and donor atom specification, especially for multidentate ligands.
- Save all `.ct` structure files with the exact same names as the fragments in the CSV.

Location of Input Files
-----------------------

- Place input files in your working directory or reference them in your scripts/notebooks.
- Example input sets and templates are in the `examples/` and `inputs_template/` folders.

Input Settings
==============

The following **Python variables and functions** control aspects of graph generation. These should be edited directly in the Jupyter notebook (see `SPECI.ipynb`).

Graph Generation Parameters
---------------------------

.. code-block:: python

   charge_specified = 0              # Total charge of the species to generate
   monomers = 2                      # Maximum number of repeats per fragment/component in the species
   donor_M_connection = 6            # Maximum number of connections between metals (M) and donor atoms
   donor_as_bridgeing = False        # Set True if using donor ligand to describe a charged multidentate ligand
   center = ['Mg', 'Na']             # Metal centers for filtering out 3D structures with close metal–atom contacts
   df = pd.read_csv('components-data.csv')   # Path to fragment property CSV file
   user_specified_atomcount_controll = []    # Example: [('component1', 2), ('component2', 1)]
   bonds_not_constructed = [('Na', 'R')]     # Prevents certain bonds from being constructed
   num_cores = 7                     # Number of CPU cores to use (set 7 for an 8-core machine, etc.)
   dummy_atom_needed = ['Mg', 'Li']  # Specify if dummy atoms are needed in the structure

- Adjust these parameters according to your chemical system and computational resources.
- `user_specified_atomcount_controll` lets you limit the number of certain fragments in each generated species.
- `bonds_not_constructed` prevents the program from forming bonds between specific components.


Additional Settings for Advanced Users
======================================

The following **Python variables and functions** control advanced aspects of structure embedding and output. Most are set directly in the Jupyter notebook (see `SPECI.ipynb`).

2D to 3D Structure Embedding Settings
-------------------------------------

You may need to adjust the **atomic distance thresholds** for filtering out poor 3D structures:

.. code-block:: python

   def passes_non_H_threshold(atoms, coords, threshold=1.6):   # Change threshold as needed

.. code-block:: python

   def passes_all_thresholds(atoms, coords, non_H_threshold=1.6, all_atom_threshold=0.9): # Adjust thresholds

- Default thresholds (in Å) are typically sufficient, but you can tighten or loosen them for challenging systems.

XYZ Structure Optimization and Gaussian Input
---------------------------------------------

To optimize 3D structures using quantum chemistry (e.g., Gaussian):

.. code-block:: python

   totla_structure_num = 100     # Total number of structures to model (should be at least 3x number of groups)

.. code-block:: python

   # Custom Gaussian input file generation (example):
   i = 0
   name = 'speciation'
   for index in collected_indices:
       new_comfile = name + str(index) + '.com'
       open(new_comfile, '+a').write('%chk=' + name + str(index) + '.chk' + '\n' +
                                     '%nprocshared=16\n' +
                                     '%mem=32GB\n' +
                                     '#p opt=loose PM7 freq scf=xqc \n' +
                                     '\n speciation study\n' +
                                     '\n-1 1\n')
       with open("speciation" + str(index) + ".xyz", 'r') as f:
           lines = f.readlines()
       for line in lines[2:]:
           open(new_comfile, '+a').write(line)
       open(new_comfile, '+a').write('\n')
       i += 1

- **Note:** Users must adapt these templates to their own cluster/scheduler and level of theory. Advanced computational chemistry experience is required.

Gaussian Output Interpretation & Data Export
--------------------------------------------

.. code-block:: python

   directory_path = "/path/to/your/PM7-log"    # Specify your Gaussian log file directory

.. code-block:: python

   df.to_csv("/path/to/DFT_Energies.csv", index=False)   # Path to save energies/results

- Make sure you update the paths for your own system.

Interacting Ion Pair (IIP) Generation
-------------------------------------

If using the IIP feature for ion pair generation:

- Cation and anion XYZ files must be pre-generated and placed in folders named `cat` and `ani`.

.. code-block:: python

   def random_placement_all(cation, anion, initial_distance=50.0, final_distance=2.5):
       # Adjust final_distance as needed for closest approach

.. code-block:: python

   rotation_angles = [0, 120, 240]   # Customize rotation sampling
   sorted_finals = sorted(all_final_structs, key=lambda x: x[1])[:10]   # Keep top N structures

.. code-block:: python

   # Usage:
   base_dir = '/path/to/IIP/cat2ani2'    # Set your working directory
   generate_combinations(base_dir, cation_count=1, anion_count=1)    # Specify number of cations/anions

- Output IIP XYZs will be saved to the `generated_xyz` folder.

Important Notes
---------------

- Advanced features require **prior experience with computational chemistry software** (e.g., Gaussian).
- Always review and adapt Python scripts and computational job settings for your hardware and chemical system.
- For help and troubleshooting, consult the [GitHub repository](https://github.com/Manting-Mu/OLIGO/issues) or example notebooks.

