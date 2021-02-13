#!/bin/bash

set -e

sudo add-apt-repository universe
sudo apt -y update
sudo apt -y install subversion
sudo apt -y install curl zip unzip tar
sudo apt -y install cmake 
sudo apt -y install g++
sudo apt -y install autoconf autoconf-archive
sudo apt -y install libtool
sudo apt -y install libpthread-stubs0-dev
sudo apt -y install texinfo
sudo apt -y install ccache

cd ThirdParties

export ROOT=`pwd`
export CFLAGS="-std=c++17"
export CXX=`which g++`

echo
echo "############################################################"
echo "##                                                        ##"
echo "##           CHECKOUT BLENDER SVN DEPENDENCIES            ##"
echo "##                                                        ##"
echo "############################################################"
echo

svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/linux_centos7_x86_64/tbb/
svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/linux_centos7_x86_64/openvdb/
svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/linux_centos7_x86_64/gmp/
svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/linux_centos7_x86_64/blosc/
svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/linux_centos7_x86_64/openexr/
svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/linux_centos7_x86_64/python
svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/linux_centos7_x86_64/boost

echo
echo "############################################################"
echo "##                                                        ##"
echo "##           INSTALL CGAL and BOOST with VCPKG            ##"
echo "##                                                        ##"
echo "############################################################"
echo

cd vcpkg
if [ -e vcpkg ]
then
echo "Vcpkg already built."
else
./bootstrap-vcpkg.sh -disableMetrics
fi
./vcpkg update
./vcpkg install cgal:x64-linux
./vcpkg install boost-uuid:x64-linux
./vcpkg install boost-iostreams:x64-linux
./vcpkg install boost-locale:x64-linux
./vcpkg install boost-wave:x64-linux

cd ..

echo
echo DEPENDENCIES SUCCESSFULLY INSTALLED
echo You can now run build_project.bat