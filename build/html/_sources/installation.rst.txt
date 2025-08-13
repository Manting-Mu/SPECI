Installation
============

SPECI is distributed as an open-source Python toolkit. The recommended way to install and run SPECI is via the Conda environment provided in this repository. This ensures that all required dependencies are installed and your setup is fully reproducible.

Setting Up Your Environment
---------------------------

1. **Install Conda (if not already installed)**

   Download and install [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) for your operating system.

2. **Clone the SPECI repository**

   Open a terminal and run:

   .. code-block:: bash

      git clone https://github.com/Manting-Mu/OLIGO.git
      cd OLIGO

3. **Create the SPECI environment**

   Use the provided `environment.yml` file to set up a new Conda environment with all necessary dependencies:

   .. code-block:: bash

      conda env create -f environment.yml

4. **Activate the environment**

   .. code-block:: bash

      conda activate speci-env

   (The environment name may differ if you change it in the `environment.yml` file.)

5. **Launch Jupyter Notebook**

   .. code-block:: bash

      jupyter notebook

   Open the SPECI notebooks (e.g., `SPECI.ipynb`) or use the scripts in the `speci/` folder as needed.

Dependencies
------------

Key dependencies installed include:

- Python (>= 3.10)
- JupyterLab / Notebook
- pandas, numpy, matplotlib
- openbabel (via `conda-forge`)

Refer to the `environment.yml` file for a complete, up-to-date list.

Troubleshooting
---------------

If you encounter any issues with installation, please open an issue on the [GitHub repository](https://github.com/Manting-Mu/OLIGO/issues).

