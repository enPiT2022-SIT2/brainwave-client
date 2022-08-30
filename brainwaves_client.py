import atexit
import numpy as np
import socket
import sys
import time
import argparse

# socket
client = None

#コマンドライン引数受取
parser = argparse.ArgumentParser(description = 'add two integer')
parser.add_argument('--id',type=float,default=1,help='student id')
parser.add_argument('--sleep',type=float,default=1,help='sleep or awake')
parser.add_argument('--host',type=str,default='localhost',help='host')
parser.add_argument('--port',type=int,help='port')

args = parser.parse_args()

# socket切断
def disconnect():
    global client
    if client:
        client.close()
    print("atexit function called")

# socket接続
def connect(host, port):
    global client
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        # 接続に成功したらsocketを返す
        return client
    except Exception as err:
        print(err)
        # 接続に失敗したらNoneを返す
        return None

def main():
    global client
    # localhost:33400に接続
    client = connect(args.host,args.port)
    if not client:
        # 接続に失敗したらプログラムを終了する
        sys.exit()
    while True:
        client.sendall(np.array([args.id, 1, 1, args.sleep],dtype=np.float64))
        # 1s待機
        time.sleep(1)

# プログラム終了時にdisconnect関数を実行する
atexit.register(disconnect)

# main関数をentry pointとして実行する
if __name__ == "__main__":
    main()
