# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/127o2E2YDCLxkB84FYk-dr_lEc-mV94j9
"""

list = [
"月曜日は晴れです",
"火曜日は雨です",
"水曜日は晴れです",
"木曜日は晴れです",
"金曜日は曇りです",
"土曜日は曇りのち雨です",
"日曜日は雷雨です"]

dictionary = {
"mon":"晴れ",
"tue":"雨",
"wed":"晴れ",
"thu":"晴れ",
"fri":"曇り",
"sat":"曇りのち雨",
"sun":"雷雨",
}

print(list[2])
print(dictionary["wed"])

import random

var = random.randint(1, 100)

print(var)

if var % 3 == 0 and var % 5 == 0:
    print("FizzBuzz")
elif var % 3 == 0:
    print("Fizz")
elif var % 5 == 0:
    print("Buzz")
else :
    print(var)