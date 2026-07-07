# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] - 2026-07-07

### Added
- Initial release of site-selection-ga
- Genetic Algorithm implementation using DEAP library
- Custom fitness function with three optimization criteria:
  - Population coverage (maximize)
  - Distance to facilities (minimize)
  - Spatial distribution (maximize)
- Visualization module with matplotlib (2D scatter plot)
- Bilingual comments and output (Persian/English)
- Unit tests with pytest (5 tests, 97% coverage)
- CI/CD pipeline with GitHub Actions
- Codecov integration for coverage reporting
- Pre-commit hooks for code quality (Black, Ruff, MyPy)
- Comprehensive README with badges and documentation
- MIT License
- Modular project structure (src/, tests/, scripts/)

### Technical Details
- Python 3.8+ compatibility
- DEAP 1.4.0+ for evolutionary algorithms
- NumPy 1.24.0+ for numerical operations
- Matplotlib 3.7.0+ for plotting
- GitHub Actions matrix testing (Python 3.9, 3.10, 3.11)
- Codecov coverage reporting

---

## [Unreleased]

### Planned
- PSO (Particle Swarm Optimization) implementation
- Real-world dataset support
- Interactive web dashboard with Streamlit
- Performance benchmarks
- Documentation with MkDocs
