from utils import *
from setup_python import python_configuration

def main():
  python_configuration.validate()

  with open(".projectname", "r") as file:
    project_name = file.read().strip()

  reply = input("Would you like to reset project's name? [Y/N]: ").lower().strip()[:1]

  if reply == 'y':
    with open(".projectname", "w") as file:
      file.write("project_name")
    rename_dir(project_name, "project_name")
    rename_dir(f"../{project_name}", "../project_name")
    edit_file("premake5.lua", f"workspc = \"{project_name}\"", "workspc = \"project_name\"")
    edit_file("premake5.lua", f"prj = \"{project_name}\"", "prj = \"project_name\"")
    project_name = "project_name"

  os.chdir("..")
  
  print("Cleaning up your project...")
  system = platform.system()
  if system == "Windows":
    delete_dir(".vs")
    delete_files("*.sln")
    delete_files("mh/*.vcxproj*")
    delete_files(f"{project_name}/*.vcxproj*")
    delete_files("mh/vendor/glfw/*.vcxproj*")
    delete_files("mh/vendor/glad/*.vcxproj*")
    delete_files("mh/vendor/imgui/*.vcxproj*")
  elif system == "Linux":
    delete_dir(".vscode")

  delete_dir("bin")
  delete_dir("bin-int")
  delete_dir("mh/vendor/glfw/bin")
  delete_dir("mh/vendor/glfw/bin-int")
  delete_dir("mh/vendor/glad/bin")
  delete_dir("mh/vendor/glad/bin-int")
  delete_dir("mh/vendor/imgui/bin")
  delete_dir("mh/vendor/imgui/bin-int")
  
  input("Cleaning completed, press Enter/Return to exit...\n")

if __name__ == "__main__":
  main()