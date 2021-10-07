import bpy
from math import radians

#####
# Crear Sol

#Crear esfera
bpy.ops.mesh.primitive_uv_sphere_add()
so = bpy.context.active_object

#Cambiar nombre
bpy.context.object.name = "Sol"

bpy.data.objects["Sol"].location[0] = 0.0
bpy.data.objects["Sol"].location[1] = 0.0
bpy.data.objects["Sol"].location[2] = 0.0

#Modificar el tamaño
bpy.data.objects["Sol"].scale[0] = 8.0
bpy.data.objects["Sol"].scale[1] = 8.0
bpy.data.objects["Sol"].scale[2] = 8.0

#Crear modificador
mod_subsurf = so.modifiers.new("Mi modificador", "SUBSURF")
mod_subsurf.levels = 3

#Smooth the object
bpy.ops.object.shade_smooth()

#####
# Crear Tierra

#Crear esfera
bpy.ops.mesh.primitive_uv_sphere_add()
so = bpy.context.active_object

#Cambiar nombre
bpy.context.object.name = "Tierra"

bpy.data.objects["Tierra"].location[0] = 0.0
bpy.data.objects["Tierra"].location[1] = 48.0
bpy.data.objects["Tierra"].location[2] = 0.0

#Modificar el tamaño
bpy.data.objects["Tierra"].scale[0] = 4.0
bpy.data.objects["Tierra"].scale[1] = 4.0
bpy.data.objects["Tierra"].scale[2] = 4.0

#Crear modificador
mod_subsurf = so.modifiers.new("Mi modificador", "SUBSURF")
mod_subsurf.levels = 3

#Smooth the object
bpy.ops.object.shade_smooth()

#####
# Camara
bpy.ops.object.camera_add(enter_editmode=False, align='VIEW')
bpy.context.object.name = "Camarita"

bpy.data.objects["Camarita"].location[0] = 80.0
bpy.data.objects["Camarita"].location[1] = 60.0
bpy.data.objects["Camarita"].location[2] = 80.0

bpy.data.objects["Camarita"].rotation_euler[0] = radians(45)
bpy.data.objects["Camarita"].rotation_euler[1] = radians(25)
bpy.data.objects["Camarita"].rotation_euler[2] = radians(100)

bpy.data.objects["Camarita"].scale[0] = 20.0
bpy.data.objects["Camarita"].scale[1] = 20.0
bpy.data.objects["Camarita"].scale[2] = 20.0

#####
# animar Tierra
import numpy as np
import mathutils
import math

Planeta = bpy.data.objects['Tierra']
planetaOrigin = np.array(Planeta.location)
theta = (2*math.pi)/250

def rotatePlaneta(scene):
    newTheta = theta*scene.frame_current
    rotationMatrix = np.array([[math.cos(newTheta), math.sin(newTheta), 0],
                               [math.sin(newTheta), math.cos(newTheta), 0],
                               [0, 0, 1]])
    Planeta.location = np.dot(planetaOrigin, rotationMatrix)

def setRotationPlaneta():
    # Clear old handlers
    bpy.app.handlers.frame_change_pre.clear()
    # register a new handler
    bpy.app.handlers.frame_change_pre.append(rotatePlaneta)

setRotationPlaneta()
