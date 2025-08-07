
# Make sure to remove old data

while True:
    file = open("Parts list.txt","a")
    file.write("\n")
    file.write(input("\nEnter RMA: \n"))
    while True:
        part = input("\nParts: ")
        if part == "":
            break
        file.write(f"\n{part}")
    file.write("\n")
    file.close()
    break

#parts = ["Sieve beds","Rotary valve","Cup seals","Capacitor","Compressor","Front cover","Rear cover","Base enclosure","Compressor box(Spine)","Valve cap","Purge manifold - Low Pressure","Pressure regulator","Power switch","Flow meter","Main Board","Sintered filter","Filter door","Exhaust muffler"]

#print('\n'.join(map(str, parts)))


# "Sieve beds"
# "Rotary valve"
# "Cup seals"
# "Capacitor"
# "Compressor"
# "Front cover"
# "Rear cover"
# "Base enclosure"
# "Compressor box(Spine)"
# "Valve cap"
# "Purge manifold - Low Pressure"
# "Pressure regulator"
# "Power switch"
# "Flow meter"
# "Main Board"
# "Sintered filter"
# "Filter door"
# "Exhaust muffler"
# "No part needed"