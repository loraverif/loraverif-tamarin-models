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

   
if lemma[0:7]=="correct":
  print "applying oracle to "+lemma
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*EntityInit*', line): rank[109].append(num)
    elif re.match('.*Initialised.*', line): rank[108].append(num)
    elif re.match('.*CommissionCompleted.*', line): rank[107].append(num)
    elif re.match('.*Commissioned.*', line): rank[106].append(num)
    elif re.match('.*Ltk_shared.*', line): rank[105].append(num)
    elif re.match('.*_State_.*', line): rank[104].append(num)
    elif re.match('.*CheckCtr.*', line): rank[103].append(num)
    elif re.match('.*Join_Request.*', line): rank[100].append(num)
    elif re.match('.*Join_Accept.*', line): rank[90].append(num)
    elif not(re.match('.*splitEqs.*', line)): rank[1].append(num)
    elif re.match('.*splitEqs.*', line): rank[0].append(num)
    
elif lemma[0:10]=="oracle_two":
  print "applying oracle to"+lemma
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*Check.*', line): rank[109].append(num)
    elif re.match('.*ED_Store.*', line): rank[108].append(num)


elif lemma[0:24]=="AS_confusion_freeness_1":
  print "applying oracle to "+lemma
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*Commit.*', line): rank[109].append(num)
    elif re.match('.*Role*', line): rank[108].append(num)
    elif re.match('.*In_S.*', line): rank[108].append(num)
    elif re.match('.*ED_State.*', line): rank[107].append(num)
    elif re.match('.*Check.*', line): rank[106].append(num)
    elif re.match('.*KU\( AesKey\(.*JSAS.*JSAS.*', line): rank[105].append(num)
    elif re.match('.*KU\( ~JSASKey.*', line): rank[105].append(num)
    elif re.match('.*KU\( AesKey\(.*Nwk.*~rootN.*', line): rank[105].append(num)
    elif re.match('.*KU\( ~rootNw.*', line): rank[105].append(num)
    elif re.match('.*KU\( AesKey\(.*JSAS.*JSAS.*', line): rank[105].append(num)
    elif re.match('.*JS_State.*', line): rank[70].append(num)
    #elif re.match('.*KU\( .*senc.*SessionKey.*SessionKey.*SessionKey.*SessionKey.*~rootNekKey\)\)\)\)\)',line): rank[85].append(num)

elif lemma[0:24]=="AS_confusion_freeness_3":
  print "applying oracle to"+lemma
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*Commit.*', line): rank[109].append(num)
    elif re.match('.*Running_Conf.*', line): rank[108].append(num)
    elif re.match('.*Commissioned.*', line): rank[100].append(num)
    elif re.match('.*Role.*', line): rank[107].append(num)
    #elif re.match('.*JS_State.*', line): rank[70].append(num)
    elif re.match('.*ED_State.*', line): rank[105].append(num)
    elif re.match('.*In_S.*', line): rank[100].append(num)
    elif re.match('.*KU\( ~root.*', line): rank[105].append(num)
    elif re.match('.*KU\( AesKey\(.*', line): rank[105].append(num)
    elif re.match('.*KU\( Counter\(.*', line): rank[90].append(num)
    elif re.match('.*KU\( MAC\(.*MHDR.*AesKey\(.*Nwk.*~rootNwk.*', line): rank[80].append(num) #*AesKey\(.*Nwk.*,~rootNwkKey.*
    #elif re.match('.*KU\( .*senc.*SessionKey.*SessionKey.*SessionKey.*SessionKey.*~rootNekKey\)\)\)\)\)',line): rank[85].append(num)

elif lemma[0:19]=="auth_weak_agreement":
  print "applying oracle to "+lemma
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*Commit.*', line): rank[109].append(num)
    elif re.match('.*Role*', line): rank[109].append(num)
    elif re.match('.*In_S.*', line): rank[108].append(num)
    elif re.match('.*ED_State.*', line): rank[107].append(num)
    elif re.match('.*Check.*', line): rank[106].append(num)
    elif re.match('.*KU\( AesKey\(.*JSAS.*JSAS.*', line): rank[105].append(num)
    elif re.match('.*KU\( ~JSASKey.*', line): rank[105].append(num)
    elif re.match('.*KU\( AesKey\(.*Nwk.*~rootN.*', line): rank[105].append(num)
    elif re.match('.*KU\( ~rootNw.*', line): rank[105].append(num)
    elif re.match('.*KU\( AesKey\(.*JSAS.*JSAS.*', line): rank[105].append(num)
    elif re.match('.*KU\( .*senc.*SessionKey.*SessionKey.*SessionKey.*SessionKey.*~rootNekKey\)\)\)\)\)',line): rank[85].append(num)


