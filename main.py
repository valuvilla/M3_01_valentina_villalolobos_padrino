#n2 = int(input("Dime un número entero: "))
#print(n2,(type(n2)))
#n3 = float(input("Dime un número racional:" ))
#print(n3, type(n3))   
#########################
#e1= int(input("dime un número entero: "))
#print("{:05d}".format(e1))
#e2= float(input("Dime un número flotante: "))
#print("{:08.03f}".format(e2))
#########################
alt = float(input("Introduce altura: "))
peso = float(input("Introduce peso: "))
print("P1 : La altura es {} metros y el peso es de {} KG".format(alt, peso))
print("P2 : La altura es {0} metros y el peso es de {1} KG".format(alt, peso))
print("P3 : La altura es {1} metros y el peso es de {0} KG".format(peso, alt))
print("P4: La altura es {alt} metros y el peso es de {peso} KG".format(alt=alt, peso=peso))
print(f'P5: la altura es {alt} metros y el peso es de {peso} KG')


      