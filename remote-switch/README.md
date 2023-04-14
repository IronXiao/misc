# RemoteSwitch

## 前言

在自动化测试中有一个很重要的项目就是开关机压力测试， 本例抽取出其中的开关控制部分做一个简单的示范。

## 1. 准备工作

### 1.1 购买并配置插座

购买可以通过云服务远程控制的插座，如：

https://item.m.jd.com/product/3000728.html?&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share&utm_user=plusmember&gx=RnFkwW9Zaz2Lz9TALzugzo--oy46ePgdsR0

下载相关受支援app 并给插座配网使能远程控制插座的开关状态。

### 1.2 抓取插座控制请求

本repo 适配的是[quantumultX](https://apps.apple.com/us/app/quantumult-x/id1443988620) 抓取的控制js 脚本，抓取步骤如下：

1. 进入`quantumultX` 点击右上角开启VPN 服务；
2. 点击右下角菱形开关进入`settings`；
3. 在`settings` 页面点击开启MitM 开关（首次执行需要按提示生成并安装证书，并到Iphone `Settings`->`General`->`About`-`Certificate Trust Settings`打开你安装的证书的信任开关）；
4. 在`Tools & Analysis` 栏目下点击进入`HTTP Capture`，在该页面点击右上角`http`图标开始抓包；
5. 后台切换到远程控制插座的专用app，做一下开关控制操作；
6. 切回`quantumultX` 的`HTTP Capture` 页面，在该页面点击右上角`http`图标停止抓包；
7. 在`Capture` 下方文件夹图标点击进入查看抓取到的请求，一般请求比较有规律，可以找到疑似匹配数据包进入通过`Text Viewer` 或者`JSON Viewer` 查看`RESPONSE BODY` 或`REQUEST BODY` 推测是否是控制插座开关的请求。可以进一步通过点击该请求详情页顶部`JS` 图标进入， 点击三角形播放按钮再次请求，如果此时可以控制插座开关，则为我们需要抓取的网络请求。点击右上角对勾√符号导出JS。

当然，用户也可以通过其他方式抓取控制请求参数，目前控制插座只需要三部分：

1. url；
2. headers；
3. post data。

可按下述格式写入文本（文本编码格式为utf-8)即可：

```python
url = 'some url'
headers = {'key1': 'value1', 'key2': 'value2' ... ... ... ...}
body = 'some body'
```

## 2. 代码执行

1. 安装依赖

   ```shell
   pip install requests
   ```

2. 脚本执行

   ```shell
   python3 main.py <switch config file path>
   ```

   如下是一个实例返回：

   ```shell
   $ python3 main.py 001.js
   {'status': 101, 'error': {'errorCode': 2004, 'errorInfo': '设备不在线', 'debugInfo': 'SMART业务错误  [设备不在线]', 'debugMe': 'SWC9K3NF1681457693453'}, 'result': None}
   ```

   (由于设备已关机，故无法做正确实操... ... ... ...)

   基于安全信息，提交代码版本已经随机抹除了部分数据，故得到的结果如下：

   ```shell
   {'result': {}, 'error': {'errorInfo': 'token invalid', 'errorCode': '401'}, 'status': 100}
   ```



