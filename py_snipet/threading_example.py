#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   Date    :   17/3/31 下午5:58
#   Desc    :   获取子线程异常

import sys
import Queue
import threading


class SampleThread(threading.Thread):
    def run(self):
        raise Exception('An error occured here.')


def sample_main():
    try:
        thread_obj = SampleThread()
        thread_obj.start()
        thread_obj.join()
    except Exception as e:
        print e
        print 'catch that'


class ExcThread(threading.Thread):

    def __init__(self, bucket):
        super(ExcThread, self).__init__()
        self.bucket = bucket

    def run(self):
        try:
            raise Exception('An error occured here.')
        except Exception:
            self.bucket.put(sys.exc_info())


def main():
    bucket = Queue.Queue()
    thread_obj = ExcThread(bucket)
    thread_obj.start()

    while True:
        try:
            exc = bucket.get(block=False)
        except Queue.Empty:
            pass
        else:
            exc_type, exc_obj, exc_trace = exc
            # deal with the exception
            print exc_type, exc_obj
            print exc_trace

        if thread_obj.isAlive():
            continue
        else:
            break


if __name__ == '__main__':
    main()
