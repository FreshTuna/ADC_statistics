def printLvN(dictionary,name,level) : 

  dict_champ = dictionary[name]

  print('Lv',level,' statistics of ',name ,":")

  AD_Plus = dict_champ['AD+'] * (level-1) * (0.7025 + 0.0175 * (level-1))

  HP_Plus = dict_champ['HP+'] * (level-1) * (0.7025 + 0.0175 * (level-1))

  MP_Plus = dict_champ['MP+'] * (level-1) * (0.7025 + 0.0175 * (level-1))

  AS_Plus = (dict_champ['AS+'] * 0.01) * (level-1) * (0.7025 + 0.0175 * (level-1))

  print("\n AD : ",round(dict_champ['AD'] + AD_Plus),"\n","AS : ", round(dict_champ['AS']+(dict_champ['AS']*AS_Plus),3),"\n","HP : ", dict_champ['HP']+HP_Plus,"\n","MP : ", dict_champ['MP']+MP_Plus,"\n","Range : ",dict_champ['Range'],"\n","MS : ",dict_champ['MS'],"\n" )
