#!/usr/bin/python3

# open file1 - "bunker east"
bedata = open("bunkereast.txt", "r")

# open file2 - "bunker west"
bwdata = open("bunkerwest.txt", "r")

# read file1 - "bunker east"
belines = bedata.readlines()

# read file2 - "bunker west"
bwlines = bwdata.readlines()

#close file1 - "bunker east"
bedata.close()

#close file2 - "bunker west"

# create a single file of all our lines
bafile = open('bunkerall.txt', 'w')
for switch in belines:
    bafile.write('e-' + switch.rstrip('\n') + '\n')
for switch in bwlines:
    bafile.write('w-' + switch.rstrip('\n') + '\n')
bafile.close() # close single file of all times

# read in all lines from our single file
bafile = open('bunkerall.txt', 'r')
balines = bafile.readlines()
bafileip = open('bunkerips.txt', 'w') # create a new file for ips only
for line in balines:
    bafileip.write(line.split(' ')[1]) # just write out ips

bafileip.close()
bafile.close()

# combine data sets
# lists [] and dict {key:value}

bunkerdict = {}
bedata = open('bunkereast.txt', 'r')
belist = bedata.readlines()
bedata.close() # close our open file
for line in belist:
    hostip = line.split(' ')
    bunkerdict[hostip[0]] = hostip[1].rstrip('\n')

eastwest = {}
eastwest.update({'east': bunkerdict})

bunkerdict = {}
bedata = open('bunkereast.txt', 'r')
belist = bedata.readlines()
bedata.close() # close our open file
for line in belist:
    hostip = line.split(' ')
    bunkerdict[hostip[0]] = hostip[1].rstrip('\n')

bunkerdict.clear()
bwdata = open('bunkerwest.txt', 'r')
bwlist = bwdata.readlines()
bwdata.close()
for lin in bwlist:
    hostip = line.split(' ')
    bunkerdict[hostip[0]] = hostip[1].rstrip('\n')

eastwest.update({"west": bunkerdict})
print(eastwest)

#[{"sw1": "10.0.0.1", "sw2": "10.0.0.2"}, {"sw1": "192.168.0.1, "sw2": "192.168.0.2"}]

#{"east":{"sw1": "10.0.0.1", "sw2": "10.0.0.2"}, "west":{"sw1": "192.168.0.1, "sw2": "192.168.0.2"}}

# write out to file3 - "bunker all"
