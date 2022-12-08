#本程序由wood秋木制作
from PIL import Image
print("本程序由wood秋木制作，欢迎使用图片转指令！")
#获取输入
图像文件 = input("图像文件")
宽 = int(input("宽"))
长 = int(input("长"))
指令文件 = input("指令文件")

#图片转成数据
色彩对照表 = {
"aaa":1,
"aab":2,
"aba":3,
"abb":4,
"baa":5,
"bab":6,
"bba":7,
"bbb":8
}
def 处理色值(色值):
	处理后色值 =  "a"
	if(色值 >= 128):
	    处理后色值 = "b"
	return 处理后色值
数据 = ""
图像 = Image.open(图像文件)
图像 = 图像.resize((长,宽), Image.Resampling.LANCZOS)
图像 = 图像.convert(mode="RGB")
图像像素 = 图像.load()
#图像.save("0.png")
for y in range(图像.size[1]):
    for x in range(图像.size[0]):
        像素色 = 图像像素[x,y]
        像素色R = 处理色值(像素色[0])
        像素色G = 处理色值(像素色[1])
        像素色B = 处理色值(像素色[2])
        del 像素色
        像素色 = 色彩对照表[像素色R+像素色G+像素色B]
        数据 = 数据+str(像素色)
        
        
#数据转成指令
颜色方块 = {
"1":"concrete 15",
"2":"concrete 11",
"3":"concrete 5",
"4":"concrete 3",
"5":"concrete 14",
"6":"concrete 2",
"7":"concrete 4",
"8":"concrete 0"
}
指令前缀 = ""
最终指令 = ""
i = 0
宽i = 0


if(宽 * 长 != len(数据)):
    print("您输入的数据存在问题")
    exit()


while (宽i < 宽):
    宽i = 宽i + 1
    长i = 0
    while (长i < 长):
        长i = 长i + 1
        i = i + 1
        本次方块 = 颜色方块[str(数据[i-1])]
        本次命令 = 指令前缀 + "setblock ~" + str(长i) + " ~" + str(宽 - 宽i) +  " ~ " + 本次方块
        if(i != len(数据)):
            本次命令 = 本次命令 + "\n"
        最终指令 = 最终指令 + 本次命令
open(指令文件+"_all.mcfunction","w").write(最终指令)

未拆分文件 = 指令文件
拆分行数 = 10000
未拆分 = open(未拆分文件+"_all.mcfunction","r").readlines()
行数 = len(未拆分)
拆分后文件数 = 行数 // 拆分行数
if(行数 / 拆分行数 > 行数 // 拆分行数):
    拆分后文件数 = 拆分后文件数 + 1
文件数i = 0
行数i = 0
while (文件数i < 拆分后文件数):
    文件数i = 文件数i + 1
    拆分行 = 文件数i - 1
    open(未拆分文件+"_"+str(文件数i)+".mcfunction","w").write("".join(未拆分[拆分行 * 拆分行数 : 文件数i * 拆分行数]))
    print(未拆分文件+"_"+str(文件数i)+".mcfunction")
#本程序由wood秋木制作