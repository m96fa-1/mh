project "mh"
    kind "SharedLib"
    language "C++"
    cppdialect "C++23"
    cdialect "C17"
    staticruntime "Off"
    systemversion "latest"

    targetdir ("../bin/" .. outputdir .. "/%{prj.name}")
    objdir ("../bin-int/" .. outputdir .. "/%{prj.name}")

    files {
        "src/**.h",
        "src/**.cpp",
        "vendor/glm/glm/**.hpp",
        "vendor/glm/glm/**.inl"
    }

    includedirs {
        "src",
        "vendor/glfw/include",
        "vendor/glad/include",
        "vendor/glm",
        "vendor/stb_image",
        "vendor/imgui"
    }

    defines {
        "GLFW_INCLUDE_NONE",
        "STB_IMAGE_IMPLEMENTATION"
    }

    links {
        "glfw",
        "glad",
        "imgui",
        "Opengl32",
    }

    pchheader "mhpch.h"
    pchsource "src/mhpch.cpp"

    filter "system:windows"
        defines {
            "MH_WINDOWS",
            "MH_BUILD_DLL"
        }

        postbuildcommands {
            ("IF NOT EXIST \"../bin/" .. outputdir .. "/" .. prj .. "/\" (mkdir \"../bin/" .. outputdir .. "/" .. prj .. "/\")"),
            ("{COPYFILE} \"%{cfg.buildtarget.relpath}\" \"../bin/" .. outputdir .. "/" .. prj .. "/\"")
        }

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