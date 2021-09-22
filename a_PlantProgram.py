import a_PlantClass as pc

primrose = pc.Plant("Green")

sunflower = pc.Flower("Yellow",12)

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())


#print(primrose.get_petals())
#this wouldn't work bcs primrose is a Plant and petals is an attribute of the flower subtype
