# -*- coding: utf-8 -*-
import hashlib
import mmh3

class MySimHash(object):
    def __init__(self):
        self.f = 32

    def get_simhash(self, pairs):
        s = [0] * self.f
        for p in pairs:
            feature = p[0]
            weight = p[1]
            h = list(bin(mmh3.hash(feature.encode('utf-8'), signed=False))[2:])
            #h = list(bin(int(hashlib.md5(feature.encode('utf-8')).hexdigest(), 16))[2:])
            h = ['0'] * (self.f - len(h)) + h
            for i in range(self.f):
                s[i] += weight * (-1) ** (int(h[i]) + 1)
        for i in range(self.f):
            if s[i] < 0:
                s[i] = 0
            else:
                s[i] = 1
        return s

    def get_distance(self, s1, s2):
        hamdis = []
        for i in range(self.f):
            hamdis.append(s1[i] ^ s2[i])

        # print(hamdis)
        hamdis = hamdis.count(1)
        return hamdis
