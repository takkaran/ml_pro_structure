from setuptools import find_packages, setup
# from typing import List

HYPHEN_E_DOT = '-e .'

# def get_requirements(filepath: str) -> List[str]:
def get_requirements(filepath):
    '''This function will return the list of requirements'''
    print(filepath)
    requirements = []
    with open(filepath) as file_obj:
        requirement = file_obj.readlines() 
        requirements = [req.strip() for req in requirement]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Karan',
    author_email='takkaran987@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
