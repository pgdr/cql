import setuptools

setuptools.setup(
    name="cql",
    version="0.0.0",
    py_modules=["cql"],
    entry_points={"console_scripts": ["cql=cql:main"]},
    install_requires=["pandas"],
)
