Addon By Mackraken (mackraken2023@hotmail.com)
Materials Files By meta-androcto
to collaborate either send a message or pull request if you clone this repo.

Matlib Credits:
Materials collection compiled & maintained by Meta-Androcto over several years.
All materials have been renamed, most groups have been renamed, all image textures have been removed(most replaced with node groups), many node trees have been changed or rewritten.
Addon by Alfonso Serra https://sites.google.com/site/aleonserra/home/scripts/matlib-vx-5-6
Special thanks to Sybren & TynkaTopi for help with scripts to sort nodes & materials.
Original Authors: 
Kramon, guismo, elbrujodel,  Mr_Lamppost, Charblaze, shivraj, mStuff, Kaluura, ata4, enilnacs, cgcookie, 
GyngaNynja, DarkCrescent, kavabanga, Alphisto, Wiser, ThorntonJStrolia, huggaida, flaken369, BigMouse, arenyart,
mackanov, 28selves, slickracoonpaws, tdmsiska, tynaud, ManuelL, kilbeeu, Family1, CGMasters, sadaj72,
Lucasvreis, xBlend2, Oceanoblu, ShadowCamero, meigo, bytewav, Alvarocgi, flaken369, oblyz, gp3991,
Saiyan, Avenger, ziwerliz, alain oiselet, dreadbwai, JDHaller, Joster, Motion, VirusZParadox, AlanShukan, 
Regus, Mr_Lamppost, CgAlpha, jakaboxjumping, Cebbi, jkon, HellGate, mherpin, seraphim10, mbeke2, varkenvarken, sambler, Blender Guru, 
champignondobrasil, sizzler, Wooxen, lklleb, Mikel007, TowerCG, blenderdiplom.com, dingto, Kaluura, brecht,
Conner Addison, agus3d, 19seanak19, neon15, budip, jenov, Substance_Painter, Bartek Skorupa, BlenderNerd, MmAaXx,
meta-androcto, mib2berlin, kellpossible, monsterdog, Jonathon L, elbrujodelatribu, lubomircenovsky, wesdevs,
ace dragon, naibot, gwenouille, NRK, Agus, dimistic, broadstu, gexwing, const, moony, enzyme69, enzyme69, JuanJosé Torres, Greg Zaal, sambler.
Materials from sites:
blender diplom, blender nation materials section, blend swap, blender artists forums, git hub & anyone I've forgotten, let me know, I'll add you.

# #####BEGIN GPL LICENSE BLOCK #####
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
# #####END GPL LICENSE BLOCK #####

bl_info = {
	"name": "Material Library",
	"author": "Mackraken (mackraken2023@hotmail.com)",
	"version": (0, 5, 61),
	"blender": (2, 7, 2),
	"api": 60995,
	"location": "Properties > Material",
	"description": "Material Library VX",
	"warning": "",
	"wiki_url": "https://sites.google.com/site/aleonserra/home/scripts/matlib-vx",
	"tracker_url": "",
	"category": "System"}

MATLIB 5.6.1

Installation:

- Copy the matlib folder inside Blender's addons.
Example: D:\Blender\2.76\scripts\addon\

- Start Blender.
- Goto File->User Preferences->Addons
- Enable "Material Library"


Updates:
v 0.5.61
- Libraries arent read on each draw call, only on startup or when added. This fixes potential crashes and is less stressful, but  when a library is deleted blender should be restarted.
-Moved the addon from "System" category to "Materials"

v 0.5.6
- Create new libraries.
	Libraries are read from the matlib folder. If you want to change this behaviour, edit the variable "matlib_path" at line 40. (Untested)
	
	To delete a library delete the blend file within the matlib folder.
        To Add a Library, Simply drop a new .blend file into the matlib directory.

- Apply material to all selected objects.

- Apply material in edit mesh mode.

- Improved Material preview.
	You can apply a material to the last selected object/s while you are previewing.

- Categories are saved within the library blend file.

- More warnings when things goes wrong.

- Options Added:
	- Force Import. False By default.
		This option helps to avoid material duplicates when the same material its applied several times.
		When this option is disabled the script will try to find the selected material within the working scene, instead of importing a new one from the library. 
	- Linked.
		Import the material by making a link to the library.
	- Hide search.
		Shows or hides the search box.


