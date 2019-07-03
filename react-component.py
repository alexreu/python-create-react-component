import platform
import os
import sys

systemOs = platform.system()
checkDirectory = os.path.isdir("/src/component")
componentName = sys.argv[1]