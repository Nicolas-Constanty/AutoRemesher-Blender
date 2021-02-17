@echo off
echo:
echo ############################################################
echo ##                                                        ##
echo ##                   RUNNING PREMAKE 5                    ##
echo ##                                                        ##
echo ############################################################
echo: 
.\premake_v5\premake5.exe --file=premake5_37.lua vs2019
.\premake_v5\premake5.exe --file=premake5_39.lua vs2019