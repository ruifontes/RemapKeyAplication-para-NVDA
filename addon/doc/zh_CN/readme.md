# 重新映射 Application 键


## 信息
* 作者：Rui Fontes，改编自 Héctor J. Benítez Corredera 的作品
* 更新于 07/01/2024
* 下载[稳定版][1]
* 兼容性：NVDA 2019.3 及更高版本


## 介绍
适用于那些没有 Application 键或 Application 键无法使用的计算机的简单插件。
其在 Windows 11 build 22621 及更高版本的文件资源管理器中也很有用，因为它允许为 Shift+Application 组合键分配一个快捷键，用于显示完整的上下文菜单。从此 Windows 版本起，Application 键仅显示上下文菜单的精简版本。
有必要分配我们想要替换 Application 键的按键或按键组合。
在 NVDA 菜单/选项/按键与手势.../重新映射 Application 键中，可以分配想要的按键组合。


## 注意
当分配组合键或单个按键时，我们必须考虑到该按键不会在任何应用程序中使用。
如，Ctrl + 向下箭头适用于大多数系统，但在 Google Chrome 中会出现错误，不允许访问上下文菜单。


## 译者及合作者：
* 法语：Rémy Ruiz
* 俄语：Valentin Kupriyanov
* 乌克兰语：VovaMobile
* 土耳其语：Umut Korkmaz


## 更改日志


### 版本 2023.09.30
* 2023.09.26 NVDA兼容性扩展至2024.1版本；
* 现在还可以将按键分配给 Shift+Application键；


### 版本 2023.09.02
* 现在由 Rui Fontes 和 NVDA 葡萄牙团队维护
* 现在代码是基于英文的。


### 版本 0.4
* 添加了俄语、乌克兰语和土耳其语翻译。
* 添加了与 NVDA 2023.1 的兼容性


### 版本 0.3
* 将调用 Application 键的方式从本机 NVDA 更改为本机 Windows，因为这是一种更可靠、更直接的方法。
* 添加了鼠标左键和右键单击焦点的可能性。
我们必须在按键与手势对话框中分配相应的组合键。
当我们执行该动作时，鼠标会移动到焦点处并进行相应的单击，并且会听到声音表明单击已执行。


### 版本 0.2
* 与 NVDA 2022 兼容


### 版本 0.1.5
* 修复了 NVDA 插件中的问题。
* 添加了法语翻译。


### 版本 0.1
* 初始版本。

[1]:https://github.com/ruifontes/RemapKeyAplication-para-NVDA/releases/download/2024.01.07/remapApplicationsKey-2024.01.07.nvda-addon

