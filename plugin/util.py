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
        for d, p, c in zip(node_data, node_plot, node_color) :
            t = round(count * 0.1, 2)

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

