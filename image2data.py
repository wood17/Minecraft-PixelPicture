#本程序由wood秋木制作
from PIL import Image
print("本程序由wood秋木制作，欢迎使用图片转数据！")
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
图像文件 = input("图像文件")
宽 = int(input("宽"))
长 = int(input("长"))
数据文件 = input("数据文件")
数据 = str(宽).zfill(3) + str(长).zfill(3)
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
open(数据文件,"w").write(数据)
#本程序由wood秋木制作
