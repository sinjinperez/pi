#! /usr/bin/env python3
import sys
if len(sys.argv) < 2:
    print('usage: {} <n>'.format(sys.argv[0]))
    sys.exit(1)

n = int(sys.argv[1])



# count from 1 to n
for i in range(1,n+1):
   print(i)
   if i % 2 == 0:
        print('gig')
   if i % 3 == 0:
        print("'em")
   if i % 5 == 0:
        print("'em")
   if i % 5 == 0:
        print("'em"
   if i % 5 == 0:
        print("'em"

# if number is divisable by 3 say 'gig'
#if number is divisable by 5, say 'em'
#if number is divisable by both, say 'gig em'
