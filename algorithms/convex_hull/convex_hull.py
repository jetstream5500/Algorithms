import math
import numpy as np
import matplotlib.pyplot as plt
import random
import functools

def is_convex(a, b, c):
    ''' Takes 3 points (a, b, c) and computes whether the cross product of
    vector a->b and vector b->c is negative (Negative cross product represents
    convex in this setup)'''
    return (b[0]-a[0])*(c[1]-b[1]) - (b[1]-a[1])*(c[0]-b[0]) < 0

def fetch_points(filename):
    points = []
    with open('test.in', 'r') as fin:
        for line in fin:
            p = tuple(map(float,line.split()))
            points.append(p)

    return points

def lowest_point_index(points):
    min_point = [float('inf'), float('inf')]
    min_index = -1
    for i,p in enumerate(points):
        if p[1] < min_point[1]:
            min_point = p
            min_index = i
        elif (p[1] == min_point[1] and p[0] > min_point[0]):
            min_point = p
            min_index = i

    return min_index

def generate_hull_plot(points, hull):
    points_xs = [p[0] for p in points]
    points_ys = [p[1] for p in points]
    plt.plot(points_xs, points_ys, 'o')

    hull_xs = [p[0] for p in hull]
    hull_ys = [p[1] for p in hull]
    hull_xs.append(hull_xs[0])
    hull_ys.append(hull_ys[0])
    plt.plot(hull_xs, hull_ys, '-o', markersize=3)
    plt.show()

def generate_random_integer_points(size = 1000, min = -10, max = 10):
    return [(random.randint(min, max), random.randint(min, max)) for i in range(size)]

def generate_random_float_points(size = 300, min = -10, max = 10):
    return [(random.random()*(max-min)+min, random.random()*(max-min)+min) for i in range(size)]

def angle_cmp(a, b, min_point):
    k_a = (a[0]-min_point[0]) / math.sqrt((a[1]-min_point[1])**2 + (a[0]-min_point[0])**2)
    k_b = (b[0]-min_point[0]) / math.sqrt((b[1]-min_point[1])**2 + (b[0]-min_point[0])**2)
    if k_a < k_b:
        return -1
    elif k_a > k_b:
        return 1
    else:
        if ((a[0]-min_point[0])*(b[0]-a[0]) >= 0) and ((a[1]-min_point[1])*(b[1]-a[1]) >= 0):
            return -1
        else:
            return 1

def graham_scan(filename=None):
    points = []
    if filename is None:
        points = list(set(generate_random_float_points()))
    else:
        points = list(set(fetch_points(filename)))
    min_index = lowest_point_index(points)
    min_point = points.pop(min_index)

    def angle_cmp_mod(a, b):
        return angle_cmp(a, b, min_point)

    points.sort(key=functools.cmp_to_key(angle_cmp_mod))
    points.insert(0, min_point)

    hull = []
    for p in points:
        hull.append(p)
        while len(hull) > 2:
            if is_convex(hull[-3], hull[-2], hull[-1]):
                break
            else:
                hull.pop(-2)

    print(hull)
    generate_hull_plot(points, hull)

if __name__ == '__main__':
    graham_scan()
