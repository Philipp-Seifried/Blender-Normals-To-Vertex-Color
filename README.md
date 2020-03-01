# Normals To Vertex Colors Addon
## Overview
![Screenshot](http://www.philippseifried.com/github/normals_to_vertex_colors_v2.gif)

A simple Blender 2.8x addon that copies a selected object's normals to its vertex colors. Useful for some shader tricks. Vertex colors go from 0 to 1, so normals are encoded n*0.5+0.5

Based on the stackexchange solution here: https://blender.stackexchange.com/questions/32584/set-vertex-normals-to-vertex-color-in-python

## Installation
Navigate to Edit -> Preferences -> Addons -> Install. Select the .zip file or the unzipped normals_to_vertex_colors.py file.

## How To Use
In Vertex Paint mode, select "Paint -> Vertex Color from Normals" in the menu. Depending on your engine, you'll want to change which axis is mapped to which rgb channel. For Unity, the parameters for FBX exported using the default settings are -X, +Y, +Z. For FBX exported using "Experimental Apply Transform", the settings are -X, +Z, -Y.
