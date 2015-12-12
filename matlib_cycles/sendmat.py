
import bpy, json
class EmptyProps(bpy.types.PropertyGroup):
	pass
bpy.utils.register_class(EmptyProps)
bpy.types.Scene.matlib_categories = bpy.props.CollectionProperty(type=EmptyProps)
cats = []
for cat in bpy.context.scene.matlib_categories:
	materials = []
	for mat in bpy.data.materials:
		if "category" in mat.keys() and mat['category'] == cat.name:
			materials.append(mat.name)
	cats.append([cat.name, materials])
with open("C:\\Users\\Dell\\Downloads\\blender-2.76-301115-win64\\blender-2.76.0-git.3780158-AMD64\\2.76\\scripts\\addons\\matlib_cycles\\categories.txt", "w") as f: 
	f.write(json.dumps(cats, sort_keys=True, indent=4))
