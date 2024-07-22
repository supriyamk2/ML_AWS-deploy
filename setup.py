from setuptools import find_packages, setup
from typing import List
HYPHON_E = "-e ."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPHON_E in requirements:
            requirements.remove(HYPHON_E)


    return requirements

    




setup(
    name="mlproject",
    version="0.0.1",
    author="Supriya Pillai",
    author_email="mksupriya2@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)

