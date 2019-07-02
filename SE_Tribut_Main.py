from SE_Tribut import SE_Tribut
from SE_Operation import SE_Operation
from pyknow import *

#Carga das constantes
regimeEmpresa = "Lucro Real"

#Carga dos dados informados pelo usuário
codNCM = input("Informe o NCM do produto")
tpMvto = input("Informe o tipo do movimento") #venda / compra / transferencia
carTrib = "consumidor"  #consumidor / varejo / distribuidor / simples

#Execução do sistema
engine = SE_Tribut()
engine.reset()

engine.declare(Fact(codNCM=codNCM))
engine.declare(Fact(tpMvto=tpMvto))
engine.declare(Fact(carTrib=carTrib))

# Teste,não precisa remover por enquanto
# pode ignorar a classe SE_Operation por enquanto também, foi um teste que fiz para retornar variável que não deu certo
# mas não quero remover ainda
#a = SE_Operation(xVar=codNCM)
#a = SE_Operation(xVar=codNCM)
#a.xVar = codNCM
#engine.declare(a)

engine.run()

print("COFINS")
print("CST: "+engine.r_cofins_cst)
print("Alíquota: "+str(engine.r_cofins_aliquota))
print("Código de Natureza: "+engine.r_cofins_natureza)