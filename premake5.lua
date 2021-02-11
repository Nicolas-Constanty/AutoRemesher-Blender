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
        symbols "On"
        buildoptions { "/Zm250", "/bigobj" }
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
    targetextension ".pyd"

    files {
        "src/**.cpp",
        "src/autoremesher/**.cpp",
        "include/**.h",
        "include/autoremesher/**.h"
    }

    libdirs {
        "ThirdParties/python3.7/libs",
        "ThirdParties/zlib/build/Release",
        "ThirdParties/openexr/lib",
        "ThirdParties/openvdb/lib",
        "ThirdParties/gmp/lib",
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
        "ThirdParties/tbb/include",
        "ThirdParties/geogram/src/lib",
        "ThirdParties/geogram",
        "ThirdParties/libigl/include",
        "ThirdParties/eigen",
        "ThirdParties/openexr/include",
        "ThirdParties/vcpkg/installed/x64-windows/include"
    }

    links {
        "openvdb",
        "advapi32",
        "shell32",
        "user32",
        "opengl32",
        "udan_debug",
        "udan_utils",
        "geogram",
        "libgmp-10",
        "zlib"
    }

    filter "Release"
        targetname "autoremesher"
        libdirs {
            "ThirdParties/tbb/lib"
        }

        links {
            "Half_s",
            "tbb",
            "python37"
        }

        postbuildcommands {
            "copy bin\\Release\\autoremesher.pyd mesh_autoremesher\\src",
            "powershell -Command \"Compress-Archive -Update -LiteralPath 'mesh_autoremesher\'  -DestinationPath mesh_autoremesher.zip\""
        }
    
    filter "Debug"
        targetname "autoremesher_d"
        libdirs {
            "ThirdParties/tbb/lib/debug"
        }

        links {
            "Half_s_d",
            "tbb_debug",
            "python37_d"
        }
        
        postbuildcommands {
            "copy bin\\Debug\\autoremesher_d.pyd mesh_autoremesher\\src",
            "powershell -Command \"Compress-Archive -Update -LiteralPath 'mesh_autoremesher\'  -DestinationPath mesh_autoremesher.zip\""
        }

local function disableVcpkg(prj)
    premake.w('<VcpkgEnabled>No</VcpkgEnabled>')
end

require('vstudio')

premake.override(premake.vstudio.vc2010.elements, "globals", function(base, prj)
    local calls = base(prj)
    table.insertafter(calls, premake.vstudio.vc2010.globals, disableVcpkg)
    return calls
end)
