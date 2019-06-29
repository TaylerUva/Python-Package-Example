import setuptools

setuptools.setup(
    name="uva_libs",
    version="1.1.1",
    author="Tayler Uva",
    author_email="None",
    description="A file wrapper",
    license="INTERNAL USE ONLY",
    install_requires=['keyring'],
    packages=setuptools.find_packages()
)
