from setuptools import setup,find_packages

setup(
    name="mi_conversor",
    version="1.0",
    description="Libreria sencilla de conversión",
    author="Denis Lucian Morar Ochis",
    package_dir={"":"src"},
    packages=find_packages(where='src'),
    python_requires=">=3.7"
    
)