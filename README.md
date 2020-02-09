# Reactor
A program for ecobalancing a reaction equation

## What functions are available?
* `temp_to_lamb`: find the lambda value from a temperature
* `lamb_to_temp`: find the temperature from a lambda value
* `atoms_counter`: count each atoms of any equation
* `balancing`: balance any equation
* `limiting_reagent`: find the limiting reagent from any equation

## How use it?
Input:
```python
print(temp_to_lamb(5254.55))
print(lamb_to_temp(550))
print(atoms_counter("2*CH4+1*O2=1*CO2+2*H2O"))
print(balancing("NH3+O2=NO+H2O"))
print(limiting_reagent("1*Cu+2*HO=Cu(OH)2", "0.05*Cu+0.16*HO"))
```

Output:
```
> 550.0
> {'k': 5254.55, 'c': 4981.4, 'f': 8998.52}
> {'reagents': {'C': 2, 'H': 8, 'O': 2}, 'products': {'C': 1, 'O': 4, 'H': 4}}
> 4*NH3+5*O2=4*NO+6*H2O
> Cu
```
