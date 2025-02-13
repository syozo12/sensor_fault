from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e."
def get_requirements(file_path:str)->list[str]:
    r=[]
    with open(file_path) as file_obj:
        r=file_obj.readlines()
        r=[req.replace("\n","") for req in r]
    if HYPEN_E_DOT in r:
        r.remove("-e.")
    return r

setup(
    name='fault detection',
    version='0.0.1',
    authors='radha',
    author_mail="radhasvohra05@gmail.com",
    install_requirements=get_requirements("requirements.txt"),
    packages=find_packages()

)