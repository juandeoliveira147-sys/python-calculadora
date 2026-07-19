def primeiro_numero():
    while True:
        try:
            num1 = int(input("Digite o primeiro numero: "))
            #poderia colocar o segundo numero aqui, mas quero que a pessoa possa escolher a operação antes do segundo numero
            return num1
        except ValueError:
            print("\nDigite um numero inteiro")
    

operacao = ("+","-","x","/","//","*","**","%")

def escolher_operacao():
    while True:
        qualoperacao = input("\nQual operação? ")
        if qualoperacao in operacao:
            break
        else:
            print("\nPor favor, Digite uma operação valida!")
            print("As operações são -, +, x, /, // , * , ** e  % \n")
    return qualoperacao
    
        
def segundo_numero():
    while True:
        try:
            num2 = int(input("\nDigite o segundo numero: "))
            return num2
        except ValueError:
            print("\nDigite um numero inteiro: ")
    
def divisor(num1,num2):
    try:
        resultado = num1 / num2
        return resultado 
    except ZeroDivisionError:
        return None
    
    


num1 =  primeiro_numero()
qualoperacao = escolher_operacao()
num2 = segundo_numero()
if qualoperacao == "+":
    resultado = num1 + num2
elif qualoperacao == "-":
    resultado = num1 - num2
elif qualoperacao in("x","*"):
    resultado = num1 * num2
elif qualoperacao == "/":
    resultado = divisor(num1 , num2)
elif qualoperacao == "//":
    resultado = num1 // num2
elif qualoperacao == "**":
    resultado = num1 ** num2
elif qualoperacao == "%":
    resultado = num1 % num2

if resultado is None:
    print("Não é possivel dividir por 0")
else:
    print(f"\nO resultado de {num1}{qualoperacao}{num2} é {resultado}")
