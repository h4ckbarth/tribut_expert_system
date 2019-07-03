from icms_engine import IcmsEngine
from tribut_base_fact import TributBaseFact
from pyknow import *

#Carga dos dados informados pelo usuário
ncm_code = input("Informe o NCM do produto")
tp_mvto = input("Informe o tipo do movimento (venda / compra)") #venda / compra
car_trib = input("Informe o tipo de carga tributária (consumidor / varejo / distribuidor / simples)")

#Execução do sistema
engine = IcmsEngine()
engine.reset()

engine.declare(TributBaseFact(ncm_code=ncm_code, tp_mvto=tp_mvto, car_trib=car_trib))

engine.run()

print(engine.facts)