#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec

SYMBOLS = {
    'customary': ('B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y'),
    'customary_ext': ('byte', 'kilo', 'mega', 'giga', 'tera', 'peta', 'exa',
                      'zetta', 'iotta'),
    'iec': ('Bi', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi', 'Yi'),
    'iec_ext': ('byte', 'kibi', 'mebi', 'gibi', 'tebi', 'pebi', 'exbi',
                'zebi', 'yobi'),
}


def bytes2human(n, fmt='%(value).1f%(symbol)s', symbols='customary'):
    """
    Convert n bytes into a human readable string based on fmt.
    symbols can be either "customary", "customary_ext", "iec" or "iec_ext",
    see: http://goo.gl/kTQMs

      >>> bytes2human(0)
      '0.0B'
      >>> bytes2human(0.9)
      '0.0B'
      >>> bytes2human(1)
      '1.0B'
      >>> bytes2human(1.9)
      '1.0B'
      >>> bytes2human(1024)
      '1.0K'
      >>> bytes2human(1048576)
      '1.0M'
      >>> bytes2human(1099511627776127398123789121)
      '909.5Y'

      >>> bytes2human(9856, symbols="customary")
      '9.6K'
      >>> bytes2human(9856, symbols="customary_ext")
      '9.6kilo'
      >>> bytes2human(9856, symbols="iec")
      '9.6Ki'
      >>> bytes2human(9856, symbols="iec_ext")
      '9.6kibi'

      >>> bytes2human(10000, "%(value).1f%(symbol)s/sec")
      '9.8K/sec'

      >>> # precision can be adjusted by playing with %f operator
      >>> bytes2human(10000, fmt="%(value).5f%(symbol)s")
      '9.76562K'
    """
    n = int(n)
    if n < 0:
        raise ValueError("n < 0")
    symbols = SYMBOLS[symbols]
    prefix = {}
    for i, s in enumerate(symbols[1:]):
        prefix[s] = 1 << (i + 1) * 10
    for symbol in reversed(symbols[1:]):
        if n >= prefix[symbol]:
            value = float(n) / prefix[symbol]
            return fmt % locals()
    return fmt % dict(symbol=symbols[0], value=n)
