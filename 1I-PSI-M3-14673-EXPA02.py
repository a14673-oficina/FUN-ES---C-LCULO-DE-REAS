"""Cálculo das áreas de figuras geométricas:
1. Círculo
2. Triângulo
3. Retângulo
Qual figura deseja calcular a área? ____

De acordo com a opção escolhida, o programa deve chamar a função calcula_area_circulo(), calcula_area_triagulo() ou calcula_area_retangulo(). Cada uma delas deve solicitar ao utilizador os parâmetros necessários para o cálculo da área. 
As funções devem retornar o valor calculado."""

print("Cálculo das áreas de figuras geométricas:")
print("1. Círculo")
print("2. Triângulo")
print("3. Retângulo")
opcao = input("Qual figura deseja calcular a área? ")
def circulo():
  raio = float(input("Insira o raio do círculo: "))
  area = 3.14 * raio ** 2
  return area
def triangulo():
  base = float(input("Insira a base do triângulo: "))
  altura = float(input("Insira a altura do triângulo: "))
  area = (base * altura) / 2
  return area
def retangulo():
  base = float(input("Insira a base do retângulo: "))
  altura = float(input("Insira a altura do retângulo: "))
  area = base * altura
  return area
if opcao == "1":
  area = circulo()
  print("A área do círculo é:", area)
elif opcao == "2":
  area = triangulo()
  print("A área do triângulo é:", area)
elif opcao == "3":
  area = retangulo()
  print("A área do retângulo é:", area)
else:
  print("Opção inválida. Por favor, escolha uma opção válida.")