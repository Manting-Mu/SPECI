# SPECI Automated Speciation Study for Multinuclear Metal Complexes

This repository contains all supporting scripts, notebooks, and structured input files used in the development and application of the **SPECI** and **SPECI-AUTOCOPASI** workflow, designed for automated chemical speciation and microkinetic modeling. It supports a Jupyter notebook-based interface and is tailored for reproducible research and extension by all other chemists.

---


## ⚙️ Conda Environment Setup

To ensure full reproducibility of the environment used to run SPECI:

### 🧪 Step 1: Create the Conda environment

```bash
conda env create -f environment.yml
```

This creates a new environment named `speci-env` (or as defined in the YAML file).

### 🧬 Step 2: Activate it

```bash
conda activate speci-env
```

---

## 🚀 Running the Notebook

Once the environment is activated:

```bash
jupyter notebook
```

Then open and run the appropriate `.ipynb` file in the `notebooks/` folder, or use the `speci/` scripts directly depending on your workflow.

---

## 📦 Dependencies and Features

The environment installs:

- `python >= 3.10`
- `jupyterlab` / `notebook`
- `pandas`, `numpy`, `matplotlib`
- `openbabel` (installed via `conda-forge`, used for molecular handling)

> See `environment.yml` for full dependency list.

### 🧪 Notable Features:
- 📁 Organizes `.ct` input files into clean example folders
- 📊 Converts speciation data into structured `.csv` format
- 🔎 Supports reaction sorting and automatic generation of input for downstream AUTOCOPASI use
- 🧠 Includes IIP (Intermediate Identification Protocol) implementation

---

## 🔒 Licensing and Use of Open Babel

This project uses **[Open Babel](http://openbabel.org/)** for chemical structure parsing and conversion. Open Babel is licensed under the [**GNU General Public License v2 (GPL-2.0)**](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html). The Open Babel original code was not modified, it was called with the command line within this the SPECI script.

### ✔️ What this means for users:
- You are **free to use and modify** this project, including Open Babel functionality, for research and educational purposes.
- If you **redistribute** modified versions of this repository (including scripts that directly use Open Babel), you must also:
- Make your **full source code available**
- Release it under **GPLv2 or a compatible license**
- Include the original Open Babel license text and attribution

---

## 📚 Related Publication

This repository supports the methods presented in:
*Manting Mu et al., 2025 manuscript under preparation*  

If you use this software or any function originated from this software please cite it as below in your work.
Mu, M., Sommer, T., & García-Melchor, M. (2025). SPECI (Version 1.0.0) [Computer software]. https://doi.org/10.5281/zenodo.16823094

---

## 📬 Contact

**Manting Mu**

For questions, bug reports, or suggestions, please [open an issue](https://github.com/Manting-Mu/OLIGO/issues), do not contact directly.

---

## 📄 License

This project is distributed under the terms of the **GNU General Public License v2.0**, in compliance with Open Babel licensing. For full terms, see the [`LICENSE`](https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt) file or [https://www.gnu.org/licenses/old-licenses/gpl-2.0.html](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html).
