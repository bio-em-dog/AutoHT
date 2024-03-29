# AutoHT v0.2
Automatic HT controll for JEOL JEM1400 electron microscope

v0.1: Fixed procedure  
v0.2: Optimize work flow. Make it more flexiable for different EM UI.  

# 文件结构
```
├── dec                     # 降压识别的位置
├── icon                    # 升降压的icon
├── README.md               # 说明文档
├── inc                     # 升压识别的位置
├── pyinstaller             # pipenv的执行目录
│    └── pipfile
├── RAW_UI                  # 整张UI
├── AutoHT.py
├── dec.py
├── inc.py
└── README.md
```

# 结构

- AutoHT
  - 主py (放在一个文件夹里，这样pyinstaller出来后路径一致)
  - 参数 flowname
  - def findlocation(), click, judgeclick, input
- flow
  - flow1
    - 图
    - flow1.lst:
      - 循    环：Loop 1,End
      - 等    待: Wait, time
      - 点    击：Click, img, LR , times ,shiftx ,shift y
      - 判断点击：Judgeclick, img1, img2, LR , times ,shiftx ,shift y
      - 输    入：Input,jobtype, value
      - 键盘： Key 
      - 挂起： Halt


  - flow2
  - ...

## pipenv
https://zhuanlan.zhihu.com/p/57674343


```
cd <path to pyinstaller folder>
#建立虚拟环境
pipenv --python 3.7.11 # 一定要在project dir中执行
# pipenv新建的虚拟环境统一放在`%USERPROFILE%\.virtualenvs`, 在特定目录下运行pipenv shell时,pipenv会自动在虚拟环境目录下搜索以当前目录名称开头的虚拟环境目录.
#进入虚拟环境
pipenv shell
#安装模块
pip install <.py里面用到的模块>


pip install pyperclip
pip install pyautogui==0.9.50
pip install opencv-python==3.4.10.37
pip install pyscreeze==0.1.29

pipenv graph #显示安装的环境
#打包的模块也要安装
pip install pyinstaller
#开始打包
pyinstaller -Fw E:\test\url_crawler.py
```
## 32bit x86 版本
在 Support PC 的 Hyper V 中安装虚拟机  
安装32位的python3.7.8 x86，其他相同操作  

## pyinstaller

http://c.biancheng.net/view/2690.html


```cmd
:: pipenv prompt
pipenv shell  :: in pyinstaller folder
pyinstaller -D -i "..\icon\dec.ico" "..\dec.py"
pyinstaller -D -i "..\icon\inc.ico" "..\inc.py"
```

-D 文件夹
-F 单文件
-w 隐藏consel
--icon

## icon
win10 256 128 64 32 16
https://www.reddit.com/r/learnpython/comments/fks3oc/autoscaling_ico_with_pyinstaller/

生成各个大小合一的icon才能在生成后正常显示

注意缩略图有缓存，可以ctrl拖拽一个副本看看，或者删除`%localappdata%/Iconcache.db`

`Imagemagick`命令：  
`convert dec_waifu2x_art_scale_tta_1.png  -define icon:auto-resize=256,64,48,32,16 my_icon.ico`


### 
cv2.matchTemplate(haystackImage, needleImage, cv2.TM_CCOEFF_NORMED)
