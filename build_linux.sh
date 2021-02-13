#!/bin/bash

set -e

export CC="ccache gcc"
rm -rf build/lib.linux-x86_64-3.7
ThirdParties/python/bin/python3.7m setup.py build
cp build/lib.linux-x86_64-3.7/* mesh_autoremesher/src
zip -r -u mesh_autoremesher.zip mesh_autoremesher/