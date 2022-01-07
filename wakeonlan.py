from flask import Flask,request
from wakeonlan import send_magic_packet

app = Flask(__name__)

@app.route('/wakeonlan')
def wakeonlan():
    if request.method == 'GET':
        mac = request.args.get('mac')#以json形式发送
        ip_address = request.args.get('ip_address')
        port = request.args.get('port')
        print(mac,ip_address,port)
    send_magic_packet(mac,ip_address=ip_address,port=int(port))
    return 'ok'


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)
