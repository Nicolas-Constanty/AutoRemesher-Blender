#!/bin/bash

set -e

export CC="gcc"


export PY_VERSION=3.7m
export LD_LIBRARY_PATH=ThirdParties/python/$PY_VERSION/lib
rm -rf build/lib.linux-x86_64-$PY_VERSION
ThirdParties/python/$PY_VERSION/bin/python3 setup.py build
cp build/lib.linux-x86_64-3.7/* mesh_autoremesher/src

export PY_VERSION=3.8
export LD_LIBRARY_PATH=ThirdParties/python/$PY_VERSION/lib
rm -rf build/lib.linux-x86_64-$PY_VERSION
ThirdParties/python/$PY_VERSION/bin/python3 setup.py build
cp build/lib.linux-x86_64-$PY_VERSION/* mesh_autoremesher/src

export PY_VERSION=3.9
export LD_LIBRARY_PATH=ThirdParties/python/$PY_VERSION/lib
rm -rf build/lib.linux-x86_64-$PY_VERSION
ThirdParties/python/$PY_VERSION/bin/python3 setup.py build
cp build/lib.linux-x86_64-$PY_VERSION/* mesh_autoremesher/src

zip -r -u mesh_autoremesher_linux.zip mesh_autoremesher/