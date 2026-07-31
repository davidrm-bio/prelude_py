# Prelude_py

[![Tests][badge-tests]][tests]
[![Coverage][badge-coverage]][codecoverage]
[![Issues][badge-issues]][issue tracker]
[![Stars][badge-stars]](https://github.com/davidrm-bio/DOTools_py/stargazers)

[badge-tests]: https://img.shields.io/github/actions/workflow/status/davidrm-bio/prelude_py/test.yaml?branch=main
[badge-issues]: https://img.shields.io/github/issues/davidrm-bio/prelude_py
[badge-stars]: https://img.shields.io/github/stars/davidrm-bio/prelude_py?style=flat&logo=github&color=yellow
[badge-coverage]: https://codecov.io/gh/davidrm-bio/prelude_py/branch/main/graph/badge.svg



`prelude_py` is a lightweight convenience module that provides lazy imports for commonly used scientific Python 
libraries through familiar aliases. Instead of importing each library individually, you can access them 
from a single namespace.

Modules are imported only when first accessed, so importing `prelude_py` itself has virtually no overhead.

## Installation

Install the package:

```bash
uv pip install prelude_py
```

To install all supported optional dependencies:

```bash
uv pip install "prelude_py[all]"
```

## Usage

```python
from prelude_py import np, pd, plt, sc

# NumPy
x = np.arange(10)

# Pandas
df = pd.DataFrame({"x": x})

# Matplotlib
plt.plot(x, x ** 2)
plt.show()

# Scanpy
adata = sc.read_h5ad("dataset.h5ad")
```

The first time an alias is accessed, the corresponding package is imported automatically. Subsequent accesses use the cached module.

## Available aliases

| Alias  | Package             |
| ------ | ------------------- |
| `np`   | `numpy`             |
| `nb`   | `numba`             |
| `pd`   | `pandas`            |
| `pl`   | `polars`            |
| `mpl`  | `matplotlib`        |
| `plt`  | `matplotlib.pyplot` |
| `sns`  | `seaborn`           |
| `ad`   | `anndata`           |
| `sc`   | `scanpy`            |
| `dc`   | `decoupler`         |
| `sq`   | `squidpy`           |
| `pt`   | `pertpy`            |
| `scvi` | `scvi`              |
| `do`   | `dotools_py`        |

## License

This project is distributed under the MIT License.
