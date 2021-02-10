cd ThirdParties
svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/win64_vc15/tbb/
svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/win64_vc15/openvdb/

git clone https://github.com/microsoft/vcpkg
cd vcpkg
.\vcpkg.exe update
.\vcpkg.exe install cgal:x64-windows

cd ..

if exist python3.7\ (
	echo "Python already extracted"
) else (
	powershell -Command "Expand-Archive -Path python3.7.zip -DestinationPath ."
)

cd ..