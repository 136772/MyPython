#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''

import sys


class WebServer(object):
    def __init__(self, host,post):
        self.host = host
        self.post = post

    def stop(self):
        print('Server is Stop...')

    def start(self):
        print('Server is start...')

    def restart(self):
        print('Server is restart...')
        self.stop()
        self.start()


def test_run(self,name):
    print('running....', name , self.host)


if __name__ == '__main__':

    server = WebServer('localhost', 333)
    server2 = WebServer('localhost', 333)

    # sys.argv 命令行输入函数   python *****.py start
    if hasattr(server, sys.argv[1]):  # 判断server里是否有sys.argv 这个方法
        func = getattr(server, sys.argv[1])  # 获取server.sys.argv 内存地址
        func()



    setattr(server,'run',test_run) #给server这个实例 绑定了一个test_run 只在本实例中 如server2没有
    server.run(server,'alex')      #调用实例的host 必须传入实例 才能调用


    delattr(server,'host')          #删除只能删除自己的 如 实例只能删除实例的属性
    print(server.host)

    delattr(WebServer,'start')
    print(server.start())

        # cmd_dic = {
        #     'start':server.start,
        #     'stop':server.stop,
        #     'restart':server.restart,
        # }
        # for i in cmd_dic.keys():
        #     print(i)
        #
        # if sys.argv[1] in cmd_dic:
        #     cmd_dic[sys.argv[1]]()
