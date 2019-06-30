import setuptools

setuptools.setup(
    name="uva_libs",
    version="2.1.0",
    author="Tayler Uva",
    author_email="None",
    description="A file wrapper",
    license="INTERNAL USE ONLY",
    install_requires=['keyring'],
    packages=setuptools.find_packages()
)
