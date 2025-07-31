import sys
import subprocess
import importlib.util as importlib_util

class python_configuration:
    @classmethod
    def validate(cls):
      if not cls.__validate_python():
        return # cannot validate further

      for package_name in ["requests"]:
        if not cls.__validate_package(package_name):
          return # cannot validate further

    @classmethod
    def __validate_python(cls, major_version = 3, minor_version = 13):
      if sys.version is not None:
        print("Python version {0:d}.{1:d}.{2:d} detected.".format(\
          sys.version_info.major, sys.version_info.minor, sys.version_info.micro\
        ))
        if sys.version_info.major < major_version or (sys.version_info.major == major_version and sys.version_info.minor < minor_version):
          print("Python version too low, expected version {0:d}.{1:d} or higher.".format(\
            major_version, minor_version\
          ))
          return False
        return True

    @classmethod
    def __validate_package(cls, package_name):
      if importlib_util.find_spec(package_name) is None:
        return cls.__install_package(package_name)
      return True

    @classmethod
    def __install_package(cls, package_name):
      permission_granted = False
      while not permission_granted:
        reply = str(input("Would you like to install Python package '{0:s}'? [Y/N]: ".format(package_name))).lower().strip()[:1]
        if reply == 'n':
          return False
        permission_granted = (reply == 'y')
      
      print(f"Installing {package_name} module...")
      subprocess.check_call(['python', '-m', 'pip', 'install', package_name])

      return cls.__validate_package(package_name)

if __name__ == "__main__":
  python_configuration.validate()