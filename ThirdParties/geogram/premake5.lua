-- premake5.lua
project "geogram"
    kind "StaticLib"
    language "C++"
    cppdialect "C++14"
    staticruntime "off"

    undefines { 
        "UNICODE"
    }

    files {
        "geogram_src/src/lib/geogram/basic/*.c",
        "geogram_src/src/lib/geogram/basic/*.cpp",
        "geogram_src/src/lib/geogram/basic/*.h",
        
        "geogram_src/src/lib/geogram/delaunay/*.c",
        "geogram_src/src/lib/geogram/delaunay/*.cpp",
        "geogram_src/src/lib/geogram/delaunay/*.h",
        
        "geogram_src/src/lib/geogram/bibliography/*.c",
        "geogram_src/src/lib/geogram/bibliography/*.cpp",
        "geogram_src/src/lib/geogram/bibliography/*.h",
       
        
        "geogram_src/src/lib/geogram/parameterization/*.c",
        "geogram_src/src/lib/geogram/parameterization/*.cpp",
        "geogram_src/src/lib/geogram/parameterization/*.h",

        "geogram_src/src/lib/geogram/mesh/*.c",
        "geogram_src/src/lib/geogram/mesh/*.cpp",
        "geogram_src/src/lib/geogram/mesh/*.h",
        
        "geogram_src/src/lib/geogram/points/*.c",
        "geogram_src/src/lib/geogram/points/*.cpp",
        "geogram_src/src/lib/geogram/points/*.h",

        "geogram_src/src/lib/geogram/numerics/*.c",
        "geogram_src/src/lib/geogram/numerics/*.cpp",
        "geogram_src/src/lib/geogram/numerics/*.h",
        
        "geogram_src/src/lib/geogram/NL/*.c",
        "geogram_src/src/lib/geogram/NL/*.cpp",
        "geogram_src/src/lib/geogram/NL/*.h",

        "geogram_src/src/lib/geogram/image/*.c",
        "geogram_src/src/lib/geogram/image/*.cpp",
        "geogram_src/src/lib/geogram/image/*.h",
        
        "geogram_src/src/lib/geogram/voronoi/*.c",
        "geogram_src/src/lib/geogram/voronoi/*.cpp",
        "geogram_src/src/lib/geogram/voronoi/*.h",
        
        "geogram_src/src/lib/geogram/third_party/LM7/*.c",
        "geogram_src/src/lib/geogram/third_party/LM7/*.cpp",
        "geogram_src/src/lib/geogram/third_party/LM7/*.h",

        "geogram_src/src/lib/geogram/third_party/rply/*.c",
        "geogram_src/src/lib/geogram/third_party/rply/*.cpp",
        "geogram_src/src/lib/geogram/third_party/rply/*.h",

        "geogram_src/src/lib/exploragram/hexdom/*.c",
        "geogram_src/src/lib/exploragram/hexdom/*.cpp",
        "geogram_src/src/lib/exploragram/hexdom/*.h",

        "include/geogram/geogram_report_progress.h",
        "include/geogram/version.h",
    }

    includedirs { 
        "geogram_src/src/lib",
        "include"
    }
    


