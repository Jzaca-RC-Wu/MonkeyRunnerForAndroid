 # -*- coding: utf-8 -*-

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
import numpy
# import monkeyUtils as mUtils

class runner():

    def __init__(self):
        try:
            self.device = MonkeyRunner.waitForConnection(5.0,"cfa923d4")
        except:
            print ('DeviceConnectException: Device connect except!!')

    def getdisplay(self):
        height = self.device.getProperty('display.height')
        width = self.device.getProperty('display.width')
        density = self.device.getProperty('display.density')
        return width, height, density

    def swipe(self, x_ratio, y_ratio, direction=None):
        display = self.getdisplay()
        if not direction or direction.upper() == 'VERTICAL':
            self.device.drag((x_ratio * display[0], y_ratio * display[1]), ((1 - x_ratio) * display[0], y_ratio * display[1]))
        elif direction.upper() == 'HORIZONTAL':
            self.device.drag((x_ratio * display[0], y_ratio * display[1]), (x_ratio * display[0], (1 - y_ratio) * display[1]))
        # else:
        #     self.device.drag((x_ratio * display[0], y_ratio * display[1]),((1-x_ratio) * display[0], (1 - y_ratio) * display[1]))
        MonkeyRunner.sleep(0.1)

    def testswipebanner(self):
        # self.display = runner.getdisplay()
        for i in range(1000):
            self.device.swipe(0.3, 0.3)

# Home_Hot
Home_tab = {
    "Banner":{"x":(0.5,0,1),"y":(0.21,0.17,0.37)},
    "QuickButton":{"initial":(0.16,0.454),"interval":0.226},
    "Column":{"living":(0.92,0.596)}
}

#Item_List
List = {
    "Item":{"initial":(0.25,0.2),"interval":(0.5,0.23)}
}

Room_Game = {
    "Button_back":{"vertical":(0.06,0.07),"horizontal":()}
}
#click
def click(device,position):
    device.touch(position[0], position[1], MonkeyDevice.DOWN)
    device.touch(position[0], position[1], MonkeyDevice.UP)

#swipe Banner
def swipeBanner(device,number= None,direction = None):
    if not number:
        number = 1
    if not direction or direction.upper == 'LEFT':
        for i in range(number):
            device.drag((900, 400),(360, 400), 0.2, 3)
    elif direction.upper == "RIGHT":
        for i in range(number):
            device.drag((360, 400), (900, 400), 0.2, 3)
    elif direction.upper == "UP":
        for i in range(number):
            device.drag((0.5,0.75),(0.5,0.25),0.2,3)
    else:
        for i in range(number):
            device.drag((0.5,0.25),(0.5,0.75),0.2,3)

#get every item position
def getItemPosition(i):
    position = List['Item']['initial']
    row = i // 2
    remainder = i % 2
    print(row,remainder)
    x_ratio = position[0] + remainder * List["Item"]["interval"][0]
    y_ratio = position[1] + row * List["Item"]["interval"][1]
    x_axis = int(x_ratio * width)
    y_axis = int(y_ratio * height)
    print(x_axis,y_axis)
    return (x_axis,y_axis)

#to-do
def getQuickButtonPosition(i):
    y_axis = int(Home_tab["QuickButton"]['initial'][1] * height)
    x_axis = int(((Home_tab["QuickButton"]["initial"][0]) + i * Home_tab["QuickButton"]['interval']) * width)

if __name__ == "__main__":
    # run = runner()
    device = MonkeyRunner.waitForConnection(5.0, "cfa923d4")
    #get device display attribution
    width = float(device.getProperty("display.width"))
    height = float(device.getProperty('display.height'))
    density = float(device.getProperty('display.density'))

    startActivity = 'com.longzhu.tga/.clean.splash.SplashActivity'
    mainActivity = 'com.longzhu.tga/.clean.main.MainActivity'
    device.startActivity(component = startActivity)
    MonkeyRunner.sleep(8)
    print(device.getProperty("am.current.comp.package"))
    # print type(device.getProperty("am.current.comp.package"))
    print(device.getProperty('am.current.comp.class'))
    # print(device.getProperty('am.current.categories'))

    # print device.getProperty('display.width')
    # display = (device.getProperty('display.width'),device.getProperty('display.height'),device.getProperty('display.density'))
    # print (int(device.getProperty('display.width')),device.getProperty('display.height'),device.getProperty('display.density'))

    # swipeBanner(device,10,"Left")
    # swipeBanner(device,11,"Right")

    y_axi = int(Home_tab["QuickButton"]['initial'][1] * height)
    x_axi = int(((Home_tab["QuickButton"]["initial"][0]) + 2 * Home_tab["QuickButton"]['interval']) * width)
    print (x_axi,y_axi)
    # click(device, (x_axi, y_axi))
    # MonkeyRunner.sleep(5)
    # x_p1 = int(List['Item']['initial'][0]*width)
    # y_p1 = int(List['Item']['initial'][0]*height)
    # click(device,(x_p1,y_p1))
    # click(device,getItemPosition(0))
    # click(device,getItemPosition(3))

    position = numpy.array(list(Room_Game['Button_back']['vertical']))*numpy.array([width,height])
    print (position)


