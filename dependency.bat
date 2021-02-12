@echo off

cd ThirdParties
if %errorlevel% neq 0 exit /b %errorlevel%

set ROOT=%cd%
set PLATFORM=x64

echo:
echo ############################################################
echo ##                                                        ##
echo ##           CHECKOUT BLENDER SVN DEPENDENCIES            ##
echo ##                                                        ##
echo ############################################################
echo: 

svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/win64_vc15/tbb/
if %errorlevel% neq 0 exit /b %errorlevel%
svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/win64_vc15/openvdb/
if %errorlevel% neq 0 exit /b %errorlevel%
svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/win64_vc15/gmp/
if %errorlevel% neq 0 exit /b %errorlevel%
svn checkout https://svn.blender.org/svnroot/bf-blender/trunk/lib/win64_vc15/openexr/
if %errorlevel% neq 0 exit /b %errorlevel%

echo:
echo ############################################################
echo ##                                                        ##
echo ##           INSTALL CGAL and BOOST with VCPKG            ##
echo ##                                                        ##
echo ############################################################
echo: 

cd vcpkg
if %errorlevel% neq 0 exit /b %errorlevel%
.\bootstrap-vcpkg.bat -disableMetrics
.\vcpkg.exe update
.\vcpkg.exe install cgal:x64-windows
if %errorlevel% neq 0 exit /b %errorlevel%1
.\vcpkg.exe install boost-uuid:x64-windows
if %errorlevel% neq 0 exit /b %errorlevel%1

cd ..

echo:
echo ############################################################
echo ##                                                        ##
echo ##                   EXTRACT PYTHON                       ##
echo ##                                                        ##
echo ############################################################
echo:

if exist python3.7\ (
	echo Python already extracted
) else (
	powershell -Command "Expand-Archive -Path python3.7.zip -DestinationPath ."
)
if %errorlevel% neq 0 exit /b %errorlevel%

cd ..

echo:
echo DEPENDENCIES SUCCESSFULLY INSTALLED
echo You can now run build_project.bat