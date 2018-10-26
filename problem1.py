# Manny Pagan
# Sept 24th Python Course
# Assignment 9
# Due: Oct 29th

import geocoder

destinations = [
    'Space Needle',
    'Crater Lake',
    'Golden Gate Bridge',
    'Yosemite National Park',
    'Las Vegas, Nevada',
    'Grand Canyon National Park',
    'Aspen, Colorado',
    'Mount Rushmore',
    'Yellowstone National Park',
    'Sandpoint, Idaho',
    'Banff National Park',
    'Capilano Suspension Bridge'
]

for destination in destinations:
    y = geocoder.arcgis(destination)
    z = y.latlng
    print("{} is located at {}".format(destination, z))

# a = geocoder.arcgis('Crater Lake')
# b = geocoder.arcgis('Golden Gate Bridge')
# c = geocoder.arcgis('Yosemite National Park')
# d = geocoder.arcgis('Las Vegas, Nevada')
# e = geocoder.arcgis('Grand Canyon National Park')
# f = geocoder.arcgis('Aspen, Colorado')
# g = geocoder.arcgis('Mount Rushmore')
# h = geocoder.arcgis('Yellowstone National Park')
# i = geocoder.arcgis('Sandpoint, Idaho')
# j = geocoder.arcgis('Banff National Park')
# k = geocoder.arcgis('Capilano Suspension Bridge')
# coordinates = geocoder.arcgis(destination)
# coordinates = destination.latlng
# latlng_variable = str(destination.latlng())
# print("{} is located at {}".format(destination, coordinates))

# if destination == 'Crater Lake':
#     print("Crater Lake is located at " + str(a.latlng))
# elif destination == 'Golden Gate Bridge':
#     print("Golden Gate Bridge is located at " + str(b.latlng))
# elif destination == 'Yosemite National Park':
#     print("Yosemite National Park is located at " + str(c.latlng))
# elif destination == 'Las Vegas, Nevada':
#     print("Las Vegas, Nevada is located at " + str(d.latlng))
# elif destination == 'Grand Canyon National Park':
#     print("Grand Canyon National Park is located at " + str(e.latlng))
# elif destination == 'Aspen, Colorado':
#     print("Aspen, Colorado is located at " + str(f.latlng))
# elif destination == 'Mount Rushmore':
#     print("Mount Rushmore is located at " + str(g.latlng))
# elif destination == 'Yellowstone National Park':
#     print("Yellowstone National Park is located at " + str(h.latlng))
# elif destination == 'Sandpoint, Idaho':
#     print("Sandpoint, Idaho is located at " + str(i.latlng))
# elif destination == 'Banff National Park':
#     print("Banff National Park is located at " + str(j.latlng))
# elif destination == 'Capilano Suspension Bridge':
#     print("Capilano Suspension Bridge is located at " + str(k.latlng))


