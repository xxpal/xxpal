# 什么是多线程？并行/并发运行某个程序。(伪并行)
# 进程：一个应用程序就是一个进程，可以拥有1个或多个线程。
# 多线程可以显著提高程序的执行效率。
# 真正的并行：多核CPU，多路CPU。
import time
import datetime
import threading


# 第一种使用多线程的方式：
# 1. 让某个类继承自threading.Thread类。
# 2. 该类将需要多线程运行的代码放在run方法中。run方法是父类的方法，子类必须重写。
# 3. 实例化类时，直接通过类实例调用start()方法来实现多线程，start()方法会在父类中去调用run()。
class ThreadDemo(threading.Thread):
    def run(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print('线程: %s 正在执行：%s.' % (self.getName(), now))
        time.sleep(1)


# if __name__ == '__main__':
#     for i in range(20):
#         demo = ThreadDemo()
#         demo.start()


# 第二种方式使用多线程：直接使用Thread类进行实例化并传递要调用的方法给target参数作为构造参数，即可启动线程。
# 在传递被调用方法的参数时，必须用args参数来指定为元组的形式进行传递，且target参数所调用方法不能加圆括号。
class ThreadDemo2:
    def func_a(self, a1, a2):
        time.sleep(2)
        print('A方法正在执行 ==> %d\t\t' % (a1+a2))

    def func_b(self, b1):
        time.sleep(2)
        print('B方法正在执行 ==> %d\t\t' % b1)

    def func_c(self):
        time.sleep(1)
        print("C方法正在执行 ==> \t\t")


if __name__ == '__main__':
    demo = ThreadDemo2()
    for i in range(10):
        threading.Thread(target=demo.func_a, args=(100, 200)).start()

    for i in range(10):
        threading.Thread(target=demo.func_b, args=(-100, )).start()

    for i in range(10):
        threading.Thread(target=demo.func_c, args=()).start()

# 正常情况下，一个程序的运行，Python会自己启动一个线程来执行，这个线程称为“主线程”
# 可以通过获取线程的名称，来确认是否为多线程。
# 主线程并非一定是最后结束，需要看代码的实际情况，主线程一旦生成了子线程后，子线程再不受控。
# 线程并不是按严格的生成顺序来执行的，完全依赖于CPU的心情。
# 线程什么时候结束：每一个线程将要执行的代码执行完成后就会结束。
# 只要一个进程中还有一个线程活着，则进程就不会结束。
