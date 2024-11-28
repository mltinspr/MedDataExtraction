# MedDataExtraction
[第一个链接](https://code.nhsa.gov.cn/jbzd/public/dataWesterSearch.html)的数据获取方法思路
## 1.进入网页，鼠标右键任意位置打开检查，进入开发者模式。
![image](https://github.com/user-attachments/assets/9602d5ca-c866-4d7d-a8a6-0ea36f6125e4)
## 2.点击网络选项。如果没有，点击右边“+”号添加该工具
![image](https://github.com/user-attachments/assets/0675425c-2cba-43e9-b12a-f51daccf3836)
## 3.在此界面，选择文档选项，并刷新该网页
![image](https://github.com/user-attachments/assets/4add0690-626f-4f0e-bdd2-b94deed1c5f7)
## 4.刷新后，应该会出现一个名为toStdIcdDetail.html文件，点击该文件查看
![image](https://github.com/user-attachments/assets/51791a96-43b7-4d8a-9930-774306a3fc9e)
## 5.点击预览，便可以看到由真实接口发送的代码，但经尝试仍然无法正常爬取数据。
![image](https://github.com/user-attachments/assets/f1636aba-43d4-4235-abf9-33e38af14e28)
## 6.转换一下思路，右键文件名，选择另存为，将该文件保存到本地。
![image](https://github.com/user-attachments/assets/1ddf8848-8acb-4eae-a6d6-6a2e44d8e664)
## 7.此时我们在本地打开该文件，可以发现每一行就是一个完整的数据！于是可以考虑将数据放置本地，在本地对这些html文件进行处理。
![image](https://github.com/user-attachments/assets/05f860b2-8a48-4e91-8aa9-9e33fea3fc21)
## 8.重试1-5步，在第5步时，点击左边2-22章按钮，可以发现会出现新的数据。按照上述方法将它们保存到本地。
![image](https://github.com/user-attachments/assets/b82c86e7-047a-4cde-9582-a4fbc511aa14)
## 9.之后在本地打开这些文件，ctrl+A全选，在本项目data文件夹下新建chapterX.txt文件，X为章节数
![image](https://github.com/user-attachments/assets/d8337e45-4f43-4438-8b98-9db641bfe101)
## 10.运行main.py文件，便可以得到处理好的数据。具体数据如何保存再做商讨
![image](https://github.com/user-attachments/assets/86b1e5f2-4898-4fa7-81f2-3d287e4c3ad1)




