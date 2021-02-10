import bpy

from .src.autoremesherui import AutoRemesherSettings, OBJECT_OT_autoremesher, MAINPANEL_PT_autoremesher


bl_info = {
    "name": "AutoRemesher",
    "description": "AutoRemesher for Blender",
    "author": "nicolas constanty",
    "version": (1, 0, 0),
    "blender": (2, 91, 0),
    "wiki_url": "my github url here",
    "tracker_url": "my github url here/issues",
    "category": "Mesh"
}

classes = (
    AutoRemesherSettings,
    OBJECT_OT_autoremesher,
    MAINPANEL_PT_autoremesher
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    bpy.types.Scene.ar_settings = bpy.props.PointerProperty(type=AutoRemesherSettings)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)


if __name__ == "__main__":
    register()
