from icms_engine import IcmsEngine
from tribut_base_fact import TributBaseFact
from product import Product
from pyknow import *

#Carga dos dados informados pelo usuário
ncm_code = input("Informe o NCM do produto")
tp_mvto = input("Informe o tipo do movimento (venda / compra)") #venda / compra / bonificacao / perdas
car_trib = input("Informe o tipo de carga tributária (consumidor / industria / distribuidor / simples)")

product = Product('normal', 1)
product(ncm_code=ncm_code)
product(tp_mvto=tp_mvto)
product(car_trib=car_trib)
#Execução do sistema
engine = IcmsEngine(product)
engine.reset()

engine.declare(TributBaseFact(ncm_code=ncm_code))
engine.declare(TributBaseFact(tp_mvto=tp_mvto))
engine.declare(TributBaseFact(car_trib=car_trib))

engine.run()

print(engine.facts)
