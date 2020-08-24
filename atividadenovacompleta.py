def name():
	return(name)                     
def main():
    name = str(input("digite seu nome: "))
    print(len(name))
if __name__=="__main__":
    main()



def numero():
    return(numero)
def main():
    numero = int(input("digite um número inteiro: "))
    print (chr(numero))
if __name__== "__main__":
    main()



def converte(segundos):
    hora = segundos//3600
    minutos = (segundos % 3600) // 60
    segundos = (segundos % 3600) % 60
    return f'{hora}H:{minutos}M:{segundos}S'
def main():
    segundos = int(input("Escreva os segundos: "))
    total = converte(segundos)
    print(total)
if __name__ == "__main__":
   main()



def cauculo():
      return(calculo)
def main():
    num1 = int(input(" Escreva o número 1: "))
    num2 = int(input(" Escreva o número 2: "))
    num3 = int(input(" Escreva o número 3: "))
    num4 = int(input(" Escreva o número 4: "))
    num5 = int(input(" Escreva o número 5: "))
    calculo = (num1, num2, num3, num4, num5)

    print(max(num1, num2, num3, num4, num5))
    print(min(num1, num2, num3, num4, num5))
    print((num1 + num2 + num3 + num4 + num5)/5)

    
if __name__ =='__main__' :
    main()




def preco():
    preco = float(input("escreva o preço: "))
    vista = preco - (preco*0.09)
    prestacao = preco / 5
    prazo = (preco + (preco * 0.17))

    print("Preço a vista: %.2f"  % vista)
    print("Preço em 5 vezes: %.2f" % prestacao)
    print("Preço em 10 vezes: %.2f" % prazo)
              
def main():
    preco()
    

    
    
            
if __name__== '__main__' :
    main()
             



