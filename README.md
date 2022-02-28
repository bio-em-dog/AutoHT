# AutoHT v0.1
Automatic HT controll for JEOL JEM1400 electron microscope

v0.1  
Fixed procedure

- [AutoHT v0.1](#autoht-v01)
- [文件结构](#文件结构)
- [流程](#流程)
- [change](#change)
- [install and run](#install-and-run)
  - [source](#source)
  - [Executable file](#executable-file)
  - [Make executable file yourself](#make-executable-file-yourself)
    - [Method1: pipenv](#method1-pipenv)
    - [Method2: conda](#method2-conda)
    - [pyinstaller param](#pyinstaller-param)
- [Notes and Info](#notes-and-info)
  - [cv2](#cv2)
  - [pipenv](#pipenv)
  - [pyinstaller](#pyinstaller)
  - [icon](#icon)

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

# 流程
anaconda  
coding  
pyvenv - pyinstaller  
--or--  
conda - pyinstaller

# change
* before 2022: origin v0.1
* 2022.02.28: add log, cancal console quit confirm.

# install and run
## source

install:
```cmd
conda create -n autoht python=3.7
conda activate autoht
conda install pyautogui==0.9.50 pyperclip opencv-python
```
run:
```cmd
:: modify the bat file
call <your anaconda location>\Scripts\activate.bat <your env name>
:: example:
call %USERPROFILE%\anaconda3\Scripts\activate.bat autoht
```

you'd better modify log file path in `AutoHT.py` line 6

## Executable file

download from release  
unzip

## Make executable file yourself

### Method1: pipenv

```
cd <path to pyinstaller folder>
pipenv --python 3.7.11
pipenv shell
pip install pyperclip
pip install pyautogui==0.9.50
pip install opencv-python
pip install pyinstaller

pyinstaller -D -i "..\icon\dec.ico" "..\dec.py"
pyinstaller -D -i "..\icon\inc.ico" "..\inc.py"

```

** copy `dec` and `inc` image fodler to corresponding working folder **

manual remove pipenv in `%USERPROFILE%\.virtualenvs` if you do not need this pipenv any more.

### Method2: conda
```
conda activate autoht
conda install pyinstaller

pyinstaller -D -i "..\icon\dec.ico" "..\dec.py"
pyinstaller -D -i "..\icon\inc.ico" "..\inc.py"

```

** copy `dec` and `inc` image fodler to corresponding working folder **

### pyinstaller param

* -D 文件夹
* -F 单文件
* -w 隐藏console
* -i --icon icon


# Notes and Info
## cv2
cv2.matchTemplate(haystackImage, needleImage, cv2.TM_CCOEFF_NORMED)

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
pip install <模块>
pip install pyinstaller #打包的模块也要安装

pipenv graph #显示安装的环境
```

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
-w 隐藏console
--icon

## icon
win10 256 128 64 32 16
https://www.reddit.com/r/learnpython/comments/fks3oc/autoscaling_ico_with_pyinstaller/

生成各个大小合一的icon才能在生成后正常显示。同时注意同名文件的缩略图有缓存，在更换的icon后可能不显示，可以`1.`ctrl拖拽一个副本，或者`2.`删除`%localappdata%/Iconcache.db`，或者`3.`复制到全新目录

`Imagemagick`命令：  
`convert dec.png  -define icon:auto-resize=256,64,48,32,16 dec_icon.ico`