# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Normals To Vertex Colors",
    "author": "Philipp Seifried",
    "version": (0, 1, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Paint > Vertex Color from Normals",
    "description": "Bakes selected object's normals to active vertex colors. Based on https://blender.stackexchange.com/questions/32584/set-vertex-normals-to-vertex-color-in-python",
    "category": "Paint",
}

from .normals_to_vertex_colors import *