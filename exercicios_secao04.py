"""
Exercícios da seção 04 do curso de Python
"""
"""
# 01.Faça um programa que leia um número inteiro e o imprima
print('Digite um número inteiro: ')

num_int = input()

print(f'O número inteiro digitado é {int(num_int)}')

# 02.Faça um programa que leia um numero real e o imprima
print('Digite um número real: ')

num_real = input()

print(f'O número real digitado é {float(num_real)}')

# 03.Peça ao usuário para digitar três valores inteiros e imprima a soma deles
print('Digite o primeiro número inteiro para a soma: ')

num1 = input()

print('Digite o segundo número inteiro para a soma: ')

num2 = input()

print('Digite o primeiro número inteiro para a soma: ')

num3 = input()

soma = int(num1) + int(num2) + int(num3)

print(f'A soma dos numeros é igual a {int(soma)}')

# 04.Leia um número real e imprima o resultado do quadrado desse número

print('Insira o número que você quer o quadrado: ')

num1 = input()

quadrado = float(num1) * float(num1)

print(f'O quadrado de {num1} é {quadrado}')

# 05. Leia um número real e impima a quinta parte deste número
print('Digite um número real: ')

num = input()

divisao = float(num) / 5

print(f'A quinta parte de {num} é {divisao}')

# 06. Leia uma temperatura em graus Celcius e apresente-a convertida em graus Fahrenheit.
# A fórmula de conversão é: F = C*(9.0/5.0)+32.0

print('Temperatura em Celcius: ')

c = input()

f = float(c)*(9/5)+32

print(f'{c}º Celcius são {f}º Fahrenheit')

# 07. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
# A fórmula de conversão é: C = 5.0*(F-32.0)/9.0
print('Temperatura em Fahrenheit: ')

f = input()

c = 5*(float(f)-32)/9

print(f'{f}º Fahrenheit são {c}º Celsius')

# 08. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
# A fórmula de conversão é: C = K - 273.15

print('Temperatura em Kelvin: ')

k = input()

c = float(k) - 273.15

print(f'{k}º Fahrenheit são {c}º Celsius')

# 09. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
# A fórmula de conversão é: K = C + 273.15

print('Temperatura em Celsius: ')

c = input()

k = float(c) + 273.15

print(f'{c}º Celsius são {k}º Fahrenheit')

# 10. Leia uma velocidade em km/h e apresente-a convertida em m/s
# Fórmula de conversão: M = K/3.6

print('Km/h:  ')

k = input()

m = float(k)/3.6

print(f'{k}km/h é o mesmo que {m}m/s')

# 11.Leia uma distância em m/s e apresente-a convertida em km/h.
# Formula de conversão: k = m*3.6

print('m/s:  ')

m = input()

k = float(m)*3.6

print(f'{m}m/s é o mesmo que {k}km/h')

# 12. Leia uma distância em milhas e apresente-a convertida em km.
# Fórmula de conversão é: k = 1.61*m

print('Milhas:  ')

m = input()

k = float(m)*1.61

print(f'{m} Milhas é o mesmo que {k} quilômetros')

# 13. Leia uma distância em quilômetros e apresente-a convertida em milhas.
# Fórmula de conversão: m = k/1,61

print('Quilômetros:  ')

k = input()

m = float(k)/1.61

print(f'{k} quilômetros é o mesmo que {m} milhas')

# 13. Leia uma distância em quilômetros e apresente-a convertida em milhas.
# Fórmula de conversão: m = k/1,61

print('Quilômetros:  ')

k = input()

m = float(k)/1.61

print(f'{k} quilômetros é o mesmo que {m} milhas')

# 14. Leia um ângulo em graus e apresente-o convertido em radianos.
# Fórmula de conversão: r = g * pi/180

print('ângulo em graus que quer converter para radianos: ')

g = input()

r = float(g)*3.14/180

print(f'{g} graus são {r} radianos')

# 15. Leia um ângulo e radianos e apresente-o convertido em graus.
# Fórmula de conversão: g = r*180/pi

print('ângulo em graus que quer converter para radianos: ')

r = input()

g = float(r)*180/3.14

print(f'{r} radianos são {g} graus')

# 16. Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
# Fórmula de conversão: c = p*2.54

print('Digite as polegadas: ')

p = input()

c = float(p)*2.54

print(f'{p} polegadas são {c} centimetros')

# 17. Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
# Fórmula de conversão: p = c/2.54

print('Digite os centímetros: ')

c = input()

p = float(c)/2.54

print(f'{c} centímetros são {p} polegadas')

# 18. Leia um valor de volume em metros cúbicos m3 e apresente-o em litros.
# Fórmula de conversão: l = 1000 * m

print('Digite os metros cúbicos: ')

m = input()

l = float(m)*1000

print(f'{m} metros cúbicos são {l} litros')

# 19. Leia um valor de volume em litros e apresente-o em metros cúbicos.
# Fórmula de conversão: m = l/1000

print('Digite os litros: ')

l = input()

m = float(l)/1000

print(f'{l} litros são {m} metros cúbicos')

# 20. Leia um valor de massa em quilogramas e apresente-o convertido em libras.
# Fórmula de conversão: l = k/0.45

print('Quilogramas: ')

k = input()

l = float(k)/0.45

print(f'{k} quilogramas são {l} libras')

# 21. Leia um valor de massa em libras e apresente-o convertido em quilogramas.
# Fórmula de conversão: k = l*0.45

print('Libras: ')

l = input()

k = float(l)*0.45

print(f'{l} libras são {k} quilogramas')

# 22. Leia um valor de comprimento em jardas e apresente-o em metros.
# Fórmula de conversão: m = 0.91*j

print('Jardas: ')

j = input()

m = float(j)*0.91

print(f'{j} jardas são {m} metros')

# 23. Leia um valor de comprimento em metros e apresente-o em jardas.
# Fórmula de conversão: j = m/0.91

print('Metros: ')

m = input()

j = float(m)/0.91

print(f'{m} metros são {j} jardas')

# 24. Leia um valor de área em metros quadrados e apresente-o convertido em acres.
# Fórmula de conversão: a = m*0.00247

print('Metros quadrados: ')

m = input()

a = float(m)*0.00247

print(f'{m} metros quadrados são {a} acres')

# 25. Leia um valor de área em acres e apresente-o convertido em metros quadrados.
# Fórmula de conversão: m = a*4048.58

print('Acres: ')

a = input()

m = float(a)*4048.58

print(f'{a} acres são {m} metros quadrados')

# 26. Leia um valor de área em metros quadrados e apresente-o convertido em hectares.
# Fórmula de conversão: h = m*0.0001

print('Metros quadrados: ')

m = input()

h = float(m)*0.0001

print(f'{m} metros quadrados são {h} hectares')

# 27. Leia um valor de área em metros quadrados e apresente-o convertido em hectares.
# Fórmula de conversão: m = h*10000

print('Hectares: ')

h = input()

m = float(h)*10000

print(f'{h} hectares são {m} metros quadrados')

# 28. Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.

print('Digite 3 valores: ')
print('A: ')
a = input()
print('B: ')
b = input()
print('C: ')
c = input()
soma = (float(a)*float(a))+(float(b)*float(b))+(float(c)*float(c))
print(f'A soma dos quadrados de {a},{b} e {c} é {soma}')

# 29. Leia quatro notas, calcule a média aritmética e imprima o resultado
print('Digite 4 valores: ')
print('A: ')
a = input()
print('B: ')
b = input()
print('C: ')
c = input()
print('D: ')
d = input()
media = (float(a)+float(b)+float(c)+float(d))/4
print(f'A média aritmética de {a}, {b}, {c} e {d} é {media}')

# 30. Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.
print('Digite a quantia de reais: ')
real = input()
print('Cotação do dólar: ')
dolar = input()
valor = float(real)/float(dolar)
print(f'Com R${real} você consegue U${valor}')

# 31. Leia um número inteiro e imprima o seu antecessor e seu sucessor.
print('Escolha um número: ')
a = input()
print(f'O antecessor e sucessor de {a} são {int(a)-1} e {int(a)+1} respectivamente')

# 32. Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor do seu dobro.
print('Um número: ')
a = input()
soma = (int(a)*3+1)+(int(a)*2-1)
print(f'A soma do sucessor do triplo com o antecessor do dobro de {a} é {soma}')

# 33. Leia o lado de um quadrado e imprima como resultado a sua área.
print('Lado de um quadrado: ')
l = input()
print(f'A área de um quadrado de lado {float(l)} é {float(l)*2}')

# 34. Leia o valor do raio de um círculo e calcule e imprima a área do círculo correpondente.
# A área do círculo é pi*raio2, pi = 3.141592
print('Valor do raio de um círculo: ')
r = input()
a = 3.141592*float(r)*float(r)
print(f'A área de um círculo de raio {r} é de {a}')

# 35. Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
# hip = raiz de a2+b2. Calcule o valor da hipotenusa através da equação.
print('Digite os catetos: ')
print('A: ')
a = input()
print('B: ')
b = input()
hip = ((float(a)*float(a))+(float(b)*float(b))) ** 0.5
print(f'A hipotenusa de um triangulo de lados {a} e {b} é {hip}')

# 36. Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
# Fórmula: v = pi*raio2*altura, pi = 3.141592

print('Altura do cilindro: ')
h = input()
print('Raio do cilindro: ')
r = input()
v = 3.141592*float(r)**2*float(h)
print(f'Volume do cilindro de raio {r} e altura {h} = {v}')

# 37. Faça um programa que leia o valor de um produto e imprima o valor com desconto,
# tendo em vista que o desconto foi de 12%
print('Valor do produto: ')
v = input()
desconto = float(v)*0.12
print(f'O valor do desconto é de R${desconto} e o preço final é de R${float(v)-float(desconto)}')

# 38. Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo
# que ele ganhou um aumento de 25%
print('Salário atual: ')
a = input()
aumento = float(a)*0.25
print(f'O aumento de salário foi de R${aumento} e o novo salário é igual a R${float(a)+float(aumento)}')

# 39. A importância de R$780000 será dividida entre três ganhadores de um concurso.
# Sendo que da quantia total o primeiro ganhará 46%, o segundo 32%, o terceiro o restante, quanto cada um ganhará?
a = 780000*0.46
b = 780000*0.32
c = 780000-(float(a)+float(b))
print(f'O primeiro ganhador ganhará R${a}, o segundo ganhará R${b} e o terceiro ganhará R${c}')

# 40. Uma empresa contrata um encanador a R$30 por dia. Faça um programa que solicite o
# número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga
# sabendo-se que são descontados 8% para imposto de renda.
print('Dias trabalhados: ')
d = input()
b = int(d)*30
l = float(b)-float(b)*0.08
print(f'O valor bruto será de R${b} e o valor líquido R${l}')

# 41. Faça um programa que leia o valor da hora de trabalho e o número de horas trabalhadas no mês.
# Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.
print('Informe valor da hora: ')
v = input()
print('Informe quantia de horas: ')
h = input()
s = float(v)*int(h)
t = float(s)+float(s)*0.1
print(f'Total do salário é de R${t}')

# 42. Receba o salário-base de um funcionário. Calcule e imprima o salário a receber,
# sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base.
# Além disso ele paga 7% de impostos sobre o salário-base.
print('Salário-base: ')
s = input()
g = float(s)*0.05
i = float(s)*0.07
t = float(s)-float(i)+float(g)
print(f'O salário base sofre com o imposto de {i} e ganha com a gratificação de {g} ficando um total de {t}')

# 43. Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
# O total a pagar com desconto de 10%, o valor de cada parcela, no parcelamento 3x sem juros,
# a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
# a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
print('Valor da venda: ')
valor = input()
desconto = float(valor)*0.1
parcela = (float(valor)-float(desconto))/3
comvista = (float(valor)-float(desconto))*0.5
comprazo = float(valor)*0.5
print(f'O preço da venda:{valor}\nCom desconto:{float(valor)-float(desconto)}'
      f'\n3 Parcelas de:{parcela}'
      f'\nComissão do vendedor se for a vista:{comvista}\nComissão vendedor se for parcelado:{comprazo}')
      
# 44. Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada.
# Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo
print('Altura dos degraus em cm: ')
hescada = input()
print('Altura desejada em metros: ')
hdesejada = input()
degraus = float(hdesejada)/(float(hescada)/100)
print(f'Terá que subir {degraus} degraus')

# 45. Faça um programa para converter uma letra maiúscula em letra miníscula.
# Use a tabela ASCII para resolver o problema.

print('Digite uma letra em maiúsculo: ')
letra = input()
letram = letra.lower()
print(f'A letra digitada foi "{letra}" e em minúsculo fica "{letram}"')

# 46. Faça um programa que leia um número inteiro positivo de três digitos (de 100 a 999).
# Gere outro numero formado pelos dígitos invertidos do número lido.

print('Digite um número de 3 digitos(100 a 999): ')
numero = input()
numerocontrario = numero[::-1]
print(f'O número {numero} invertido fica {numerocontrario}')

# 47. Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.

n = int(input('Digite um número de 4 dígitos (de 1000 a 9999): '))
print(n)
m = (int(n)//1000)%10
c = (int(n)//100)%10
d = (int(n)//10)%10
u = (int(n)//1)%10
print(f'{m}\n{c}\n{d}\n{u}')

# 48. Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.

segundos = int(input('Digite um tempo em segundos: '))
minutos = int(segundos)/60
horas = int(minutos)/60
print(f'{segundos} segundos ou {minutos} minutos ou {horas} horas')

# 49. Faça um programa para ler o horário (hora, minutos e segundo)
# de início e a duração, em segundos, de uma experiência biológica.
# O programa deve resultar com o novo horário (hora, minuto e segundo) do término da mesma.
print('Digite a hora, minuto e segundo em que a experiencia começou respectivamente: ')
hora = int(input('Hora: '))
minuto = int(input('Minuto: '))
segundo = int(input('Segundo: '))
print(f'Hora iniciada: {hora}:{minuto}:{segundo}')
print('Digite o tempo de duração em horas, minutos e segundos respectivamente: ')
horad = int(input('Horas de duração: '))
minutod = int(input('Minutos de duração: '))
segundod = int(input('Segundos de duração: '))
print(f'A experiencia durou: {hora}:{minuto}:{segundo}')
print(f'Hora do término da experiencia: {int(hora)+int(horad)}:{int(minuto)+int(minutod)}:{int(segundo)+int(segundod)}')
# obs.: se a soma de segundos ou minutos passar de 60 infelizmente n]ao há divisão 
# para deixar o horario correto, apenas com if/else/elif

# 50. Implemente um prgrama que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.
idade = int(input('Idade: '))
ano = int(input('Ano atual: '))
anon = int(ano)-int(idade)
print(f'Quem tem {idade} nasceu em {anon}')

# 51. Escreva um programa que leia as coordenadas x e y de pontos no R2 e calcule sua distância da origem (0,0)
x = float(input('Digite a coordenada x: '))
y = float(input('Digite a coordenada y: '))
print(f'Coordenada x:{x}\nCoordenada y:{y}')
distancia = ((float(x)**2)+(float(y)**2))**0.5
print(f'Distância do ponto ({x},{y}) do eixo (0,0) é {distancia}')

# 52. Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido
# proporcionalmente ao valor que cada deu para a realização da aposta. Faça um programa que leia quanto cada
# apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.

print('Digite o valor da aposta do maior apostador para o menor.')
p = float(input('Qual o valor do prêmio?'))
a = float(input('Quanto investiu o apostador A(maior aposta)?'))
b = float(input('Quanto investiu o apostador B?(aposta do meio)'))
c = float(input('Quanto investiu o apostador C?(menor aposta)'))
res_a = 0.5 * p
res_b = 0.35 * p
res_c = 0.15 * p
print(f'Proporcionalmente alinhado com o valor apostado o apostador A ganhou R${int(res_a)} reais.')
print(f'Proporcionalmente alinhado com o valor apostado o apostador B ganhou R${int(res_b)} reais.')
print(f'Proporcionalmente alinhado com o valor apostado o apostador C ganhou R${int(res_c)} reais.')

# 53. Faça um programa para ler as dimenções de um terreno (comprimento c e largura l),
# bem como o preço do metro de tela p. Imprima o custo para cercar este mersmo terreno com tela.

c = float(input('Comprimento do terreno em metros: '))
l = float(input('Largura do terreno em metros: '))
perimetro = (2*float(c))+(2*float(l))
preco = float(input('Preço do metro da tela: '))
print(f'Perímetro total do terreno: {perimetro}m\nTotal preço tela: R${float(preco)*float(perimetro)}')

"""


