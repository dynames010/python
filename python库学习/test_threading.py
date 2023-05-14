import threading
import time
#多进程
import multiprocessing

def show_info():
    for i in range(5):
        print("test:",i)
        time.sleep(0.5)

def show1_info(num):
    for i in range(num):
        print("test1:",i)
        time.sleep(0.5)

if __name__ == '__main__':
    showinfo_process = multiprocessing.Process(target=show_info)
    showinfo1_process = multiprocessing.Process(target=show1_info,kwargs={'num':7})
    showinfo_process.start()
    showinfo1_process.start()
    # sub_thread = threading.Thread(target=show_info)
    # sub1_thread = threading.Thread(target=show1_info)
    # sub_thread.start()
    # sub1_thread.start()
    # print("over")