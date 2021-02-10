    -- premake5.lua
workspace "autoremesher"

    architecture "x86_64"
    startproject "autoremesher"

    configurations
    { 
        "Debug",
        "Release"
    }

    flags {
        "MultiProcessorCompile"
    }

    -- Log library
    defines {
        "NDEBUG",
        "AUTOREMESHER_EXPORTS",
        "_WINDOWS",
        "_USRDLL",
        "_CRT_SECURE_NO_WARNINGS",
        "_USE_MATH_DEFINES",
        "NOMINMAX",
        "PY_SSIZE_T_CLEAN",
        "OPENEXR_DLL",
        "HALF_EXPORTS"
    }

    undefines { 
        "UNICODE"
    }

    filter "Debug"
        defines { "DEBUG" }
        defines { "USE_SPDLOG" }
        -- defines { "PRINT_LINE" }

    filter "Release"
        optimize "Full"


outputdir = "%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}"

group "Udan"
    include "ThirdParties/udan_debug"
    include "ThirdParties/udan_utils"
    include "ThirdParties/geogram"

group ""

project "autoremesher"
    kind "SharedLib"
    language "C++"
    cppdialect "C++14"
    staticruntime "off"

    files {
        "src/**.cpp",
        "src/autoremesher/**.cpp",
        "include/**.h",
        "include/autoremesher/**.h",
        "ThirdParties/openexr/IlmBase/Half/half.cpp",
        "ThirdParties/openexr/IlmBase/Half/toFloat.cpp"
    }

    libdirs {
        "ThirdParties/python3.7/libs",
        "ThirdParties/zlib/build/Release",
        "ThirdParties/openexr/build/IlmBase/Half/Release",
        "ThirdParties/openvdb/lib",
        "ThirdParties/vcpkg/installed/x64-windows/lib"
    }

    includedirs {
        "include",
        "ThirdParties/udan_debug/include",
        "ThirdParties/udan_utils/include",
        "ThirdParties/geogram/include/geogram",
        "ThirdParties/geogram/geogram_src/src/lib",
        "ThirdParties/SpdLog/include",
        "ThirdParties/python3.7/include",
        "ThirdParties/openvdb/include",
        "ThirdParties/geogram/src/lib",
        "ThirdParties/geogram",
        "ThirdParties/libigl/include",
        "ThirdParties/eigen",
        "ThirdParties/openexr/IlmBase/Half",
        "ThirdParties/vcpkg/installed/x64-windows/include"
    }

    links {
        "openvdb",
        "Half-2_5",
        "advapi32",
        "shell32",
        "user32",
        "opengl32",
        "udan_debug",
        "udan_utils",
        "geogram",
        "gmp",
        "mpfr"
    }

    filter "Release"
        libdirs {
            "ThirdParties/tbb/lib"
        }

        links {
            "tbb",
            "python37"
        }
    
    filter "Debug"
        libdirs {
            "ThirdParties/tbb/lib/debug"
        }

        links {
            "tbb_debug",
            "python37_d"
        }
        


