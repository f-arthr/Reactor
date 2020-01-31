# -*- coding: utf-8 -*-

import string
import re

def atoms_counter(equation):
	coefs = []

	equation = equation
	equation = equation.split("=")
	for term in range(len(equation)):
		equation[term] = equation[term].split("+")
		for part in range(len(equation[term])):
			equation[term][part] = equation[term][part].split("*")
			for coef in range(len(equation[term][part])):
				if coef == 1:
					equation[term][part][coef] = re.findall('[A-Z][^A-Z]*', equation[term][part][coef])
					for result in range(len(equation[term][part][coef])):
						equation[term][part][coef][result] = re.split('(\d+)', equation[term][part][coef][result])
						if equation[term][part][coef][result][-1] == "":
							del equation[term][part][coef][result][-1]
						if len(equation[term][part][coef][result]) == 1:
							equation[term][part][coef][result].append('1')

	result = {"reagents":{}, "products":{}}

	for term in range(len(equation)):
		for molecule in equation[term]:
			for coefficients in molecule:
				try:
					coefficient = int(coefficients)
				except:
					pass
				for atom in coefficients:
					try:
						if term == 0:
							result["reagents"][atom[0]] = int(atom[1])*coefficient
						elif term == 1:
							result["products"][atom[0]] = int(atom[1])*coefficient
					except:
						pass

	return result

def lamb_to_temp(wave):
  kelvin = round((2.89*(10**3))/(wave/1000), 2)
  celsius = round( kelvin - 273.15, 2)
  fahr = round((celsius*(9/5)) + 32, 2)
  return {"k": kelvin,
  "c": celsius,
  "f": fahr}

def temp_to_lamb(kelvin):
  lamb = round((2.89*(10**3))/(kelvin/1000), 2)
  return lamb

def test():
	print(temp_to_lamb(5254.55))
	#print(lamb_to_temp(550))
  #print(split_equation("2*CH4+1*O2=1*CO2+2*H2O"))

test()