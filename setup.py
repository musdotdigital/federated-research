import sys
from subprocess import call, check_call

from setuptools import find_packages, setup
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
from setuptools.command.install import install

# Histolab has a dependency that requires options
histolab_dep_commands = [
    sys.executable,  # the python interpreter (needed to install in the right pipenv)
    "-m",
    "pip",
    "install",
    "large-image-source-openslide",
    "--find-links",
    "https://girder.github.io/large_image_wheels",
]


class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        command = call(histolab_dep_commands)
        assert command == 0


class CustomDevelopCommand(develop):
    def run(self):
        develop.run(self)
        command = call(histolab_dep_commands)
        assert command == 0


class CustomEggInfoCommand(egg_info):
    def run(self):
        egg_info.run(self)
        command = check_call(histolab_dep_commands)
        assert command == 0


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="flamby",
    version="0.0.1",
    python_requires=">=3.7.0",
    license="MIT",
    classifiers=[
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        "argparse",
        "numpy",
        "pandas",
        "pre-commit",
        "scikit-learn",
        "scipy",
        "seaborn",
        "setuptools==59.5.0",
        "tensorboard",
        "torch",
        "torchvision",
        "torchaudio",
        "tqdm",
        "umap-learn",
        "opacus",
        "substrafl==0.32.0",
        "wget",
        "matplotlib==3.5.2",
        "inquirer"
    ],
    description="FLamby: A cross-silo Federated Learning Benchmark.",
    long_description=long_description,
    author="FL-datasets team",
    author_email="unknown",
    packages=find_packages(),
    include_package_data=True,
    cmdclass={
        "install": CustomInstallCommand,
        "develop": CustomDevelopCommand,
        "egg_info": CustomEggInfoCommand,
    },
)