elif lemma[0:15]=="auth_non_inject":
  print "applying oracle to "+lemma
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*Commit.*', line): rank[109].append(num)
    elif re.match('.*Role*', line): rank[109].append(num)
    elif re.match('.*In_S.*', line): rank[108].append(num)
    elif re.match('.*KU\( Response.*', line): rank[105].append(num)
    elif re.match('.*KU\( SessionKey.*', line): rank[105].append(num)
    elif re.match('.*KU\( senc\(.*0x0.*', line): rank[100].append(num)
    elif re.match('.*KU\( MAC.*', line): rank[105].append(num)
    elif re.match('.*KU\( ~JSASKey.*', line): rank[105].append(num)
    elif re.match('.*KU\( ~rootNw.*', line): rank[105].append(num)
    elif re.match('.*KU\( AesKey\(.*JSAS.*JSAS.*', line): rank[105].append(num)
    elif re.match('.*State.*', line): rank[103].append(num)
    elif re.match('.*KU\( senc\(<n1.*JSAS.*', line): rank[100].append(num)
    elif re.match('.*Ltk_shared.*', line): rank[90].append(num)
    elif re.match('.*Role*', line): rank[90].append(num)
    elif re.match('.*KU\( MAC\(.*senc.*~JSAS.*',line): rank[85].append(num)
    elif re.match('.*KU\( senc\(<AppSKey.*AesKey.*~JSAS.*',line): rank[85].append(num)
    elif re.match('.*KU.*senc.*MAC.*', line): rank[80].append(num)
    elif re.match('.*KU\( AesKey\(.*', line): rank[80].append(num)
    elif re.match('.*Check.*', line): rank[70].append(num)

elif lemma[0:11]=="auth_inject":
  print "applying oracle to "+lemma
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*Commit.*', line): rank[109].append(num)
    elif re.match('.*Role*', line): rank[109].append(num)
    elif re.match('.*In_S.*', line): rank[108].append(num)
    elif re.match('.*Check.*', line): rank[107].append(num)
    elif re.match('.*State.*', line): rank[107].append(num)
    elif re.match('.*KU\( Response.*', line): rank[105].append(num)
    #elif re.match('.*KU\( PD_Wrapper.*', line): rank[105].append(num)
    elif re.match('.*KU\( SessionKey.*', line): rank[105].append(num)
    elif re.match('.*KU\( senc\(.*0x0.*', line): rank[100].append(num)
    elif re.match('.*KU\( MAC.*', line): rank[105].append(num)
    elif re.match('.*KU\( ~JSASKey.*', line): rank[105].append(num)
    elif re.match('.*KU\( ~rootNw.*', line): rank[105].append(num)
    elif re.match('.*KU\( AesKey\(.*JSAS.*JSAS.*', line): rank[105].append(num)
    elif re.match('.*KU\( AesKey\(.*', line): rank[105].append(num)
    elif re.match('.*KU\( senc\(<n1.*JSAS.*', line): rank[100].append(num)
    elif re.match('.*Ltk_shared.*', line): rank[90].append(num)
    elif re.match('.*KU\( MAC\(.*senc.*~JSAS.*',line): rank[85].append(num)
    elif re.match('.*KU\( senc\(<AppSKey.*AesKey.*~JSAS.*',line): rank[85].append(num)
    elif re.match('.*KU.*senc.*MAC.*', line): rank[80].append(num)




elif lemma[0:5]=="auth_":
  print "applying oracle to "+lemma
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*Check.*', line): rank[109].append(num)
    elif re.match('.*State.*', line): rank[100].append(num)
    elif re.match('.*Ltk_shared.*', line): rank[90].append(num)
    elif re.match('.*Role*', line): rank[90].append(num)
    elif re.match('.*KU.*senc.*MAC.*', line): rank[80].append(num)
    elif re.match('.*KU\( AesKey\(.*', line): rank[80].append(num)


else:
    print "not applying the rule"
    exit(0)

# Ordering all goals by ranking (higher first)
for listGoals in reversed(rank):
  for goal in listGoals:
    sys.stderr.write(goal)
    print goal