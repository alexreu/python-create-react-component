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
    "import React, {Component} from 'react' \n\n",
    "class " + componentName + " extends Component { \n",
    "\tconstruct(props) { \n",
    "\t\tsuper(props) \n",
    "\t} \n\n",
    "\trender() { \n"
    "\t\treturn 'Hello " + componentName +"'\n",
    "\t} \n",
    "} \n",
    "export default " + componentName
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
        print("Successful create component")
    else:
        subprocess.call(["mkdir", "src/components"])