import os
import glob
import shutil
import platform
import subprocess
import requests
import zipfile

def download_file(url, destination):
  try:
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Check for HTTP errors

    with open(destination, 'wb') as file:
      for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk)
    
    print(f"Downloaded \"{url}\" to \"{destination}\"")
  except requests.RequestException as e:
    print(f"Error downloading \"{url}\": {e}")

def extract_zip(zip_path, extract_to = "."):
  try:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
      zip_ref.extractall(extract_to)
      print(f"Extracted \"{zip_path}\" to \"{extract_to}\"")
  except zipfile.BadZipFile as e:
    print(f"Error extracting \"{zip_path}\": {e}")
  except Exception as e:
    print(f"An error occurred while extracting \"{zip_path}\": {e}")

def rename_dir(old_name, new_name):
  try:
    os.rename(old_name, new_name)
    print(f"Renamed directory from \"{old_name}\" to \"{new_name}\"")
  except FileNotFoundError:
    print(f"Directory \"{old_name}\" not found.")
  except Exception as e:
    print(f"Error renaming \"{old_name}\" directory: {e}")

def delete_dir(path):
  try:
    shutil.rmtree(path)
    print(f"Deleted directory \"{path}\"")
  except FileNotFoundError:
    print(f"Directory \"{path}\" not found.")
  except Exception as e:
    print(f"Error deleting directory \"{path}\": {e}")

def edit_file(file_path, old_line, new_line):
  try:
    with open(file_path, 'r') as file:
      lines = file.readlines()
    
    with open(file_path, 'w') as file:
      for line in lines:
        if old_line in line:
          line = new_line + '\n'
        file.write(line)

    print(f"Edited \"{file_path}\": replaced \"{old_line}\" with \"{new_line}\"")
  except Exception as e:
    print(f"Error editing \"{file_path}\": {e}")

def copy_file(src, dst):
  try:
    shutil.copy(src, dst)
    print(f"Copied \"{src}\" to \"{dst}\"")
  except Exception as e:
    print(f"Error copying \"{src}\" to \"{dst}\": {e}")

def delete_files(path):
  for file_path in glob.glob(path):
    try:
      os.remove(file_path)
      print(f"Deleted \"{file_path}\"")
    except Exception as e:
      print(f"Error deleting \"{file_path}\": {e}")

def run_premake():
  premake_exe = ""
  premake_args = ""
  system = platform.system()
  
  if system == "Windows":
    premake_exe = ".\\vendor\\premake5-x64-windows\\premake5.exe"
    premake_args = "vs2022"
  elif system == "Linux":
    premake_exe = "./vendor/premake5-x64-linux/premake5"
    premake_args = "gmake"
  elif system == "Darwin": # macos
    premake_exe = "./vendor/premake5-x64-macosx/premake5"
    premake_args = "xcode4"
  else:
    print("Your operating system is not supported. Please contact me to add support for it.")
    return

  subprocess.run([premake_exe, premake_args])
