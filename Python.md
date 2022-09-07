## Managing environments with Conda
- Adding new environment with required packages<br>
  ` conda create --name <environment name> <package names> `
- Activating an environment <br>
` conda activate <environment name>`
- Deactivating an environment (leaving) <br>
  ` conda deactivate `
- Listing all of your environments <br>
  ` conda env list `
- Removing and environment <br>
  ` conda env remove --name <environment name> `
- Conda package manager information <br>
  detailed: ` conda info `<br>
  version: ` conda --version `
- Listing all packaged in the current Conda environment <br>
  ` conda list `
- Searching for all the available versions of a certain package (e.g, seaborn)<br>
  ` conda search <package name> `
- Installing a package (e.g, seaborn) <br>
  ` conda install <package name> `<br>
  ` conda install <package name=version> `
- Create an environment using clone (copying other env)L
  `conda create --name <new env name> --clone <env name>`
