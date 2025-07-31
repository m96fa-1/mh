outputdir = "%{cfg.buildcfg}-%{cfg.architecture}-%{cfg.system}"
workspc = "project_name"
prj = "project_name"

workspace (workspc)
   architecture "x64"
   configurations { "Debug", "Release", "Dist" }
   startproject (prj)

group "dependencies"
    include "mh/vendor/glfw"
    include "mh/vendor/glad"
    include "mh/vendor/imgui"
group ""

group "core"
    include "mh"
group ""

include (prj)