project (prj)
    kind "ConsoleApp"
    language "C++"
    cppdialect "C++23"
    cdialect "C17"
    staticruntime "Off"
    systemversion "latest"

    targetdir ("../bin/" .. outputdir .. "/%{prj.name}")
    objdir ("../bin-int/" .. outputdir .. "/%{prj.name}")

    files {
        "src/**.h",
        "src/**.cpp"
    }

    includedirs {
        "src",
        "../mh/src",
        "../mh/vendor/glm"
    }

    links {
        "mh"
    }

    filter "system:windows"
        defines "MH_WINDOWS"

    filter "system:macosx"
        defines "MH_MACOSX"

    filter "system:linux"
        defines "MH_LINUX"

    filter "configurations:Debug"
        defines "MH_DEBUG"
        runtime "Debug"
        symbols "On"
        
    filter "configurations:Release"
        defines "MH_RELEASE"
        runtime "Release"
        optimize "On"
        symbols "On"
        
    filter "configurations:Dist"
        kind "WindowedApp"
        defines "MH_DIST"
        runtime "Release"
        optimize "On"
        symbols "On"