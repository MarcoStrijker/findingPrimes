""" 
This script compiles the code for all implementations.
"""

import os
import subprocess
import sys

from setuptools import setup
from setuptools import Extension


# Set the PYO3_PYTHON environment variable this enables maturin to find Python
os.environ["PYO3_PYTHON"] = sys.executable

project_path = os.path.dirname(__file__)



################################################################################
# C Implementation
# gcc -shared -o c_implementation\src\main.pyd -I"$INCLUDE_PATH" -L"$LIB_PATH" c_implementation\src\main.c -lpython313
################################################################################
os.chdir(os.path.join(project_path, "c_implementation"))

setup(
    name="main",
    version="1.0.0",
    packages=["src"],
    ext_modules=[
        Extension(
            "src.main",
            ["src/main.c"],
            include_dirs=[os.getenv("INCLUDE_PATH")],
            library_dirs=[os.getenv("LIB_PATH")],
            libraries=["python313"],
            extra_compile_args=[
                '/O2',
                '/Oi',
                '/GL',
                '/Gy',
                '/fp:fast',
                ] if sys.platform == 'win32' else [
                '-O3',
                '-march=native',
                '-ffast-math',
                '-flto',
                '-funroll-loops',
            ]
        )
    ],
)


################################################################################
# Cython Implementation
# cythonize --3str --no-docstrings -i cython_implementation\src\*.pyx
################################################################################
os.chdir(os.path.join(project_path, "cython_implementation"))

from Cython.Build import cythonize

setup(
    name="main",
    version="1.0.0",
    packages=["src"],
    requires=["cython"],
    ext_modules=cythonize(
        [
            Extension(
                "src.main",
                ["src/main.pyx"],
                extra_compile_args=["--no-docstrings"],
            )
        ],
    ),
)


################################################################################
# Mypyc Implementation
# cd mypyc_implementation\src && mypyc ..\..\python_implementation\src\main.py
################################################################################

os.chdir(os.path.join(project_path, "mypyc_implementation", "src"))
subprocess.run(["mypyc", "../../python_implementation/src/main.py", ], check=True)


os.chdir(os.path.join(project_path, "mypyc_implementation"))
setup(
    name="main",
    version="1.0.0",
    packages=["src"],
)


################################################################################
# Rust Implementation
# cd rust_implementation && maturin develop --release --strip --skip-install --bindings pyo3
################################################################################

os.chdir(os.path.join(project_path, "rust_implementation"))
subprocess.run(["maturin", "develop", "--release", "--skip-install", "--bindings", "pyo3"], check=True)

setup(
    name="main",
    version="1.0.0",
    packages=["src"],
)


