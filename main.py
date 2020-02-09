# -*- coding: utf-8 -*-

import string
import re
import itertools

def atoms_counter(equation, view="default"):
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
						try:
							if term == 0:
								result["reagents"][atom[0]] += int(atom[1])*coefficient
							elif term == 1:
								result["products"][atom[0]] += int(atom[1])*coefficient
						except KeyError:
								if term == 0:
									result["reagents"][atom[0]] = int(atom[1])*coefficient
								elif term == 1:
									result["products"][atom[0]] = int(atom[1])*coefficient
					except:
						pass

	return result

def balancing(equation):
	equation = equation
	equation = equation.split("=")
	element_number = 0
	for term in range(len(equation)):
		equation[term] = equation[term].split("+")
		element_number += len(equation[term])

	for coefs in itertools.product(range(1, 20), repeat=element_number):
		new_equation = ""
		coef_number = 1
		for term in equation:
			for molecule in range(len(term)):
				if molecule == len(term)-1:
					new_equation += str(coefs[coef_number-1]) + "*" + term[molecule]
				else:
					new_equation += str(coefs[coef_number-1]) + "*" + term[molecule] + "+"
				coef_number += 1
			new_equation += "="
		new_equation = new_equation[:-1]
		if atoms_counter(new_equation)["reagents"] == atoms_counter(new_equation)["products"]:
			return new_equation

def limiting_reagent(equation, initial_quantity):
	equation = equation.split("=")
	for terms in range(len(equation)):
		equation[terms] = equation[terms].split("+")
	equation = equation[0]
	for terms in range(len(equation)):
		equation[terms] = equation[terms].split("*")

	initial_quantity = initial_quantity.split("=")
	for terms in range(len(initial_quantity)):
		initial_quantity[terms] = initial_quantity[terms].split("+")
	initial_quantity = initial_quantity[0]
	for terms in range(len(initial_quantity)):
		initial_quantity[terms] = initial_quantity[terms].split("*")

	for terms in range(len(equation)):
		try:
			if float(initial_quantity[terms][0])/float(equation[terms][0]) < coefficient:
				coefficient = float(initial_quantity[terms][0])/float(equation[terms][0])
				molecule = equation[terms][1]
		except NameError:
			coefficient = float(initial_quantity[terms][0])/float(equation[terms][0])
			molecule = equation[terms][1]
	
	return molecule

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
	#print(temp_to_lamb(5254.55))
	#print(lamb_to_temp(550))
  #print(atoms_counter("2*CH4+1*O2=1*CO2+2*H2O"))
	#print(balancing("NH3+O2=NO+H2O"))
	#print(limiting_reagent("1*Cu+2*HO=Cu(OH)2", "0.05*Cu+0.16*HO"))

test()