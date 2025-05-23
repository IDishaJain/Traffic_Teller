from random import randint
import time

class Car:
    tracks = []

    def __init__(self, i, xi, yi, max_age):
        self.i = i
        self.x = xi
        self.y = yi
        self.tracks = []
        self.done = False
        self.state = '0'
        self.age = 0
        self.max_age = max_age
        self.dir = None
        self.height = None  # Added height attribute
        self.width = None   # Added width attribute

    def getTracks(self):
        return self.tracks

    def getId(self):  # For the ID
        return self.i

    def getState(self):
        return self.state

    def getDir(self):
        return self.dir

    def getX(self):  # for x coordinate
        return self.x

    def getY(self):  # for y coordinate
        return self.y

    def updateCoords(self, xn, yn, wn=None, hn=None): # Added width and height to update
        self.age = 0
        self.tracks.append([self.x, self.y])
        self.x = xn
        self.y = yn
        if wn is not None:
            self.width = wn
        if hn is not None:
            self.height = hn

    def setDone(self):
        self.done = True

    def timedOut(self):
        return self.done

    def going_UP(self, mid_start, mid_end):
        if len(self.tracks) >= 2:
            if self.state == '0':
                if self.tracks[-1][1] < mid_end and self.tracks[-2][1] >= mid_end:
                    self.state = '1'
                    self.dir = 'up'
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def going_DOWN(self, mid_start, mid_end):
        if len(self.tracks) >= 2:
            if self.state == '0':
                if self.tracks[-1][1] > mid_start and self.tracks[-2][1] <= mid_start:
                    self.state = '1'
                    self.dir = 'down'
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def age_one(self):
        self.age += 1
        if self.age > self.max_age:
            self.done = True
        return True

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

#Class2

class MultiCar:
    def __init__(self, cars, xi, yi):
        self.cars = cars
        self.x = xi
        self.y = yi
        self.tracks = []
        self.done = False