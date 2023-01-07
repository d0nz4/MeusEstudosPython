x = " Incrivel" #Variavel de escopo GLOBAL


def MyFunc():  #Variavel de escopo LOCAL
    global x
    x = " Inacreditavel"
    y = "Fantastico"
    global z # Para utilizar dentro de uma varivel local, uma função global
    z = "Bem Vindo ao Curso"
    print("Python é " + x + " e " + y)
    print(z)

MyFunc()

print("=======================")
print("você é" + x)
print(z)