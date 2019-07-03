from pyknow import *
from icms_fact import IcmsFact
from tribut_base_fact import TributBaseFact

class IcmsEngine(KnowledgeEngine):

    #Variáveis de resultado
    icms_aliquota = 0
    icms_cst = ""
    icms_reducao = 0
    icms_st_mva = 0
    icms_st_pauta = 0
    icms_st_reducao = 0
    icms_st_aliq_credito = 0
    icms_st_aliq_debito = 0


    @DefFacts()
    def _initial_action(self):
        yield IcmsFact(regime_empresa="Lucro Real")

    # ICMS - Vendas
    @Rule(TributBaseFact(tp_mvto='venda', car_trib='consumidor'), salience=10)
    def icms_cst_venda_consumidor(self):
        print(1)
        #if (codNCM in ['123']):
        self.declare(IcmsFact(icms_cst="00"))

        #Senão se estiver na lista dos isentos
        self.declare(IcmsFact(icms_cst="40"))
        self.declare(IcmsFact(icms_aliquota=0))

        #Senão se estiver na lista de ICMS ST
        self.declare(IcmsFact(icms_cst="60"))
        self.declare(IcmsFact(icms_aliquota=0))


    @Rule(IcmsFact(tp_mvto='venda'),
          OR(IcmsFact(car_trib='distribuidor'), IcmsFact(car_trib='simples'), IcmsFact(car_trib='varejo')), salience=10)
    def icms_cst_venda_distribuidor(self):
        # if (codNCM in ['123']):
        self.declare(IcmsFact(icms_cst="00"))

        # Senão se estiver na lista dos isentos
        self.declare(IcmsFact(icms_cst="40"))
        self.declare(IcmsFact(icms_aliquota=0))

        # Senão se estiver na lista de ICMS ST
        self.declare(IcmsFact(icms_cst="60"))
        self.declare(IcmsFact(icms_aliquota=0))
        # Senão gerar erro

    @Rule(IcmsFact(tp_mvto='venda'),
          IcmsFact(car_trib='consumidor'),
          IcmsFact(icms_cst="00"), salience=9)
    def icms_aliquota_venda_consumidor(self):
        print(2)
        # Se estiver na lista dos itens a 7%
        self.declare(IcmsFact(icms_aliquota=7))

        # Se estiver na lista dos itens a 8.4%
        self.declare(IcmsFact(icms_aliquota=8.4))

        # Se estiver na lista dos itens a 12%
        self.declare(IcmsFact(icms_aliquota=12))

        # Se estiver na lista dos itens a 18%
        self.declare(IcmsFact(icms_aliquota=18))

        # Se estiver na lista dos itens a 29%
        self.declare(IcmsFact(icms_aliquota=29))

    @Rule(IcmsFact(tp_mvto='venda'),
          OR(IcmsFact(car_trib='distribuidor'),IcmsFact(car_trib='simples'),IcmsFact(car_trib='varejo')),
          IcmsFact(icms_cst="00"), salience=9)
    def icms_aliquota_venda_distribuidor(self):
        # Se estiver na lista dos itens a 7%
        self.declare(IcmsFact(icms_aliquota=7))

        # Se estiver na lista dos itens a 8.4%
        self.declare(IcmsFact(icms_aliquota=8.4))

        # Se estiver na lista dos itens a 12%
        self.declare(IcmsFact(icms_aliquota=12))

        # Se estiver na lista dos itens a 18%
        self.declare(IcmsFact(icms_aliquota=18))

        # Se estiver na lista dos itens a 29%
        self.declare(IcmsFact(icms_aliquota=29))


    # ICMS - Compras
    @Rule(IcmsFact(tp_mvto='compra'), IcmsFact(car_trib='simples'), salience=10)
    def icms_cst_compra_simples(self):
        # if (codNCM in ['123']):
        self.declare(IcmsFact(icms_cst="00"))

        # Senão se estiver na lista dos isentos
        self.declare(IcmsFact(icms_cst="40"))
        self.declare(IcmsFact(icms_aliquota=0))

        # Senão se estiver na lista de ICMS ST
        self.declare(IcmsFact(icms_cst="60"))
        self.declare(IcmsFact(icms_aliquota=0))
        # Senão gerar erro

    @Rule(IcmsFact(tp_mvto='compra'),
          IcmsFact(car_trib='simples'),
          IcmsFact(icms_cst="00"), salience=9)
    def icms_aliquota_venda_distribuidor(self):
        # Se estiver na lista dos itens a 7%
        self.declare(IcmsFact(icms_aliquota=7))

        # Se estiver na lista dos itens a 8.4%
        self.declare(IcmsFact(icms_aliquota=8.4))

        # Se estiver na lista dos itens a 12%
        self.declare(IcmsFact(icms_aliquota=12))

        # Se estiver na lista dos itens a 18%
        self.declare(IcmsFact(icms_aliquota=18))

        # Se estiver na lista dos itens a 29%
        self.declare(IcmsFact(icms_aliquota=29))

    @Rule(IcmsFact(tp_mvto='compra'),
          IcmsFact(car_trib='simples'),
          IcmsFact(icms_cst="20"), salience=9)
    def icms_aliquota_venda_distribuidor(self):
        # Se estiver na lista dos itens a 7%
        self.declare(IcmsFact(icms_aliquota=7))

        # Se estiver na lista dos itens a 8.4%
        self.declare(IcmsFact(icms_aliquota=8.4))

        # Se estiver na lista dos itens a 12%
        self.declare(IcmsFact(icms_aliquota=12))

        # Se estiver na lista dos itens a 18%
        self.declare(IcmsFact(icms_aliquota=18))

        # Se estiver na lista dos itens a 29%
        self.declare(IcmsFact(icms_aliquota=29))
