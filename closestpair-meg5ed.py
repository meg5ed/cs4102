# Mary Graham (meg5ed)
# CS 4102 - Algorithms- S'18- Nate Brunelle
# HW2 Due Friday February 16, 2018 at 11PM Via Collab
# Collaborators: Parisa Roohafzaii 
# Sources: Introduction to Algorithms 3rd edition Cormen et al.
# Using Divide and Conquer Algorithm to find the closest pair of points in the n log n time 
# 

import sys
import math
import time


# euclidean distances of  points
def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])** 2 + (p1[1]-p2[1])** 2) 

def brute_force(x_list):
    minimum_distance = dist(x_list[0], x_list[1])
    p1 = x_list[0]
    p2 = x_list[1]
    length_of_x_list = len(x_list)
    if length_of_x_list == 2:
        return p1, p2, minimum_distance
    for i in range(length_of_x_list-1):
        for j in range(i + 1, length_of_x_list):
            if i != 0 and j != 1:
                d = dist(x_list[i], x_list[j])
                if d < minimum_distance:  
                    minimum_distance = d
                    p1, p2 = x_list[i], x_list[j]
    return p1, p2, minimum_distance

# divide and conquer algorithm
def closest_pair(x,y):
    length_of_x = len(x)   
    if length_of_x <= 3:   
        return brute_force(x)


# divide at median x coordinate
    median = length_of_x // 2   # divide by 2 & ignore remainder then divide that in half
    X_Left = x[:median]   
    X_Rirght = x[median:]   
    # finds midpoint by defining the x in median pair
    midpoint = x[median][0]
    # breaking y into arrays to be able to sort quickly
    Y_Left = []
    Y_Right = []
    for x_value in y:  # divide into left and right arrays using the midpoint for y list
        if x_value[0] <= midpoint:    # add x to left list if less or equal 
            Y_Left.append(x_value)
        if x[0] >= midpoint:
           Y_Right.append(x_value)    # add to right list if greater

# conquer recursively find closest pair from Left and Right 
    (p1, q1, d1) = closest_pair(X_Left, Y_Left)     
    (p2, q2, d2) = closest_pair(X_Rirght, Y_Right)     

    if d1 <= d2:
        minimum_distance = d1
        min_pt = (p1, q1)
    if d1 > d2:
        minimum_distance = d2
        min_pt = (p2, q2)
    (p3, q3, d3) = closest_runway_pair(x, y, minimum_distance, min_pt)

    if minimum_distance <= d3:
        return min_pt[0], min_pt[1], minimum_distance
    if minimum_distance > d3:
        return p3, q3, d3


def closest_runway_pair(P_Left, P_Right, delta, new_runway_pair):
    length_of_x = len(P_Left)
    midpoint = P_Left[length_of_x // 2][0]  
    # subarray of y that has the runway points
    subarray_y = [x for x in P_Right if midpoint - delta <= x[0] <= midpoint + delta]
    delta_distance = delta  
    # doing the same thing as closest_pair() but for  runway
    length_of_y = len(subarray_y)
    for i in range(length_of_y - 1): 
    # 7 points only need to be taken int account (see textbook)
        for j in range(i+1, min(i + 7, length_of_y)):
            p, q = subarray_y[i], subarray_y[j]
            new_delta_distance = dist(p, q)
            if new_delta_distance < delta_distance:
                new_runway_pair = p, q
                delta_distance = new_delta_distance # change current minimum to new minimum
    return new_runway_pair[0], new_runway_pair[1], delta_distance

def main():
    coordList = []
    with open("garden.txt", "r") as file:
        next(file)                       #reads second line bc first line is amount of points in garden.txt aka 5
        for line in file:
            myline = line.split()                              
            coordpoint = (float(myline[0]), float(myline[1]))  
            coordList.append(coordpoint)                       
        # sorting before using closest_pair function 
        xsort = sorted(coordList, key=lambda k: [k[0]])        
        ysort = sorted(coordList, key=lambda k: [k[1]])        
        file.close()
        x, y, distance = closest_pair(xsort,ysort)
        print(distance)  #prints distance of your two closest pairs of points

        # checking the time to ensure that it runs quickly for large amount of inputs
        #start_time = time.time()
        #print("--- %s seconds ---" % (time.time() - start_time))

if __name__=="__main__":
    main()