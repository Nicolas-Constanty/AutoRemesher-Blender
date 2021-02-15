import bpy
from .autoremesher import generate_quad_mesh
from bpy_extras.object_utils import object_data_add
from mathutils import Vector
import sys

modelTypeEnum = [
    ("0", "Organic", ""),
    ("1", "Hard Surface", "")]

class AutoRemesherSettings(bpy.types.PropertyGroup):
    density: bpy.props.FloatProperty(name="Density", default=0.0, min=0.0, max=1.0)
    edge_scale: bpy.props.IntProperty(name="Edge scaling", default=2, min=1, max=4)
    model_type: bpy.props.EnumProperty(
        name="Model Type",
        default="0", 
        items=modelTypeEnum
    )

class OBJECT_OT_autoremesher(bpy.types.Operator):
    """Generate Quad Mesh"""
    bl_idname = "object.auto_remesher"
    bl_label = "Generate Quad Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj is not None and obj.type == 'MESH')

    def execute(self, context):
        
        scene = context.scene
        obj = context.view_layer.objects.active
        data = obj.data

        ar_settings = context.scene.ar_settings
        vertices, faces = generate_quad_mesh(data.vertices.values(), data.polygons.values(), ar_settings.density, ar_settings.edge_scale, int(ar_settings.model_type))

        edges = []
        new_mesh = bpy.data.meshes.new(name="new_mesh")
        new_mesh.from_pydata(vertices, edges, faces)
        new_mesh.update()
        # make object from mesh
        new_object = bpy.data.objects.new('new_object', new_mesh)
        # make collection
        new_collection = bpy.data.collections.new('new_collection')
        bpy.context.scene.collection.children.link(new_collection)
        # add object to scene collection
        new_collection.objects.link(new_object)

        obj.select_set(False)
        bpy.data.objects[new_object.name].select_set(True)
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_loose()
        bpy.ops.mesh.delete(type='VERT')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

class MAINPANEL_PT_autoremesher(bpy.types.Panel):
    """AutoResmesher Panel"""
    bl_label = "AutoRemesher"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None)

    def draw(self, context):
        layout = self.layout
        
        ar_settings = context.scene.ar_settings
        box = layout.box()
        box.label(text="Settings")
        row = box.row()
        row.prop(ar_settings, "density")
        row = box.row()
        row.prop(ar_settings, "edge_scale")
        row = box.row()
        row.prop(ar_settings, "model_type")
        row = box.row()
        row.operator(OBJECT_OT_autoremesher.bl_idname)


