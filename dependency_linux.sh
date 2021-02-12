#!/bin/bash

set -e

cd ThirdParties

ROOT=`pwd`

echo
echo ############################################################
echo ##                                                        ##
echo ##           CHECKOUT BLENDER SVN DEPENDENCIES            ##
echo ##                                                        ##
echo ############################################################
echo

svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/linux_centos7_x86_64/tbb/
svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/linux_centos7_x86_64/openvdb/
svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/linux_centos7_x86_64/gmp/
svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/linux_centos7_x86_64/openexr/
svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/linux_centos7_x86_64/python python3.7

echo
echo ############################################################
echo ##                                                        ##
echo ##           INSTALL CGAL and BOOST with VCPKG            ##
echo ##                                                        ##
echo ############################################################
echo

cd vcpkg
./bootstrap-vcpkg.sh -disableMetrics
./vcpkg update
./vcpkg install yasm-tool:x86-windows
./vcpkg install cgal:x64-windows
./vcpkg install boost-uuid:x64-windows

cd ..

echo
echo DEPENDENCIES SUCCESSFULLY INSTALLED
echo You can now run build_project.bat