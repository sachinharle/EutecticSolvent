#my main code file for creating ORCA input files
import os
def create_orca_input(molecule, method, basis_set, charge=0, multiplicity=1, job_type='opt'):
    """
    Create an ORCA input file for a given molecule and computational parameters.

    Parameters:
    molecule (str): The molecular structure in XYZ format.
    method (str): The computational method (e.g., 'B3LYP').
    basis_set (str): The basis set to be used (e.g., '6-31G*').
    charge (int): The total charge of the molecule.
    multiplicity (int): The spin multiplicity of the molecule.
    job_type (str): The type of job to perform (e.g., 'opt', 'freq').

    Returns:
    str: The content of the ORCA input file.
    """
    input_content = f"""! {method} {basis_set} {job_type}
%pal nprocs 4 end
* xyz {charge} {multiplicity}
{molecule}
*
"""
    return input_content
def save_orca_input(file_name, input_content):
    """
    Save the ORCA input content to a file.

    Parameters:
    file_name (str): The name of the file to save the input content.
    input_content (str): The content of the ORCA input file.
    """
    with open(file_name, 'w') as file:
        file.write(input_content)
# Example usage
if __name__ == "__main__":
    molecule_xyz = """O 0.000000 0.000000 0.000000
H 0.000000 0.757000 0.586000
H 0.000000 -0.757000 0.586000"""
    method = "B3LYP"
    basis_set = "6-31G*"
    input_content = create_orca_input(molecule_xyz, method, basis_set)
    save_orca_input("water_opt.inp", input_content)
#my main code file for creating ORCA input files
import os
def create_orca_input(molecule, method, basis_set, charge=0, multiplicity=1, job_type='opt'):
    """
    Create an ORCA input file for a given molecule and computational parameters.

    Parameters:
    molecule (str): The molecular structure in XYZ format.
    method (str): The computational method (e.g., 'B3LYP').
    basis_set (str): The basis set to be used (e.g., '6-31G*').
    charge (int): The total charge of the molecule.
    multiplicity (int): The spin multiplicity of the molecule.
    job_type (str): The type of job to perform (e.g., 'opt', 'freq').

    Returns:
    str: The content of the ORCA input file.
    """
    input_content = f"""! {method} {basis_set} {job_type}
%pal nprocs 4 end
* xyz {charge} {multiplicity}
{molecule}
*
"""
    return input_content
def save_orca_input(file_name, input_content):
    """
    Save the ORCA input content to a file.

    Parameters:
    file_name (str): The name of the file to save the input content.
    input_content (str): The content of the ORCA input file.
    """
    with open(file_name, 'w') as file:
        file.write(input_content)
# Example usage
if __name__ == "__main__":
    molecule_xyz = """O 0.000000 0.000000 0.000000
H 0.000000 0.757000 0.586000
H 0.000000 -0.757000 0.586000"""
    method = "B3LYP"
    basis_set = "6-31G*"
    input_content = create_orca_input(molecule_xyz, method, basis_set)
    save_orca_input("water_opt.inp", input_content) 