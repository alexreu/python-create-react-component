import platform
import os
import sys

print(platform.system())
print(os.path.isdir("/src/component"))
print(sys.argv[1])

systemOs = platform.system()
checkDirectory = os.path.isdir("/src/component")
componentName = sys.argv[1]

if(systemOs == "linux"){

}
