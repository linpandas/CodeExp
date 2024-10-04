# CodeStack

## 简介

> **心在远方，路在脚下；仰望星空，脚踏实地。**

本项目包含了我刷过的LeetCode题、面试常考题，大部分题目由python求解，记录在此以便复习。

## 使用说明

1. 在VSCode上下载ccagml的LeetCode插件。ccagml的插件包含了每日一题、多种经典题目合集、测试用例debug等功能，比官方的好用。

2. 在浏览器打开LeetCode网页，登录自己的账号；键盘按F12，打开开发者模式；在console中输入`javascript:document.cookie`，得到Cookie；截取Cookie中csrftoken="xxx"中的xxx，LEETCODE_SESSION="yyy"中的yyy，注意不包含分号。

3. 选中LeetCode插件，选择第二个“Sign In”图标，点击第二个“LeetCode Cookie登录方式，将step2中得到的csrftoken和LEETCODE_SESSION值填入，登录即可。

## 项目结构

* LeetCode题在[LeetCode](./LeetCode/)下，里面不分题型地保存了我刷过的LeetCode题。

* 面试常考题在[Interview](./Interview/)下，里面包含了面试常考的非LeetCode手撕题目。

* 题目的组织在[Notebooks](./Notebooks/)下，里面有各种题目合集的Markdown文件，方便复习，推荐从这里开始浏览。