import socket
import threading
import wave
import pyaudio
import time

hostname = socket.gethostname()
hostip = '192.168.43.61'

port = 65432

def stream():
    BUFF_SIZE = 65536
    s_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s_socket.setsocketopt(socket.SQL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
    s_socket.bind((hostip,(port)))

    CHUNK = 10*1024
    wf = wave.open("hello.wav")
    p = pyaudio.PyAudio()

    print('server listening at',(hostip,(port)),wf.getframerate())

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),channels = wf.getnchannels(),rate = wf.getframerate(),input = True,frames_per_buffer=CHUNK)

    data = None
    sample_rate = wf.getframerate()

    while True:
        msg,client_addr = server_socket.recvfrom(BUFF_SIZE)
        print("got connection from ",client_addr,msg)

        while True:
            data = wf.readframes(CHUNK)
            server_socket.sendto(data,client_addr)
            time.sleep(0.8*CHUNK/sample_rate)

t = threading.Thread(target=stream,args=())
t.start()


