print ('Bem Vindo a calculadora de expressões, leis e equações matemáticas totalmente automatizada. Para saber quais operações automatizadas nos fazemos, aperte enter!')
import math
def deltanegativo (x):
    if (x < 0):
        print ('')
        print ('Por favor insira um número que o valor de Delta seja > ou = 0')
        print ('')
        calcex ()

def calcex ():
    print ('')
    dia1 = input ('Qual operação você deseja fazer? ')

####### COMANDO SAIR ###########################################################################################################################################################################################################
    if (dia1 == 'sair'):
        exit ()
        
                 
####### BHASKARA ################################################################################################################################################################################## ############################
    if (dia1 == 'bhaskara'):
        a = float (input ('Coloque o núnero cujo termo está elevado ao quadrado: '))
        b = float (input ('Coloque o número cujo termo está elevado a um: '))
        c = float (input ('Coloque o número que não tem termo '))
        delta = b**2 -4*a*c
        if (delta < 0):
                   deltanegativo (delta)
        x1a = -b +math.sqrt(delta)
        x2a = -b -math.sqrt(delta)
        x1 = x1a/(2*a)
        x2 = x2a/(2*a)
        print ('o valor de x1 é', x1, 'o valor de x2', x2, 'o valor de delta é', delta)
        calcex ()
####### MUV PRIMEIRA EQUAÇÃO###################################################################################################################################################################################################
    if (dia1 == 'muv1'):
        vo = str (input ('digite o valor de sua velociade inicial:  '))
        t = str (input ('digite o valor do tempo:  '))
        a = str (input ('digite o valor de sua aceleração:  '))
        v = str (input ('digite o valor de sua velocidade final:  '))
        if (vo == str ('x')):
            eq1 = float(v) - float(a)*float(t)
            print ('sua velociade inicial é de:', eq1)
            calcex ()
        if (t == str('x')):
           v1 = float (v)
           vo1 = float (vo)
           a1 = float (a)
           eq1 = (v1 - vo1)/a1
           print ('seu tempo é de:', eq1)
           calcex ()
        if (a == str('x')):
            v1 = float (v)
            vo1 = float (vo)
            t1 = float (t1)
            float (eq1 = (v - vo)/t)
            print ('sua aceleração é de:', eq1)
            calcex ()
        if (v == str('x')):
            vo1 = float (vo)
            a1 = float (a)
            t1 = float(t)
            eq1 = vo1 + a1*t1
            print ('sua velociade final é de:', eq1)
            calcex ()
        else:
            print ('por favor use apenas x para variável ou preencha os campos com apenas uma variável!')
            return
            calcex ()
    else:
        print('')
        print ('Nossa lista de operações é: MUV1 (v = vo + at) e bhaskara')
        print('')
        calcex ()
calcex ()
    
