n2 = int(input("Dime un número entero: "))
print(n2,(type(n2)))
print("\n")
n3 = float(input("Dime un número flotante:" ))
print(n3, type(n3))   
print("\n")
#########################
e1= int(input("dime un número entero: "))
print("{:05d}".format(e1))
e2= float(input("Dime un número flotante: "))
print("{:08.03f}".format(e2))
#########################
alt = float(input("Introduce altura: "))
peso = float(input("Introduce peso: "))
print("P1 : La altura es {:.02f} metros y el peso es de {:.03f} KG".format(alt, peso))
print("P2 : La altura es {} metros y el peso es de {} KG".format(alt, peso))
print("P3 : La altura es {0} metros y el peso es de {1} KG".format(alt, peso))
print("P4 : La altura es {1} metros y el peso es de {0} KG".format(peso, alt))
print("P5 : La altura es {alt} metros y el peso es de {peso} KG".format(alt=alt, peso=peso))
print(f'P6 : la altura es {alt} metros y el peso es de {peso} KG')
print('P7 : La altura es %(alt)s metros y el peso es de %(peso)s KG'% {"alt":alt,"peso":peso})
text = "P8 : La altura es {} metros y el peso es de {} KG"
print(text.format(alt, peso))
part1 = "La altura es {} metros"
part2 = "El peso es de {} KG"
print("P9 : " + part1.format(alt) + " y " + part2.format(peso))
