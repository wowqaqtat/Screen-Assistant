# 友好的屏保软件

> Screen Assistant是一款用户友好的屏保软件，它内置了若干精美的屏保，并且允许用户自定义图片文件夹的路径。该软件还具备保护用户隐私的功能，防止他人窥视用户的电脑，同时避免因误触屏幕带来不必要的麻烦。
>
> 该软件适合各种场合使用，可以用于工作、学习、娱乐等多种场景。无论是在办公室、学校、还是家里的电脑上使用，都可以让用户轻松地选择自己喜欢的图片作为屏保。

## 功能设计

- [X] 支持自定义图片文件夹路径
- [X] 支持本地保存路径配置
- [X] 支持全屏显示，按键退出
- [X] 自带默认图片
- [X] ……

<img src="https://raw.githubusercontent.com/wowqaqtat/Screen-Assistant/main/docs/流程图.png" height="500px">

## 界面截图

`<img src="https://raw.githubusercontent.com/wowqaqtat/Screen-Assistant/main/image/image (1).png" height="250px"><img src="https://raw.githubusercontent.com/wowqaqtat/Screen-Assistant/main/image/image (1).jpg" height="250px">``<img src="https://raw.githubusercontent.com/wowqaqtat/Screen-Assistant/main/image/image (2).jpg" height="250px"><img src="https://raw.githubusercontent.com/wowqaqtat/Screen-Assistant/main/image/image (3).jpg" height="250px">``<img src="https://raw.githubusercontent.com/wowqaqtat/Screen-Assistant/main/image/image (4).jpg" height="250px"><img src="https://raw.githubusercontent.com/wowqaqtat/Screen-Assistant/main/image/image (5).jpg" height="250px">`

**相关壁纸：**

[高清壁纸 | 初音未来高清壁纸 - AI](https://www.bilibili.com/read/cv27592484/)

[高清壁纸 | 可爱猫娘高清壁纸 - AI](https://www.bilibili.com/read/cv27592487/)

[高清头像 | 星空、星球与宇宙 - AI](https://www.bilibili.com/read/cv27648164/)

## 快速开始

**如果你不需要自行开发，可以直接 [下载](https://www.bilibili.com/ "安装包下载") 作者打包好的 `exe` 文件，并忽略下面的配置。**

1. 确保已安装Python环境，作者使用的是 ``python 3.8.10`` .

使用pip安装所需的依赖库，例如 ``pip install PyQt5``

也可以使用如下命令一键安装依赖包： ``pip install -r requirements.txt``

2. 执行命令 `python main.py` 启动程序 .
3. 执行命令 `pyinstaller -F -i icon.ico main.py --noconsole` 打包程序 .
4. 更多配置如下：

配置文件 ``config.ini``：

```
[settings]
path = ./image
```

> 如果想重新选择文件夹，可以手动修改配置文件，文件编码为 `ANSI` 。如果想恢复默认设置，可以直接删除配置文件 `config.ini` .

生成ui：
``pyuic5 -o ui.py ui.ui``

## 技术要点

- PyQt5 库：这是一个用于创建桌面应用程序的库。它提供了许多功能，如窗口管理、控件、事件处理等。
- 使用 PyQt5 的窗口管理功能，创建、最大化、最小化窗口。
- 使用 Qt Designer 创建一个简单的界面。

## 开发参考

开发者可以根据实际需要进行优化：

- [ ] 密码解锁
- [ ] 面部识别解锁
- [ ] 定时启动
- [ ] 界面中显示时间
- [ ] ……

## 联系我们

- 本程序基于 [MIT](https://opensource.org/licenses/MIT) 许可证开源。
- 本程序不定时更新，如果大家在使用的过程中，发现任何bug或有不错的想法，欢迎提出交流。
- 源代码：[https://github.com/wowqaqtat/Screen-Assistant](https://github.com/wowqaqtat/Screen-Assistant)
- 视频讲解：[bilibili](https://space.bilibili.com/494053707)
- 邮箱：[help@haodukeji.cn](mailto:help@haodukeji.cn)
