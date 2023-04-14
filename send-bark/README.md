# 发送Bark 消息

## 准备工作

一部IOS 手机并安装激活[BARK](https://apps.apple.com/us/app/bark-customed-notifications/id1403753865)，记录获取到的`api key`。

## 发送消息

1. 安装依赖

   ```shell
   pip install requests
   ```

2. 测试消息发送

   ```shell
   python3 send_bark.py <bark api key> <bark content>
   ```

   - 发送基本消息（仅有标题）

     ```shell
     python3 ./send_bark.py "9PFhx???AKujGY" "Test Msg"
     ```

   - 发送消息（带标题和详情）

     ```shell
     python3 ./send_bark.py "9PFhx???AKujGY" "Test Msg/This a test message"
     ```

   - 指定消息铃声

     ```shell
     python3 ./send_bark.py "9PFhx???AKujGY" "Test Msg/This a test message?sound=minuet"
     ```

   更多高级玩法参考`BARK` app 中`Service` 栏目构造args 即可。

