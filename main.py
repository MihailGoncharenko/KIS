import numpy as np
import PIL
from PIL import Image
from numpy import asarray
import math

def find_north(arr):
    x = 0
    y = 0
    for i in range (0, arr.shape[0]):
        for j in range (0, arr.shape[1]):
            if arr[i][j][0] == 0:
                if (y < i):
                    y = i
                    x = j
    return (x, y)
    
def find_west(arr):
    x = 0
    y = 0
    for i in range (0, arr.shape[0]):
        for j in range (0, arr.shape[1]):
            if arr[i][j][0] == 0:
                if (x < j):
                    y = i
                    x = j
    return (x, y)
def find_east(arr):
    x = arr.shape[1]
    y = arr.shape[0]
    for i in range (0, arr.shape[0]):
        for j in range (0, arr.shape[1]):
            if arr[i][j][0] == 0:
                if (x > j):
                    y = i
                    x = j
    return (x, y)
def find_south(arr):
    x = arr.shape[1]
    y = arr.shape[0]
    for i in range (0, arr.shape[0]):
        for j in range (0, arr.shape[1]):
            if arr[i][j][0] == 0:
                if (y > i):
                    y = i
                    x = j
    return (x, y)

def find_northeast(arr):
    x = 0
    y = 0
    for i in range (0, arr.shape[0]):
        for j in range (0, arr.shape[1]):
            if arr[i][j][0] == 0:
                if (y <= i):
                    y = i
                    x = j
    return (x, y)

def pifagor(a, b):
    return ((a[0]-b[0])**2 +(a[1]-b[1])**2)**0.5

name = input()
image = Image.open(name)
array = asarray(image)
north = find_north(array)
west = find_west(array)
east = find_east(array)
south = find_south(array)
if (north[0] == south[0] and west[1] == east[1] and north != west):
    print("Это круг!")
    print("Радиус:", end = ' ')
    print((north[1]-south[1])/2)
elif (north == east or north == west or south == east or south == west) and not (north == east and south == east):
    print("Это треугольник!")
    if (north == east):
        point1 = north
        point2 = west
        point3 = south
    if (north == west):
        point1 = north
        point2 = east
        point3 = south
    if (south == east):
        point1 = north
        point2 = west
        point3 = south
    if (south == west):
        point1 = north
        point2 = east
        point3 = south
    print("Сторона 1:", end = ' ')
    print(pifagor(point1, point2))
    print("Сторона 2:", end = ' ')
    print(pifagor(point1, point3))
    print("Сторона 3:", end = ' ')
    print(pifagor(point2, point3))
else:
    if (north == west):
        northeast = find_northeast(arr)
        if(pifagor(north, south) == pifagor(north, northeast)):
            print("Это квадрат")
            print("Сторона:", end = ' ')
            print(pifagor(north, south))
        else:
            print("Это прямоугольник")
            print("Сторона 1:", end = ' ')
            print(pifagor(north, south))
            print("Сторона 2:", end = ' ')
            print(pifagor(north, northeast))
    else:
        if(pifagor(north, west) == pifagor(north, east)):
            print("Это квадрат")
            print("Сторона:", end = ' ')
            print(pifagor(north, west))
        else:
            print("Это прямоугольник")
            print("Сторона 1:", end = ' ')
            print(pifagor(north, west))
            print("Сторона 2:", end = ' ')
            print(pifagor(north, east))
