# wake-on-lan-by-google-assistant
通过Google assistant实现开启pc

其实要实现远程开机的方法有很多，比较常用的有通过魔术数据包进行远程唤醒，智能插座断电恢复唤醒，以及打电话（“妈！帮我开下电脑”）

本方法使用的是用google assitant语音通过ifttt使用魔术封包进行唤醒。至于为什么这样做，因为感觉挺有趣的。

首先需要有一台有公网IP的服务器，需要唤醒的设备有公网ip（唤醒端口做穿透也可以）。

然后将wakeonlan.py脚本保存到服务器内，并安装相关依赖

pip install flask

pip install wakeonlan

运行脚本 python3 wakeonlan.py &

脚本代码很简单，需要唤醒的电脑请确保能使用魔术封包唤醒，并且已经做好了接收魔术封包端口的映射。

然后是ifttt的相关设置。

下载好itfff后点击“创建”-“if this”添加-选择"Google assistant"-选择“say a simple phrase”-填写你想触发开机的语音如"wake on computer"(注意语言一定要选择对应的，不然无法识别）

点击“继续”后，在“then that”添加“webhooks”，点击“make a web request” 

举个栗子：如果你的服务器ip是11.11.11.1 ；需要唤醒的设备mac地址为XX.XX.XX.XX.XX.XX，需要唤醒设备的域名/ip为excample.com,需要唤醒的设备开放的端口为3389（为rdp默认端口，建议修改）。则URL栏填写http://11.11.11.1:5000/wakeonlan?mac=XX.XX.XX.XX.XX.XX&ip_address=excample.com&port=3389 Method选择GET，其他留空。

点击“继续”后“保存”

相关设置完成，对着手机说“ok Google” “wake on computer” 即可进行语音远程开机。
