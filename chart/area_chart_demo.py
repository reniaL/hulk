# -*- coding:utf-8 -*-
from pychartdir import XYChart
import datetime
import math

FONT_SIMSUN = 'simsun.ttc' # 生成图片中的字体

def simple():
    # The data for the area chart
    data = [30, 28, 40, 55, 75, 68, 54, 60, 50, 62, 75, 65, 75, 89, 60, 55, 53, 35, 50, 66, 56, 48, 52,
        65, 62]
    
    # The labels for the area chart
    labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
        "16", "17", "18", "19", "20", "21", "22", "23", "24"]
    
    # Create a XYChart object of size 250 x 250 pixels
    c = XYChart(250, 250)
    
    # Set the plotarea at (30, 20) and of size 200 x 200 pixels
    c.setPlotArea(30, 20, 200, 200)
    
    # Add an area chart layer using the given data
    c.addAreaLayer(data)
    
    # Set the labels on the x axis.
    c.xAxis().setLabels(labels)
    
    # Display 1 out of 3 labels on the x-axis.
    c.xAxis().setLabelStep(3)
    
    # Output the chart
    c.makeChart("/temp/chart/area_simple.png")
    
    print 'done'

def custom():
    # The data for the area chart
    data = [30, 28, 40, 55, 75, 68, 54, 60, 50, 62, 75, 65, 75, 89, 60, 55, 53, 35, 50, 66, 56, 48, 52,
        65, 62, 28, 40, 55, 75, 68, 54, 28, 40, 55, 75, 68, 54]
    
    # The labels for the area chart
    d = datetime.datetime.now()
    labels = [(d + datetime.timedelta(minutes=5*i)).strftime('%m-%d %H:%M') for i in range(0, len(data))]
    
    c = XYChart(600, 400)
    c.addTitle('访问统计', FONT_SIMSUN, 14)
    c.setPlotArea(55, 40, 500, 320)
    
    c.addAreaLayer(data, 0x6699bb)
    c.xAxis().setLabels(labels)
    c.xAxis().setLabelStep(math.ceil(len(data) / float(8)))
    
    # Output the chart
    c.makeChart("/temp/chart/area_custom.png")
    
    print 'done'

if __name__ == '__main__':
    custom()