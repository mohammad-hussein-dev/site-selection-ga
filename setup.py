from setuptools import setup, find_packages

setup(
    name="site-selection-ga",
    version="0.1.0",
    description="Optimal school site selection using Genetic Algorithm",
    author="Mohammad Hussein",
    author_email="king.mohamd.09876@gmail.com",
    url="https://github.com/mohammad-hussein-dev/site-selection-ga",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "deap>=1.4.0",
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
    ],
    python_requires=">=3.8",
    license="MIT",
)
