import setuptools

setuptools.setup(
    name="An_Online_Store",
    packages=setuptools.find_packages(exclude=["An_Online_Store_tests"]),
    install_requires=[
        "dagster==0.14.19",
        "dagit==0.14.19",
        "pytest",
    ],
)
