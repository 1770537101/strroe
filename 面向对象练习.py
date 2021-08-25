#水杯
class cup:
    height = 0
    vol = 0
    color = ""
    mate = ""

    def hold(self,ml):
        print(self.mate,"材质的水杯能存放液体！现在杯里有",ml,"毫升水")

c = cup()

c.height = 20
c.vol = 500
c.color = "透明"
c.mate = "玻璃"

c.hold(400)


#电脑
class diannao:
    __pinmu = ""
    __jiag = ""
    __cpu = ""
    __neicun = ""
    __daiji = ""

    def setpinmu(self,pinmu):
        if pinmu >= "50英寸" or pinmu <= "0英寸":
            print("不可能，绝对不可能！")
        else:
            self.__pinmu = pinmu
    def getpinmu(self):
        return self.__pinmu

    def setjiag(self,jiag):
        self.__jiag = jiag
    def getjiag(self):
        return self.__jiag

    def setcpu(self,cpu):
        self.__cpu = cpu
    def getcpu(self):
        return self.__cpu

    def setneicun(self,neicun):
        self.__neicun = neicun
    def getneicun(self):
        return self.__neicun

    def setdaiji(self,daiji):
        self.__daiji = daiji
    def getdaiji(self):
        return self.__daiji


    def kuaihuo(self,dazi):
        print("正在用",self.__pinmu,"的电脑",dazi)


    def youxi(self,yx):
        print("正在用",self.__pinmu,"的电脑,玩",yx)


    def kansp(self,kan):
        print("正在用",self.__pinmu,"的电脑看",kan)


    def zhanshi(self):
        print("这台笔记本电脑屏幕大小",self.__pinmu,"价格为",self.__jiag,"cpu型号是",self.__cpu,"它有着",self.__neicun,"运行内存","它可以待机",self.__daiji)



m = diannao()


#m.pinmu = "15英寸"
m.setpinmu("15英寸")
#m.jiag = "5k"
m.setjiag("5k")
#m.cpu = "2.60ghz"
m.setcpu("2.60GHz")
#m.neicun = "8G"
m.setneicun("8G")
#m.daiji = "1天"
m.setdaiji("1天")


m.kuaihuo("打字")
m.youxi("吃鸡")
m.kansp("动漫")
m.zhanshi()



















