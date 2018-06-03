import collections


def outputXML(filename, nodes) :

    # output format
    # key : time
    # value : [type, id, data...]
    output = dict()

    for node in nodes :

        # takeoff event
        time, height = node.takeoff()
        if not time in output.keys():
            output[time] = []
        output[time].append(["takeoff", node.id(), height])

        # landing event
        time = node.landing()
        if not time in output.keys() :
            output[time] = []
        output[time].append(["landing", node.id()])

        # move event
        for t in node.trajectory() :
            if  not t[0] in output.keys() :
                output[t[0]] = []
            output[t[0]].append(["move", node.id(), t[1], t[2], t[3]])

        # color event
        for c in node.color() :
            if  not c[0] in output.keys() :
                output[c[0]] = []
            output[c[0]].append(["led", node.id()] + c[1:])

    # Sorting
    output = collections.OrderedDict(sorted(output.items()))


    # Write
    line = "\n"

    with open(filename, "w") as f:

        str ="<?xml version=\"1.0\" encoding=\"UTF-8\" ?>"
        f.writelines(str+line)

        str ="<scenarios>"
        f.writelines(str+line)

        for time in output :
            str = "<scenario time=\"%.2f\"> " % (time)
            f.writelines(str+line)
            for v in output[time] :
                type = v[0]
                if type == "takeoff" :
                    str = '<takeoff id=\"%d\"> %.2f </takeoff>' % ( v[1], v[2])
                elif type == "landing":
                    str = '<landing id=\"%d\"> </landing>' % (v[1])
                elif type == "move" :
                    str = '<move id=\"%d\"> %.2f,%.2f,%.2f,0.0 </move>' % (v[1], v[2], -v[3], v[4])
                elif type == "led" :
                    str = '<led id=\"%d\"> %d,%d,%d,%d,%d,%d </led>' % (v[1], v[2], v[3], v[4], v[5], v[6], v[7])
                else :
                    print("ERR: unknown type : ", type)

                f.writelines(str+line)
            str = "</scenario>"
            f.write(str+line)

        str = "</scenarios>"
        f.write(str+line)
