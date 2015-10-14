# -*- coding:utf-8 -*-

import math

from pychartdir import XYChart, Transparent, barLighting, Side


FONT = 'simsun.ttc'
COLOR = 0x6699bb
COLOR2 = 0xF48003

def simple():
    # The data for the bar chart
    data = [850000000, 150000000, 790000000, 210000000, 530000000, 310000000, 220000000]
    
    # The labels for the bar chart
    labels = ["8月5日", "8月6日", "8月7日", "8月8日", "8月9日", '8月10日', '8月11日']
    
    # Create a XYChart object of size 250 x 250 pixels
    c = XYChart(600, 400)
    c.addTitle('解析统计', FONT, 14)
    
    # Set the plotarea at (30, 20) and of size 200 x 200 pixels
    c.setPlotArea(80, 40, 500, 320)
    
    # Add a bar chart layer using the given data
    layer = c.addBarLayer(data, COLOR)
    layer.setAggregateLabelStyle(FONT, 12)
    
    # Set the labels on the x axis.
    c.xAxis().setLabels(labels)
    c.xAxis().setLabelStep(2, 1)
    c.xAxis().setLabelStyle(FONT, 12)
    
    # Output the chart
    c.makeChart("/temp/chart/simple.png")
    print 'done~'

def bar_label():
    # The data for the bar chart
    data = [85, 156, 179, 211, 123, 189, 166]
    
    # The labels for the bar chart
    labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    # Create a XYChart object of size 600 x 360 pixels
    c = XYChart(600, 360)
    
    # Set the plotarea at (70, 20) and of size 500 x 300 pixels, with transparent background and border
    # and light grey (0xcccccc) horizontal grid lines
    c.setPlotArea(70, 20, 500, 300, Transparent, -1, Transparent, 0xcccccc)
    
    # Set the x and y axis stems to transparent and the label font to 12pt Arial
    c.xAxis().setColors(Transparent)
    c.xAxis().setLabelStyle(FONT, 12)
    c.yAxis().setColors(Transparent)
    c.yAxis().setLabelStyle(FONT, 12)
    
    # Add a blue (0x6699bb) bar chart layer using the given data
    layer = c.addBarLayer(data, COLOR)
    
    # Use bar gradient lighting with the light intensity from 0.8 to 1.3
    layer.setBorderColor(Transparent, barLighting(0.8, 1.3))
    
    # Set rounded corners for bars
#     layer.setRoundedCorners()
    
    # Display labela on top of bars using 12pt Arial font
    layer.setAggregateLabelStyle(FONT, 12)
    
    # Set the labels on the x axis.
    c.xAxis().setLabels(labels)
    
    # For the automatic y-axis labels, set the minimum spacing to 40 pixels.
    c.yAxis().setTickDensity(40)
    
    # Add a title to the y axis using dark grey (0x555555) 14pt Arial Bold font
    c.yAxis().setTitle("Y-Axis Title Placeholder", FONT, 14, 0x555555)
    
    # Output the chart
    c.makeChart("/temp/chart/barlabel.png")
    print 'done~'

def percent():
    # The data for the bar chart
    data = [40, 15, 53.2]
    
    # The labels for the bar chart
    labels = ["8月5日", "8月6日", "8月7日"]
    
    # Create a XYChart object of size 250 x 250 pixels
    c = XYChart(600, 400)
    c.addTitle('解析统计', FONT, 14)
    
    # Set the plotarea at (30, 20) and of size 200 x 200 pixels
    c.setPlotArea(80, 40, 500, 320)
    
    # Add a bar chart layer using the given data
    layer = c.addBarLayer(data, COLOR)
    layer.setAggregateLabelStyle(FONT, 12)
    layer.setAggregateLabelFormat("{value}%")
    
    # Set the labels on the x axis.
    c.xAxis().setLabels(labels)
#     c.xAxis().setLabelStep(1, 1)
    c.xAxis().setLabelStyle(FONT, 12)
    
    c.yAxis().setLinearScale(0, 100, 20)
    c.yAxis().setLabelFormat("{value}%")
    
    # Output the chart
    c.makeChart("/temp/chart/percent.png")
    print 'done~'

def multi_percent():
    # 数据与标签
    data1 = [40, 15, 53, 66, 23, 48, 71, 55, 31, 48, 94, 57]
    data2 = [50, 35, 64, 22, 17, 67, 84, 53, 20, 78, 94, 61]
    labels = ['08-05', '08-06', '08-07', '08-08', '08-09', '08-10', '08-11', '08-12', '08-13', '08-14', '08-15', '08-16']
    
    # 数据与标签
#     data1 = [40, 15, 53]
#     data2 = [50, 35, 64]
#     labels = ['08-05', '08-06', '08-07']
    
    # 图片大小
    c = XYChart(600, 400)
    c.addTitle('解析统计', FONT, 14)
    
    # 绘图位置及大小，背景及边框透明，设置网格线颜色
    c.setPlotArea(80, 40, 500, 320, Transparent, -1, Transparent, 0xcccccc)
    
    # 图例, (left, top, is_vertical?? , font, font_size)
    c.addLegend(170, 22, 0, FONT, 10).setBackground(Transparent)
    
    # 坐标轴颜色，标签字体
#     c.xAxis().setColors(Transparent)
    c.xAxis().setLabelStyle(FONT, 12)
    c.yAxis().setColors(Transparent)
    c.yAxis().setLabelStyle(FONT, 12)
    
    # 多个数据集
    layer = c.addBarLayer2(Side)
    layer.addDataSet(data1, COLOR, "流量Cache率")
    layer.addDataSet(data2, COLOR2, "访问数Cache率")
    
    # 柱子上显示数据，并设置透明边框，柱子颜色的“光强度”介于 0.8 和 1.3 之间
    layer.setAggregateLabelStyle(FONT, 10)
    layer.setAggregateLabelFormat("{value}%")
    layer.setBorderColor(Transparent, barLighting(0.8, 1.3))
    
    # X轴标签，最多显示7个标签
    c.xAxis().setLabels(labels)
    c.xAxis().setLabelStep(math.ceil(len(data1) / float(7)))
    
    # 顶部空白
    c.yAxis().setTopMargin(30)
    
    # 最小值，最大值，步进。标签格式
    c.yAxis().setLinearScale(0, 100, 20)
    c.yAxis().setLabelFormat("{value}%")
    
    # Output the chart
    c.makeChart("/temp/chart/multi_percent.png")
    print 'done~'

if __name__ == '__main__':
    multi_percent()
