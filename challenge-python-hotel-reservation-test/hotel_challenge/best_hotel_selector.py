

"""
    Lakewood possui uma classificação 3 e suas taxas de dia de semana são R$110 para
clientes normais e R$80 para participantes do programa de fidelidade. As taxas de
final de semana são respectivamente R$90 e R$80 para clientes normais e
participantes do programa de fidelidade.
    Bridgewood possui uma classificação 4 e suas taxas de dia de semana são R$160
para clientes normais e R$110 para participantes do programa de fidelidade. As taxas
de final de semana são respectivamente R$60 e R$50 para clientes normais e
participantes do programa de fidelidade.
    Ridgewood possui uma classificação 5 e suas taxas de dia de semana são R$220
para clientes normais e R$100 para participantes do programa de fidelidade. As taxas
de final de semana são respectivamente R$150 e R$40 para clientes normais e
participantes do programa de fidelidade.

Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)


"""

from posixpath import split

tp, dates = input(print("Input your customer status and respective date(In this format[Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)]): " )).split(':',2)
dateA, dateB, dateC = dates.split(',', 3)
dateAn, dateAwd = dateA.split("(")
dateBn, dateBwd = dateB.split("(")
dateCm, dateCwd = dateC.split("(")

if(dateAwd == "sat)" or dateAwd == "sun)"):
    Aa = 2
else:
    Aa = 1
if(dateBwd == "sat)" or dateBwd == "sun)"):
    Bb = 2
else:
    Bb = 1
if(dateCwd == "sat)" or dateCwd == "sun)"):
    Cc = 2
else:
    Cc = 1
if(tp == "Regular"):
    tc = 3
else:
    tc = 7

Res = Aa + Bb + Cc + tc

if(Res == 6  or Res == 7):
    print("Lakewood")
elif(Res == 8 or Res == 9):
    print("Bridgewood")
elif(Res == Res == 10):
    print("Lakewood")
else:
    print("Ridgewood")    

