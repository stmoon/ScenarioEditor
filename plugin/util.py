import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def nextScenTime(time, duration) :
    return time, time + duration

def showNodeTrajectory(nodes, filename='') :

    mpl.rcParams['legend.fontsize'] = 10

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    node_data = []
    node_color = []
    node_plot = []

    for node in nodes :
        init_pos = node.property('init_pos')
        takeoff_time = node.property('takeoff_time')
        takeoff_height = node.property('takeoff_height')
        traj  = [[0.0] + init_pos]
        traj += [[takeoff_time, init_pos[0], init_pos[1], takeoff_height]]
        traj += node.trajectory()
        node_data.append(np.array(traj))
        node_color.append(np.array(node.color()))
        p, = ax.plot([], [], [], 'ro')
        node_plot.append(p)

    def animate(count):

        t = round(count * 0.1, 2)
        if t > 1.0 :
            checkDist(nodes, t)

        for d, p, c in zip(node_data, node_plot, node_color) :

            # trajectory
            if len(d) is 0 :
                continue
            time = d[:,0].tolist()
            if t in time :
                i = time.index(t)
                p.set_data(d[i,1], d[i,2])
                p.set_3d_properties(d[i,3])

            # color
            if len(c) is 0 :
                continue
            time = c[:,0].tolist()
            if t in time :
                i = time.index(t)
                str_c = '#%02x%02x%02x' % (int(c[i,3])%256, int(c[i,4])%256, int(c[i,5])%256)
                p.set_color(str_c)
                p.set_markeredgecolor('blue')


        return node_plot

    # set limitation of x,y,z
    min_limit = 0
    max_limit = 0
    for data in node_data :
        min = int(np.min(data[:,1:4])) - 1
        max = int(np.max(data[:,1:4])) + 1
        if min_limit > min :
            min_limit = min
        if max_limit < max :
            max_limit = max

    ax.set_xlim(min_limit, max_limit)
    ax.set_ylim(min_limit, max_limit)
    ax.set_zlim(0, max_limit)

    # calcuate max time
    max_time = 0
    for data in node_data:
        time = np.max(data[:,0])
        if max_time < time :
            max_time = time
    count = int(max_time*10)

    # start animation
    ani = animation.FuncAnimation(fig, animate, count, interval=100, repeat=False)

    if filename is not '' :
        # save the video
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=15, bitrate=1800)
        ani.save(filename, writer=writer)
    else :
        # show the plot
        plt.show()


def showScenarioTrajectory(scenario, filename='') :

    mpl.rcParams['legend.fontsize'] = 10

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    node_data = []
    node_plot = []

    scenario.run()

    traj = np.array(scenario.scenarioTrajectory())
    traj_plot, = ax.plot(traj[:, 0], traj[:, 1], traj[:, 2], color='gray', marker = 'o', markersize=2, label='scenario')
    traj_hist = scenario.trajHistory()

    for node in scenario.nodes():
        traj = scenario.trajectory(node)
        node_data.append(np.array(traj))
        p, = ax.plot([], [], [], 'ro')
        node_plot.append(p)


    def animate(i):

        traj_plot.set_data(traj_hist[i][:,0], traj_hist[i][:,1])
        traj_plot.set_3d_properties(traj_hist[i][:,2])

        for d, p in zip(node_data,node_plot) :
            p.set_data(d[i,1], d[i,2])
            p.set_3d_properties(d[i,3])
            p.set_color('red')
            p.set_markeredgecolor('blue')

        return node_plot

    # set limitation of x,y,z
    min_limit = 0
    max_limit = 0
    for data in node_data :
        min = int(np.min(data[:,1:4])) - 1
        max = int(np.max(data[:,1:4])) + 1
        if min_limit > min :
            min_limit = min
        if max_limit < max :
            max_limit = max


    ax.set_xlim(min_limit, max_limit)
    ax.set_ylim(min_limit, max_limit)
    ax.set_zlim(0, max_limit)

    # start animation
    count = len(node_data[0])
    ani = animation.FuncAnimation(fig, animate, count, interval=100, repeat=False)


    if filename is not '' :
        # save the video
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=15, bitrate=1800)
        ani.save(filename, writer=writer)
    else :
        # show the plot
        plt.show()


def checkSpeed(nodes) :
    node_pos = []

    for node in nodes :
        init_pos = node.property('init_pos')
        takeoff_time = node.property('takeoff_time')
        takeoff_height = node.property('takeoff_height')
        # traj  = [[0.0] + init_pos]
        traj = [[takeoff_time, init_pos[0], init_pos[1], takeoff_height]]
        traj += node.trajectory()
        node_pos.append(np.array(traj))


    for node in nodes :
        prev_pos = []
        max_vel = 0
        for curr_pos in node_pos[0] :
            if len(prev_pos) is not 0 :
                diff = np.array(curr_pos) - np.array(prev_pos)
                dt = diff[0]
                dist = np.linalg.norm(diff[1:4])
                max_vel = max([max_vel, dist/dt])
            prev_pos = curr_pos
        print("node %d max_vel: %.2f" %  (node.id(), max_vel))

def checkDist(nodes, time = 0.0) :
    MAX_DIST = 10000

    node_pos = {}
    for node in nodes :
        init_pos = node.property('init_pos')
        takeoff_time = node.property('takeoff_time')
        takeoff_height = node.property('takeoff_height')
        traj = [[takeoff_time, init_pos[0], init_pos[1], takeoff_height]]
        traj += node.trajectory()
        pos = dict((round(p[0],1), p[1::]) for p in traj )
        node_pos[node.id()] = pos


    ret = MAX_DIST
    if time == 0.0  :
        time_range =  np.arange(5, 200, 0.1)
    else :
        time_range = [time]
    
    for t in time_range :
        min_dist = MAX_DIST

        for target in node_pos.keys() :

            for neighbor in node_pos.keys():
                t = round(t,1)

                t2 = np.array(list(node_pos[neighbor].keys()))
                t2_tmp = t - t2
                t2_tmp[t2_tmp < 0] = MAX_DIST
                idx = t2_tmp.argmin()
                t2 = t2[idx]

                if t in node_pos[target] and t2 in node_pos[neighbor] and target is not neighbor:
                    diff = np.array(node_pos[target][t]) - np.array(node_pos[neighbor][t2])
                    dist = np.linalg.norm(diff)
                    min_dist = min([min_dist, dist])
                else :
                    pass

        if min_dist < MAX_DIST :
            print("Time[%.2f] : %.2f " % (t, min_dist))

        ret = min(ret, min_dist)

    if time == 0.0 :
        print("Result : %f" % (ret))
