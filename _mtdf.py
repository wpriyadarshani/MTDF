
from PIL import Image
import random
import numpy
import pdb

import array
import logging

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot

import math

from matplotlib.patches import Rectangle




class Clustering(object):
  
    def __init__(self, image, image_GT):
        #save image names
        self.org_image = image
        self.GT_image = image_GT

        #save pixel maps
        self.org_pixel_map = []
        self.GT_pixel_map = []
        self.output_pixel_map = []
        self.output_image = 0
       
        self.village_pixels = []
        self.village_pixel_location = []


        self.non_village_pixels = []
    

    def openImages(self):
        #load pixels
        self.GT_pixel_map = Image.open(self.GT_image).load()
        self.org_pixel_map = Image.open(self.org_image).load()

        self.output_image = Image.open(self.org_image)
        self.output_pixel_map = self.output_image.load()

        print "GT ", self.GT_pixel_map[0,0]
        print "Org ", self.org_pixel_map[0,0]



    def get_village_pixels(self):
        #select only village pixels for the clustering
        for i in range(200):
            for j in range(200):
               
                #match with exact white pixel
                if self.calcDistance(self.GT_pixel_map[i,j], self.GT_pixel_map[126,63]) == 0.0: 


                    if (self.org_pixel_map[i,j][0]-53)<10.0 and (self.org_pixel_map[i,j][1] - 53)<10.0:
                        print "catched ", self.org_pixel_map[i,j], i, j

                    elif (self.org_pixel_map[i,j][0]-76)<10.0 and (self.org_pixel_map[i,j][1] - 76)<10.0:
                        print "catched ", self.org_pixel_map[i,j], i, j
                    else:
                        #get the original image village pixel values
                        self.village_pixels.append(self.org_pixel_map[i,j])
                        #get the village village pixel locations
                        self.village_pixel_location.append((i,j))

                else:
                    self.non_village_pixels.append(self.org_pixel_map[i,j])

        return self.village_pixels, self.non_village_pixels

    def calcDistance(self, a, b):
        dis1 = pow((a[0]-b[0]),2.0)
        dis2 = pow((a[1]-b[1]),2.0)
        dis3 = pow((a[2]-b[2]),2.0)
        dis4 = pow((a[3]-b[3]),2.0)

        sumation = dis1 + dis2 + dis3 + dis4
        result = numpy.sqrt(sumation)
        return result


class MTDF(object):
    def __init__(self, minority):
        self.minority = minority

    def mean(self):
        print self.minority[0]

        sum = [0,0,0,0]

        size = len(self.minority)

        for i in range(size):
            sum[0] = sum[0] + self.minority[i][0]
            sum[1] = sum[1] + self.minority[i][1]
            sum[2] = sum[2] + self.minority[i][2]
            sum[3] = sum[3] + self.minority[i][3]


        mean = (sum[0]/size, sum[1]/size, sum[2]/size, sum[3]/size)

        print mean

        return mean

    def variance(self):





        


if __name__ == "__main__":
    c = Clustering("T5.png", "GT_T5.png")
    c.openImages()
    village_pixels, non_village_pixels = c.get_village_pixels()


    m = MTDF(village_pixels)
    m.variance()

   


