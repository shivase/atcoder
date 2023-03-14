#!/usr/bin/env python3
a,b = map(int, input().split())

num = 0;

while num * a - (num - 1) < b:
  num += 1

print(num);
