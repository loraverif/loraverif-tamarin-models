#!/usr/bin/python

import re
import os
import sys
debug = True

lines = sys.stdin.readlines()
lemma = sys.argv[1]

# INPUT:
# - lines contain a list of "%i:goal" where "%i" is the index of the goal
# - lemma contain the name of the lemma under scrutiny
# OUTPUT:
# - (on stdout) a list of ordered index separated by EOL


rank = []             # list of list of goals, main list is ordered by priority
maxPrio = 110
for i in range(0,maxPrio):
  rank.append([])

#, multp\(H_n_2.*P1.*, multp\(~f,.*~TPM_EK_Seed

   
if lemma[0:7]=="oracle_":
  print "applying oracle"
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*#t01 < #t02.*', line): rank[109].append(num)
    elif re.match('.*!KU\(.*~root.*', line): rank[108].append(num)
    elif re.match('.*Running.*', line): rank[108].append(num)
    elif re.match('.*NS_Store_00\(.*', line): rank[106].append(num)
    elif re.match('.*Network.*', line): rank[108].append(num)
    elif re.match('.*Role.*', line): rank[108].append(num)
    elif re.match('.*ED_Store_02\(.*', line): rank[107].append(num)
    elif re.match('.*random16\).*', line): rank[100].append(num)
    elif not(re.match('.*splitEqs.*', line)): rank[1].append(num)
    elif re.match('.*splitEqs.*', line): rank[0].append(num)

else:
    print "not applying the rule"
    exit(0)

# Ordering all goals by ranking (higher first)
for listGoals in reversed(rank):
  for goal in listGoals:
    sys.stderr.write(goal)
    print goal
