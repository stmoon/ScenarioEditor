# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# 
# 이 프로그램은 시나리오 파일을 드론 내부 임베딩하기 위해 작성한 초안 프로그램이다
# 
# 

# <codecell>

#######################################################
# [seq], [sysid], [time(s)], [type], [arg1], [arg2], ...
# seq : should be more than 1 (not 0)
# type:  move, led, cmd
#   - args for move : x,y,z,heading
#   - args for led  : type, r,g,b,bright
#  - args for cmd  : 1 (offboard mode change), 2 (disarm) , 3 (arm)
#
# ex) 1, 4, 3.2, move, 0.1, 0.2, 0.3, 0.0
# ex) 1, 4, 3.2, cmd, 1
#####################################################

import xml.etree.ElementTree as et
import sys, getopt
import os
'''
argc = len(sys.argv)
if argc is 1:
    print "usage : pyhton scenario [sc_file] [ID]"
'''

verbose = False
target_id = 0

# check arguments
argc = len(sys.argv)
if argc is 1:
    print "usage : pyhton scenario [sc_file] [ID]"
    sys.exit()

# check scenario file
sc_file = sys.argv[1]
if not os.path.isfile(sc_file) :
    print "wrong file %s" % (sc_file)
    sys.exit()

# check optoins
args = sys.argv[2:]
try :
    opts, args = getopt.getopt(args, "vhi:", ["id"])
except getopt.GetoptError :
    print '%s -s <scenario file> -i <target id>' % sys.argv[0]

for opt, arg in opts :
    if opt == '-h' :
	sys.exit()
    elif opt == '-v' :
	verbose = True
    elif opt in ('-i', '--id') :
	target_id = int(arg)
	 

# parse xml file
doc = et.parse(sc_file)

# get root node
root = doc.getroot()

for target_id in range(1,21) :

    # create embedded sc file
    sc_file_name, sc_file_ext = os.path.splitext(sc_file)

    em_file = 'node_' + str(target_id) + '.txt'
    f = open(em_file, 'w')

    time = 1.0
    count = 1
    buf = "%d,%d,%.2f,cmd,arm" % (count, target_id, time)
    f.write(buf+'\r\n') 
    for scenario in root.iter('scenario') :    
        time = float(scenario.attrib['time'])
        for cmd in scenario :            
            id = int(cmd.attrib['id'])
            buf = '' 
            if id == target_id :
                count += 1
                cmd_str = cmd.tag.strip()
                values = cmd.text.strip()
                if cmd_str == 'takeoff' :
                    buf = "%d,%d,%.2f,takeoff,%s" % (count, id, time, values)
                elif cmd_str == 'move' :
                    buf = "%d,%d,%.2f,%s,%s" % (count, id, time, cmd_str, values)
                elif cmd_str == 'led' :
                    buf = "%d,%d,%.2f,%s,%s" % (count, id, time, cmd_str, values)
                elif cmd_str == 'landing' :
                    buf = "%d,%d,%.2f,landing,0" % (count, id, time)
                else :
                    buf = "ERROR"

	        if (verbose) :
	            print buf
	        
	        f.write(buf+'\r\n') 

    #buf = "%d,%d,%.2f,cmd,disarm" % (count, target_id, time + 3.0)
    f.write(buf+'\r\n') 
