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

if lemma[0:23]=="AS_confusion_freeness_2":
  print "applying oracle to "+lemma
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*Role.*', line): rank[109].append(num)
    elif re.match('.*Running.*', line): rank[100].append(num)
    elif re.match('.*vr.*vr.*', line): rank[95].append(num)
    elif re.match('.*In_S.*', line): rank[90].append(num)
    elif re.match('.*_State_.*', line): rank[80].append(num)
    elif re.match('.*CheckCtr.*', line): rank[80].append(num)
    elif re.match('.*KU\( AesKey.*Nwk.*~root.*', line): rank[75].append(num)
    elif re.match('.*KU\(.*senc\(.*DevEUI,.*rootAppKey.*rootAppKey.*rootAppKey.*rootAppKey.*',line): rank[70].append(num)    
    elif re.match('.*KU\( ~root.*Key \)', line): rank[65].append(num)
    elif re.match('.*KU\( ~.*Addr \)', line): rank[65].append(num)
    elif re.match('.*KU\( Nonce.*Addr\)', line): rank[65].append(num)
    elif re.match('.*KU\( MAC.*MHDR.*rootNwkKey.*', line): rank[65].append(num)
    elif re.match('.*KU\( MAC.*Key\).*', line): rank[60].append(num)
    elif re.match('.*KU\( MAC.*Key\).*', line): rank[60].append(num)
    elif re.match('.*KU\(.*NwkSEncKey\)\).*', line): rank[60].append(num)
    elif re.match('.*KU\( senc\(<.*Nonce.*Session.*0x02.*rndJoin.*rnd32Dev.*rootAppKey.*', line): rank[55].append(num)
    elif re.match('.*KU\( SessionKey.*\)\).*', line): rank[50].append(num)
    elif re.match('.*KU\(.*0x02.*rndJoin.*rnd32Dev.*rootAppKey.*', line): rank[50].append(num)

elif lemma[0:23]=="AS_confusion_freeness_1":
  print "applying oracle to "+lemma
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*Role.*', line): rank[109].append(num)
    elif re.match('.*Running.*', line): rank[100].append(num)
    elif re.match('.*AS_State_.*', line): rank[90].append(num)  
    elif re.match('.*ED_State_.*', line): rank[90].append(num)
    elif re.match('.*JS_State_.*', line): rank[90].append(num)
    elif re.match('.*In_S.*', line): rank[85].append(num)
    elif re.match('.*CheckCtr.*', line): rank[85].append(num)
    elif re.match('.*KU\( MAC.*DevEUI,.*~rootAppKey\).*', line): rank[80].append(num)
    elif re.match('.*KU\( PD_Wrapper\(senc.*MAC.*DevEUI,.*~rootAppKey\).*FNwkSIntKey.*NwkSEncKey.*', line): rank[79].append(num)
    elif re.match('.*KU\( senc.*MAC.*DevEUI,.*~rootAppKey\).*FNwkSIntKey.*NwkSEncKey.*', line): rank[79].append(num)
    elif re.match('.*KU\( senc\(<.*\'1\'.*DevEUI,.*~rootAppKey\).*', line): rank[78].append(num)
    elif re.match('.*KU\( Nonce.*DevAddr\)', line): rank[75].append(num)
    elif re.match('.*KU\( Nonce.*DevAddr.1\)', line): rank[75].append(num)
    elif re.match('.*KU\( ~.*DevAddr.*\)', line): rank[75].append(num)
    elif re.match('.*KU\( MAC.*DevEUI.1,.*~rootAppKey.1\).*', line): rank[74].append(num)
    elif re.match('.*KU\( PD_Wrapper\(senc.*MAC.*DevEUI.1,.*~rootAppKey.1\).*FNwkSIntKey.*NwkSEncKey.*', line): rank[74].append(num)
    elif re.match('.*KU\( senc.*MAC.*DevEUI.1,.*~rootAppKey.1\).*FNwkSIntKey.*NwkSEncKey.*', line): rank[73].append(num)
    elif re.match('.*KU\( senc\(<.*\'1\'.*DevEUI.1,.*~rootAppKey.1\).*', line): rank[73].append(num)


    # elif re.match('.*KU\( AesKey.*Nwk.*~root.*', line): rank[75].append(num)
    # elif re.match('.*KU\(.*senc\(.*DevEUI.*rootAppKey.*rootAppKey.*rootAppKey.*rootAppKey.*',line): rank[70].append(num)    
    # elif re.match('.*KU\(.*senc\(<\(\'1\'+.*Nonce.*SessionKey.*~rootAppKey.*',line): rank[67].append(num)   
    # elif re.match('.*KU\( ~root.*Key \)', line): rank[65].append(num)
    # elif re.match('.*KU\(.*SessionKey.*\)\).*', line): rank[65].append(num)
    # elif re.match('.*KU\( ~root.*Key.1 \)', line): rank[65].append(num)
    # elif re.match('.*KU\( ~.*Addr.1 \)', line): rank[64].append(num
    # elif re.match('.*KU\( Nonce.*Addr.1\)', line): rank[64].append(num)

    # elif re.match('.*KU\( MAC.*Key.1\).*', line): rank[60].append(num)
    # elif re.match('.*KU\(.*NwkSEncKey\)\).*', line): rank[60].append(num)
    # elif re.match('.*KU\( senc\(<.*Nonce.*Session.*0x02.*rndJoin.*rnd32Dev.*rootAppKey.*', line): rank[55].append(num)
    # elif re.match('.*KU\(.*0x02.*rndJoin.*rnd32Dev.*rootAppKey.*', line): rank[50].append(num) 
   
elif lemma[0:7]=="correct":
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


elif lemma[0:19]=="auth_weak_agreement":
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
