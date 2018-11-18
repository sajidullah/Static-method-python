# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 13:09:36 2018

@author: sajid Ullah
"""
#
class Calculator:

    def addNums(x, y):
        return x + y

# create addNumbers static method
Calculator.addNums = staticmethod(Calculator.addNums)

print('Sum:', Calculator.addNums(15, 110))

# with static method
class Calculator:

    # create addNumbers static method
    @staticmethod
    def AddNums(x, y):
        return x + y

print('Sum:', Calculator.AddNums(15, 110))