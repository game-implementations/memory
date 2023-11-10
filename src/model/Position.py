#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Position:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        msg = ""
        msg += "x: " + str(self.x) + ", y: " + str(self.y)
        return msg
