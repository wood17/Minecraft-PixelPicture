#本程序由wood秋木制作
print("本程序由wood秋木制作，欢迎使用数据转指令！")
数据 = open(input("数据文件"),"r").read()
宽 = int(数据[0 : 3])
长 = int(数据[3 : 6])
指令文件 = input("指令文件")
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
i = 6
宽i = 0


if(宽 * 长 != len(数据) - 6):
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