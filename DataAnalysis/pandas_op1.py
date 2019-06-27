# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import string

dn_path = '/Users/corey/Tmp/dogNames2.csv'

def series():
    t = pd.Series(np.arange(3), index=list(["a", 'b', 'c']))
    print(t)
    print(string.ascii_uppercase)
    a = {string.ascii_uppercase[i]: i for i in range(10)}
    print(pd.Series(a))
    print(pd.Series(a, index=list(string.ascii_uppercase[5:15])))

def fileopen():
    t = pd.read_csv(dn_path)
    #print(t.sort_values(by='Count_AnimalName',ascending=False))
    t_sorted = t.sort_values(by='Count_AnimalName',ascending=False)
    print(list(t_sorted)[1,3,5])
    #print()

def dataframe1():
    t = pd.DataFrame(np.arange(12).reshape(3,4))
    print(t)

def main():
    #series()
    fileopen()
    #dataframe1()

if __name__ == "__main__":
    main()
