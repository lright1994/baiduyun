#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
"""
baiduyun.models
~~~~~~~~~~~~~~~

This module contains the primary objects that power baiduyun.
"""

from time import gmtime, asctime

from utils import bytes2human


class File(object):
    def __init__(self, fileinfo):
        """百度云一个文件的抽象(文件夹也是文件对象)

        :param fileinfo: 文件信息
        :type fileinfo: dict
        """
        for k, v in fileinfo.items():
            self.__setattr__(k, v)

    @property
    def hsize(self):
        """human readable size"""
        return bytes2human(self.size)

    @property
    def hlocal_ctime(self):
        """human readable local_ctime"""
        return asctime(gmtime(self.local_ctime))

    @property
    def hlocal_mtime(self):
        """human readable local_mtime"""
        return asctime(gmtime(self.local_mtime))

    @property
    def hserver_ctime(self):
        """human readable server_ctime"""
        return asctime(gmtime(self.server_ctime))

    @property
    def hserver_mtime(self):
        """human readable server_mtime"""
        return asctime(gmtime(self.server_mtime))
