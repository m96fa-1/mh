from utils import *
from setup_python import python_configuration

def main():
  python_configuration.validate()

  # Configuring libraries
  print("Configuring libraries...")
  print("Removing old vendor directories...")
  delete_dir("../mh/vendor/glfw")
  delete_dir("../mh/vendor/glm")
  delete_dir("../mh/vendor/imgui")

  print("Downloading necessary files...")
  download_file("https://github.com/glfw/glfw/archive/refs/heads/master.zip", "../mh/vendor/glfw.zip")
  download_file("https://github.com/g-truc/glm/archive/refs/heads/master.zip", "../mh/vendor/glm.zip")
  download_file("https://github.com/ocornut/imgui/archive/refs/heads/master.zip", "../mh/vendor/imgui.zip")

  print("Extracting downloaded files...")
  extract_zip("../mh/vendor/glfw.zip", "../mh/vendor/")
  extract_zip("../mh/vendor/glm.zip", "../mh/vendor/")
  extract_zip("../mh/vendor/imgui.zip", "../mh/vendor/")

  print("Cleaning up zip files...")
  delete_files("../mh/vendor/glfw.zip")
  delete_files("../mh/vendor/glm.zip")
  delete_files("../mh/vendor/imgui.zip")

  print("Renaming library directories...")
  rename_dir("../mh/vendor/glfw-master", "../mh/vendor/glfw")
  rename_dir("../mh/vendor/glm-master", "../mh/vendor/glm")
  rename_dir("../mh/vendor/imgui-master", "../mh/vendor/imgui")

  # Setting up the project directory
  project_name = input("Enter your project's name, or press Enter/Return for the same project name: ")

  with open(".projectname", "r") as file:
    old_project_name = file.read().strip()

  with open(".projectname", "w") as file:
    file.write(project_name)
  rename_dir(old_project_name, project_name)
  rename_dir(f"../{old_project_name}", f"../{project_name}")
  edit_file("premake5.lua", f"workspc = \"{old_project_name}\"", f"workspc = \"{project_name}\"")
  edit_file("premake5.lua", f"prj = \"{old_project_name}\"", f"prj = \"{project_name}\"")

  print(f"Setting up project: {project_name}")
  copy_file("premake5.lua", "..")
  copy_file(f"{project_name}/premake5.lua", f"../{project_name}")
  copy_file("mh/premake5.lua", "../mh")
  copy_file("glfw/premake5.lua", "../mh/vendor/glfw")
  copy_file("glad/premake5.lua", "../mh/vendor/glad")
  copy_file("imgui/premake5.lua", "../mh/vendor/imgui")

  os.chdir("..")

  print("Running premake...")
  run_premake()

  print("Cleaning up...")
  delete_files("premake5.lua")
  delete_files(f"{project_name}/premake5.lua")
  delete_files("mh/premake5.lua")
  delete_files("mh/vendor/glfw/premake5.lua")
  delete_files("mh/vendor/glad/premake5.lua")
  delete_files("mh/vendor/imgui/premake5.lua")

  input("Setup completed, press Enter/Return to exit...\n")

if __name__ == "__main__":
  main()
