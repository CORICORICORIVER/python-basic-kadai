# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19uM2EXPyULFhJy7x6Af08twVlcqRBMz5
"""

def consumption_tax(price, tax):
    X = price + price * tax / 100
    print(f"{X}円")

consumption_tax(999, 10)