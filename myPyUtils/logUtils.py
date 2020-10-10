#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   logUtils.py
@Time    :   2020/10/10 15:48:08
@Author  :   Jianhua Ye
@Phone    :   15655140926
@E-mail :   yejh@finchina.com
@License :   (C)Copyright Financial China Information & Technology Co., Ltd.
@Version :   1.0
@Desc    :   Print information on the console and save the log to a file.
'''

# here put the import lib
import logging
import logging.handlers
import os
import time


class logs(object):
    def __init__(self, logs_dir='logs'):
        self.logger = logging.getLogger("")

        # 设置输出的等级
        LEVELS = {
            'NOSET': logging.NOTSET,
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }

        # 创建文件目录
        #logs_dir = "logs"
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)

        # 修改log保存位置
        timestamp = time.strftime("%Y-%m-%d", time.localtime())
        logfilename = '%s.txt' % timestamp
        logfilepath = os.path.join(logs_dir, logfilename)
        rotatingFileHandler = logging.handlers.RotatingFileHandler(
            filename=logfilepath, maxBytes=1024 * 1024 * 50, backupCount=5)

        # 设置输出格式
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(funcName)s[line:%(lineno)d] %(message)s', '%Y-%m-%d %H:%M:%S')
        rotatingFileHandler.setFormatter(formatter)

        # 控制台句柄
        console = logging.StreamHandler()
        console.setLevel(logging.NOTSET)
        console.setFormatter(formatter)

        # 添加内容到日志句柄中
        self.logger.addHandler(rotatingFileHandler)
        self.logger.addHandler(console)
        self.logger.setLevel(logging.NOTSET)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)


if __name__ == "__main__":
    logs_dir = 'logs'
    logger = logs(logs_dir)
    logger.info("this is info")
    logger.debug("this is debug")
    logger.error("this is error")
    logger.warning("this is warning")