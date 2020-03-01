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
    "version": (0, 1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Paint > Vertex Color from Normals",
    "description": "Bakes selected object's normals to active vertex colors. Based on https://blender.stackexchange.com/questions/32584/set-vertex-normals-to-vertex-color-in-python",
    "category": "Paint",
}

import bpy
from mathutils import Vector
from bpy.props import (
    EnumProperty,
)


class NormalsToVertexColors(bpy.types.Operator):
    """Bakes selected object's normals to active vertex colors."""
    bl_idname = "paint.normals_to_vcol"
    bl_label = "Vertex Color from Normals"
    bl_options = {'REGISTER', 'UNDO'}

    space_items = (
        ('WORLD', "World", "Normals are encoded in world space"),
        ('LOCAL', "Local", "Normals are encoded in local space"),
    )
    space: EnumProperty(
        name="Space",
        items=space_items,
        default='WORLD',
    )

    @classmethod
    def poll(cls, context):
        if (context.mode != 'PAINT_VERTEX'):
            return False
        
        return True

    def execute(self, context):
        current_obj = bpy.context.active_object 
        mesh = current_obj.data
        if mesh.vertex_colors:
            vcol_layer = mesh.vertex_colors.active
        else:
            vcol_layer = mesh.vertex_colors.new()

        for loop_index, loop in enumerate(mesh.loops):
                loop_vert_index = loop.vertex_index
                normal = mesh.vertices[loop_vert_index].normal
                if (self.space == 'LOCAL'):
                    normal = current_obj.matrix_world.to_3x3() @ normal
                    normal.normalize()
                color = ( (normal * 0.5) + Vector((0.5,) * 3) )
                color.resize_4d()
                vcol_layer.data[loop_index].color = color

        mesh.vertex_colors.active = vcol_layer
        mesh.update()

        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(NormalsToVertexColors.bl_idname)


def register():
    bpy.utils.register_class(NormalsToVertexColors)
    bpy.types.VIEW3D_MT_paint_vertex.append(menu_func)


def unregister():
    bpy.utils.unregister_class(NormalsToVertexColors)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)


if __name__ == "__main__":
    register()
