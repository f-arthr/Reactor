# -*- coding: utf-8 -*-

import string

equation = input('Veuillez donner votre équation sous la forme "Na+Ar=NaAr" : ')

equation = equation.split('=')
equation[0] = equation[0].split('+')
equation[1] = equation[1].split('+')

    
print(equation)