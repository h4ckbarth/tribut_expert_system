from pyknow import *
from tribut_base_fact import TributBaseFact

class IcmsEngine(KnowledgeEngine):
    def __init__(self, product):
        KnowledgeEngine.__init__(self)
        self.product = product

    def choose_cst(self):
        if self.product.cst == 'normal':
            self.declare(TributBaseFact(icms_cst="00"))
        elif self.product.cst == 'exempt':
            self.declare(TributBaseFact(icms_cst="40"))
            self.declare(TributBaseFact(icms_aliquota=float(0)))
        elif self.product.cst == 'icms_st':
            self.declare(TributBaseFact(icms_cst="60"))
            self.declare(TributBaseFact(icms_aliquota=float(0)))

    def choose_range_list(self):
        # Escolhe a aliquota pelas faixas de imposto
        if self.product.range_list == 1:
            self.declare(TributBaseFact(icms_aliquota=float(7)))
        elif self.product.range_list == 2:
            # Se estiver na lista dos itens a 8.4%
            self.declare(TributBaseFact(icms_aliquota=float(8.4)))
        elif self.product.range_list == 3:
            # Se estiver na lista dos itens a 12%
            self.declare(TributBaseFact(icms_aliquota=float(12)))
        elif self.product.range_list == 4:
            # Se estiver na lista dos itens a 18%
            self.declare(TributBaseFact(icms_aliquota=float(18)))
        elif self.product.range_list == 5:
            # Se estiver na lista dos itens a 29%
            self.declare(TributBaseFact(icms_aliquota=float(29)))


    @DefFacts()
    def _initial_action(self):
        yield TributBaseFact(regime_empresa="Lucro Real")


    # ICMS - Vendas
    # Venda consumidor
    @Rule(TributBaseFact(tp_mvto='venda'), TributBaseFact(car_trib='consumidor'), salience=10)
    def icms_cst_venda_consumidor(self):
        self.choose_cst()


    # Venda distribuidor
    @Rule(TributBaseFact(tp_mvto='venda'),
          OR(TributBaseFact(car_trib='distribuidor'), TributBaseFact(car_trib='simples'), TributBaseFact(car_trib='varejo')), salience=10)
    def icms_cst_venda_distribuidor(self):
        self.choose_cst()


    #Venda CST 00
    @Rule(TributBaseFact(tp_mvto='venda'),
          TributBaseFact(car_trib='consumidor'),
          TributBaseFact(icms_cst="00"), salience=9)
    def icms_aliquota_venda_consumidor(self):
        self.choose_range_list()


    @Rule(TributBaseFact(tp_mvto='venda'),
          OR(TributBaseFact(car_trib='distribuidor'),TributBaseFact(car_trib='simples'),TributBaseFact(car_trib='varejo')),
          TributBaseFact(icms_cst="00"), salience=9)
    def icms_aliquota_venda_distribuidor(self):
       self.choose_range_list()


    # ICMS - Compras
    @Rule(TributBaseFact(tp_mvto='compra'), TributBaseFact(car_trib='simples'), salience=10)
    def icms_cst_compra_simples(self):
        self.choose_cst()


    @Rule(TributBaseFact(tp_mvto='compra'),
          TributBaseFact(car_trib='simples'),
          TributBaseFact(icms_cst="00"), salience=9)
    def icms_aliquota_venda_distribuidor(self):
        self.choose_range_list()


    @Rule(TributBaseFact(tp_mvto='compra'),
          TributBaseFact(car_trib='simples'),
          TributBaseFact(icms_cst="20"), salience=9)
    def icms_aliquota_venda_distribuidor(self):
        self.choose_range_list()
