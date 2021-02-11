# AutoRemesher Blender 2.8

Blender addon implementation of [AutoRemesher](https://github.com/huxingyi/autoremesher) by [huxingyi](https://github.com/huxingyi).
This implementation works only on Windows 10 at the moment.

![](https://raw.githubusercontent.com/Nicolas-Constanty/AutoRemesher-Blender/master/screenshots/00.PNG)
![](https://raw.githubusercontent.com/Nicolas-Constanty/AutoRemesher-Blender/master/screenshots/04.PNG)
<p align="center">
 <a href="https://raw.githubusercontent.com/Nicolas-Constanty/AutoRemesher-Blender/master/screenshots/03.PNG"><img src="https://raw.githubusercontent.com/Nicolas-Constanty/AutoRemesher-Blender/master/screenshots/03.PNG" /></a>
 </p>
 
## Install the addon in Blender
Download the package [here](https://github.com/Nicolas-Constanty/AutoRemesher-Blender/releases). **Do not extract it, Blender will use the .zip directly.**

Inside Blender :

- Edit->Preferences...->Add-ons->Install->Open "mesh_autoremesher.zip"
- Click the checkbox to enable the Add-on

⚠️ **This beta version of the addon only support Windows 10 - x64**

## Building AutoRemesher-Blender on Windows 10

### Install Development Tools
Subversion, Git, CMake and Visual Studio **must all be installed**.

* Install [Visual Studio 2019 Community Edition](https://visualstudio.microsoft.com/) (free, be sure to install the 'Desktop Development with C++' workload)
* Install [Subversion for Windows](http://www.sliksvn.com/en/download) (SlikSVN)
* Install [Git for Windows](https://gitforwindows.org/)
  * In the installer, choose to **add Git to your PATH** to ensure make update can correctly function.
* Install [CMake](http://cmake.org/)
  * In the installer set the system path option to **Add CMake to the system PATH for all users**.

### Setup the projet & Build libraries

Download the repository sources:

```
git clone --recursive -j8 https://github.com/Nicolas-Constanty/AutoRemesher-Blender.git
```
Download the libraries:
```
cd AutoRemesher-Blender
dependency.bat
```
Generate Visual Studio Solution:
```
build_project.bat
```

**Open autoremesher.sln** with Visual Studio.

You shoud be able to build the addon in Release or Debug mode. You will also need to build [Blender](https://github.com/blender/blender) in Debug mode to be able to debug it inside Visual Studio *(only if you build in Debug mode)*.
