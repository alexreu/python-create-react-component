import platform
import os
import sys
import subprocess

# print(platform.system())
# print(os.path.isdir("/src/component"))
# print(sys.argv[1])

systemOs = platform.system()
checkDirectory = os.path.isdir("src/components")
componentName = sys.argv[1]

reactClassTemplate = [
    "import React, {Component} from 'react' \n",
    "class" + componentName + " extends Component { \n",
    "construct(props){ \n",
    "super(props) \n",
    "} \n",
    "render() { \n"
    "return Hello" + componentName + "\n",
    "}}"
]

if systemOs == "Linux":
    if checkDirectory:
        subprocess.call(["mkdir", "src/components/" + componentName])
        subprocess.call(["touch", "src/components/" + componentName + "/index.js"])
        subprocess.call(["touch", "src/components/" + componentName + "/" + componentName + ".js"])
        subprocess.call(["touch", "src/components/" + componentName + "/" + componentName + ".css"])
        component = open("src/components/" + componentName + "/" + componentName + ".js", "a")
        component.writelines(reactClassTemplate)
        component.close()
    else:
        subprocess.call(["mkdir", "src/components"])