numeroTeste=int(input())
led=[6,2,5,5,4,5,6,3,7,6]

for i in range(numeroTeste):
    leds=0
    numero=input()
    numero=list(numero)

    for i in range(len(numero)):
        leds+=led[int(numero[i])]
    print("{} leds".format(leds))
