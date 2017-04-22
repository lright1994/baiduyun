#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from baidupcsapi import PCS


def main():
    pcs = PCS('891711784', 'mec9906285704')
    print(pcs.quota().content)


if __name__ == '__main__':
    main()
