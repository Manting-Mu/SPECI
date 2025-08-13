Bimetallic IIP: Example Case Study
==================================

This case study demonstrates how SPECI can be used to generate and explore bimetallic interacting ion pairs (IIPs), with an emphasis on customizing the workflow for complex systems. The folders `common_connection_tables`, `SSIP`, and `IIP` document the complete process, from individual speciation to bimetallic pair assembly.

Overview & Workflow
-------------------

1. **SSIP Generation**  
   The first stage involves generating and optimizing *single-species ion pairs* (SSIPs) for both cations and anions.  
   - All possible coordination environments are enumerated.
   - Filtered, chemically reasonable structures are optimized at the DFT level (see `SSIP` folder for input/output).

2. **Dummy Atom Embedding**  
   In this study, a dummy atom approach was used:
   - *Lithium (Li) atoms* are temporarily introduced to facilitate the embedding and geometry construction around magnesium (Mg) centers.
   - This approach allows for improved sampling of plausible bimetallic geometries before Li is replaced by Mg for the final analysis.

3. **IIP Generation and Selection**  
   Interacting ion pairs (IIPs) are explicitly constructed from the SSIP pool:
   - For this example, only the *highest* and *lowest* coordinated sodium (Na) cations were used to demonstrate the IIP construction process.
   - To **expand the search**, users can simply add the XYZ coordinates of additional cation (or anion) structures of interest into the relevant input folders (`cat`, `ani`) and rerun the IIP workflow.
   - The script will automatically generate new IIPs using all supplied species.

4. **IIP Structure Generation**
   - The filtered, DFT-optimized SSIP cation and anion XYZ files are combined using the IIP search algorithm.
   - The algorithm explores a range of initial placements and orientations, ensuring realistic starting geometries for bimetallic IIPs.
   - The resulting IIP structures are saved as XYZ files in the output directory.

Example Directory Structure
--------------------------

- `common_connection_tables/` — Lookup tables and templates for bond/connectivity enumeration.
- `SSIP/` — Contains all cation and anion single-species structure files, DFT optimization inputs/outputs, and filtered lists.
- `IIP/`
  - `cat/` — Folder containing filtered cation XYZ files (e.g., highest and lowest coordinated Na).
  - `ani/` — Folder containing filtered anion XYZ files.
  - `generated_xyz/` — Output folder where all generated IIP XYZ structures are stored.

Customization & Expansion
------------------------

- **Expanding the IIP Search:**  
  To include more cation/anion combinations, users simply copy their XYZ files into the respective `cat` and `ani` directories and rerun the IIP workflow.  
  The script will handle all valid pairings automatically.

- **Dummy Atom Guidance:**  
  If a dummy atom is needed for better geometry initialization (e.g., Li for Mg), ensure your XYZ and input files are labeled and handled accordingly.  
  Replace the dummy atom with the desired element in final post-processing steps.

- **Advanced Filtering:**  
  Users may wish to optimise and filter candidate SSIPs further at DFT level before IIP generation for efficiency or to focus on physically relevant species.

Best Practices & Tips
---------------------

- **Check structure validity** before and after DFT optimization.
- **Visualize** generated IIP structures to confirm plausible geometries and identify any anomalies.
- **Documentation:**  
  Comment and document any changes you make to the input pool, dummy atom assignments, or IIP search parameters for reproducibility.

References & Further Reading
----------------------------

- See [General Input Files](general_input_files.html) and [General Output Files](general_ouput_files.html) for broader information on file structure and workflow.
- Consult the example scripts and Jupyter notebooks in the main SPECI repository for automation and troubleshooting.


