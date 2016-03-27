#   myo     ready, floor/ceiling, on/off
         #  beacon      ready, 0/1/2/3
myo = open('outputMyo.txt', 'r')
beacon = open('outputBeacon.txt', 'r')

light = 0

#mazhar: light 0/1/2/3, 0/1,    0/1
#               room    floor   on/off

myostring = myo.readline()
beaconstring = beacon.readline()

#test if ready

if myostring[0:6] == 'Ready ':
    if beaconstring[0:6] == 'Ready ': 
        light = int(myostring[6:8]+beaconstring[6])


print(light)
print(myostring[6:8])
print(beaconstring[6])
'''
if (myo != NULL && beacon != NULL){
fscanf(myo, "%s %s %s", myoOut[0], myoOut[1], myoOut[2])

fscanf(beacon, "%s %s", beaconOut[0], beaconOut[1])

if(strcmp(beaconOut[0], "Ready") == 0 && strcmp(myoOut[0], "Ready") == 0)

if(strcmp(myoOut[1], "Floor"))
	if(strcmp(myoOut[2], "On"))
		if(strcmp(beacon[1], "**"))
		else if(***)
	else if (strcmp(myoOut[2], "Off")
else(strcmp(myoOut[1], "Ceiling"))
	if(strcmp(myoOut[2], "On"))
		if(strcmp(beacon[1], "**"))
		else if(***)
	else if (strcmp(myoOut[2], "Off")
}
'''
