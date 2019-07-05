from pyknow import *
from tribut_base_fact import TributBaseFact

class IcmsEngine(KnowledgeEngine):
    def __init__(self, product):
        KnowledgeEngine.__init__(self)
        self.product = product
        self.aliquota = 0.0
        self.cst = ""

    @DefFacts()
    def _initial_action(self):
        yield TributBaseFact(regime_empresa="Lucro Real")

    # Definição de Pauta Fiscal - regra final, somente se a tributação for de ICMS-ST
    @Rule(TributBaseFact(codbarras=MATCH.codbarras), salience=5)
    def icms_pauta(self, codbarras):
        valor = float(0)
        if codbarras == "7896045501502":
            valor = 3.06
        elif codbarras == '7896045501489':
            valor = 2.00
        elif codbarras == '7896639663609':
            valor = 2.65
        elif codbarras == '7896052600328':
            valor = 3.40
        elif codbarras == '7891149102013':
            valor = 2.65
        elif codbarras == '7891991008662':
            valor = 12.80
        elif codbarras == '7897395050191':
            valor = 3.14
        elif codbarras == '7891991000796':
            valor = 2.58
        elif codbarras == '7891991000796':
            valor = 2.62
        elif codbarras == '0000078909182':
            valor = 3.63
        elif codbarras == '7896045506095':
            valor = 1.78
        elif codbarras == '7896045506095':
            valor = 1.77
        elif codbarras == '0000078905290':
            valor = 8.53
        elif codbarras == '0000078905351':
            valor = 6.31
        elif codbarras == '7891149030309':
            valor = 4.09
        elif codbarras == '0000078905276':
            valor = 6.31
        elif codbarras == '0000078904644':
            valor = 5.32
        elif codbarras == '7891149200405':
            valor = 6.94
        elif codbarras == '7891149010400':
            valor = 7.10

        self.declare(TributBaseFact(icms_pauta=valor))

    #Caso se trate de 1 - Mercadoria Estrangeira / 2 - Mercadoria Estrangeira Adquirida no Mercado Interno
    # 3 - Mercadoria nacional com conteúdo de importação superior a 40%
    # 6 - Mercadoria estrangeira com importação direta constante em lista de resolução CAMEX
    # 7 - Mercadoria estrangeira adquirida no mercado interno constante em lista de resolução CAMEX
    @Rule(TributBaseFact(origem=MATCH.origem),
          TributBaseFact(icms_cst='00'), salience=6)
    def icms_origem(self, origem):
        if origem in ('1', '2', '3', '6', '7'):
            self.declare(TributBaseFact(icms_aliquota=float(4)))

    # ICMS - Vendas
    # Venda consumidor
    @Rule(TributBaseFact(tp_mvto='venda'), TributBaseFact(car_trib='consumidor'),
          TributBaseFact(codNCM=MATCH.codNCM), salience=10)
    def icms_cst_venda_consumidor(self, codNCM):
        if codNCM in ('17049020', '19053100', '19059090', '21069029'):
            self.declare(TributBaseFact(icms_cst="00"))
        elif codNCM in ('08043000', '10063021'):
            self.declare(TributBaseFact(icms_cst="40"))
            self.cst = "40"
            self.declare(TributBaseFact(icms_aliquota=float(0)))
        elif codNCM in ('22030000', '22011000'):
            self.declare(TributBaseFact(icms_cst="60"))
            self.cst = "60"
            self.declare(TributBaseFact(icms_aliquota=float(0)))


    # Venda distribuidor
    @Rule(TributBaseFact(tp_mvto='venda'),
          OR(TributBaseFact(car_trib='distribuidor'), TributBaseFact(car_trib='simples'), TributBaseFact(car_trib='industria')),
          TributBaseFact(codNCM=MATCH.codNCM), salience=10)
    def icms_cst_venda_distribuidor(self, codNCM):
        if codNCM in ('17049020', '19053100', '19059090', '21069029'):
            self.declare(TributBaseFact(icms_cst="00"))
        elif codNCM in ('08043000', '10063021'):
            self.declare(TributBaseFact(icms_cst="40"))
            self.declare(TributBaseFact(icms_aliquota=float(0)))
        elif codNCM in ('22030000', '22011000'):
            self.declare(TributBaseFact(icms_cst="60"))
            self.declare(TributBaseFact(icms_aliquota=float(0)))


    #Venda CST 00
    @Rule(TributBaseFact(tp_mvto='venda'),
          TributBaseFact(car_trib='consumidor'),
          TributBaseFact(icms_cst="00"),
          TributBaseFact(codNCM=MATCH.codNCM), salience=9)
    def icms_aliquota_venda_consumidor(self, codNCM):
        if codNCM in ('19059090'):
            self.declare(TributBaseFact(icms_aliquota=float(7)))
        elif codNCM in ('21069029'):
            self.declare(TributBaseFact(icms_aliquota=float(8.4)))
        elif codNCM in ('19053100'):
            self.declare(TributBaseFact(icms_aliquota=float(12)))
        elif codNCM in ('17049020'):
            self.declare(TributBaseFact(icms_aliquota=float(18)))


    @Rule(TributBaseFact(tp_mvto='venda'),
          OR(TributBaseFact(car_trib='distribuidor'), TributBaseFact(car_trib='simples'), TributBaseFact(car_trib='industria')),
          TributBaseFact(icms_cst="00"),
          TributBaseFact(codNCM=MATCH.codNCM), salience=9)
    def icms_aliquota_venda_distribuidor(self, codNCM):
        if codNCM in ('19059090'):
           self.declare(TributBaseFact(icms_aliquota=float(7)))
        elif codNCM in ('21069029'):
            self.declare(TributBaseFact(icms_aliquota=float(8.4)))
        elif codNCM in ('19053100'):
           self.declare(TributBaseFact(icms_aliquota=float(12)))
        elif codNCM in ('17049020'):
           self.declare(TributBaseFact(icms_aliquota=float(18)))


    # ICMS - Compras
    @Rule(TributBaseFact(tp_mvto='compra'),
          TributBaseFact(car_trib='simples'),
          TributBaseFact(codNCM=MATCH.codNCM),salience=10)
    def icms_compra_simples(self, codNCM):
        if codNCM in ('17049020', '19053100', '19059090', '21069029', '08043000', '10063021'):
            self.declare(TributBaseFact(icms_cst="90"))
        elif codNCM in ('22030000', '22011000'):
            self.declare(TributBaseFact(icms_cst="10"))
            self.declare(TributBaseFact(icms_mva=140))
            self.declare(TributBaseFact(icms_st_aliquota=29))

    @Rule(TributBaseFact(tp_mvto='compra'),
          TributBaseFact(car_trib='distribuidor'),
          TributBaseFact(codNCM=MATCH.codNCM), salience=10)
    def icms_compra_distribuidor(self, codNCM):
        if codNCM in ('08043000', '10063021'):
            self.declare(TributBaseFact(icms_cst="40"))
        elif codNCM in ('19053100', '19059090'):
            self.declare(TributBaseFact(icms_cst="00"))
            if codNCM in ('19053100'):
                self.declare(TributBaseFact(icms_aliquota=float(12)))
            elif codNCM in ('19059090'):
                self.declare(TributBaseFact(icms_aliquota=float(7)))
        elif codNCM in ('21069029', '17049020'):
            self.declare(TributBaseFact(icms_cst="20"))
            self.declare(TributBaseFact(icms_aliquota=float(18)))
            self.declare(TributBaseFact(icms_reducao=33.33))
        elif codNCM in ('22030000', '22011000'):
            self.declare(TributBaseFact(icms_cst="60"))


    @Rule(TributBaseFact(tp_mvto='compra'),
          TributBaseFact(car_trib='industria'),
          TributBaseFact(codNCM=MATCH.codNCM), salience=float(10))
    def icms_compra_industria(self, codNCM):
        if codNCM in ('08043000', '10063021'):
            self.declare(TributBaseFact(icms_cst="40"))
        elif codNCM in ('19053100', '19059090'):
            self.declare(TributBaseFact(icms_cst="00"))
            if codNCM in ('19053100'):
                self.declare(TributBaseFact(icms_aliquota=float(12)))
            elif codNCM in ('19059090'):
                self.declare(TributBaseFact(icms_aliquota=float(7)))
        elif codNCM in ('21069029', '17049020'):
            self.declare(TributBaseFact(icms_cst="20"))
            self.declare(TributBaseFact(icms_aliquota=float(18)))
            self.declare(TributBaseFact(icms_reducao=33.33))
        elif codNCM in ('22030000', '22011000'):
            self.declare(TributBaseFact(icms_cst="10"))
            self.declare(TributBaseFact(icms_mva=140))
            self.declare(TributBaseFact(icms_st_aliquota=float(29)))

    # ICMS - Bonificação
    @Rule(TributBaseFact(tp_mvto='bonificacao'),
          TributBaseFact(car_trib='simples'),
          TributBaseFact(codNCM=MATCH.codNCM), salience=10)
    def icms_bonif_simples(self, codNCM):
        if codNCM in ('17049020', '19053100', '19059090', '21069029', '08043000', '10063021'):
            self.declare(TributBaseFact(icms_cst="90"))
        elif codNCM in ('22030000', '22011000'):
            self.declare(TributBaseFact(icms_cst="10"))
            self.declare(TributBaseFact(icms_mva=140))
            self.declare(TributBaseFact(icms_st_aliquota=float(29)))

    @Rule(TributBaseFact(tp_mvto='bonificacao'),
          TributBaseFact(car_trib='distribuidor'),
          TributBaseFact(codNCM=MATCH.codNCM), salience=10)
    def icms_bonif_distribuidor(self, codNCM):
        if codNCM in ('08043000', '10063021'):
            self.declare(TributBaseFact(icms_cst="40"))
        elif codNCM in ('19053100', '19059090'):
            self.declare(TributBaseFact(icms_cst="00"))
            if codNCM in ('19053100'):
                self.declare(TributBaseFact(icms_aliquota=float(12)))
            elif codNCM in ('19059090'):
                self.declare(TributBaseFact(icms_aliquota=float(7)))
        elif codNCM in ('21069029', '17049020'):
            self.declare(TributBaseFact(icms_cst="20"))
            self.declare(TributBaseFact(icms_aliquota=float(18)))
            self.declare(TributBaseFact(icms_reducao=33.33))
        elif codNCM in ('22030000', '22011000'):
            self.declare(TributBaseFact(icms_cst="60"))

    @Rule(TributBaseFact(tp_mvto='bonificacao'),
          TributBaseFact(car_trib='industria'),
          TributBaseFact(codNCM=MATCH.codNCM), salience=10)
    def icms_bonif_industria(self, codNCM):
        if codNCM in ('08043000', '10063021'):
            self.declare(TributBaseFact(icms_cst="40"))
        elif codNCM in ('19053100', '19059090'):
            self.declare(TributBaseFact(icms_cst="00"))
            if codNCM in ('19053100'):
                self.declare(TributBaseFact(icms_aliquota=float(12)))
            elif codNCM in ('19059090'):
                self.declare(TributBaseFact(icms_aliquota=float(7)))
        elif codNCM in ('21069029', '17049020'):
            self.declare(TributBaseFact(icms_cst="20"))
            self.declare(TributBaseFact(icms_aliquota=float(18)))
            self.declare(TributBaseFact(icms_reducao=33.33))
        elif codNCM in ('22030000', '22011000'):
            self.declare(TributBaseFact(icms_cst="10"))
            self.declare(TributBaseFact(icms_mva=float(140)))
            self.declare(TributBaseFact(icms_st_aliquota=float(29)))


    # ICMS - Perdas
    @Rule(TributBaseFact(tp_mvto='perdas'),
          TributBaseFact(codNCM=MATCH.codNCM), salience=10)
    def icms_perdas(self, codNCM):
        if codNCM in ('19059090'):
            self.declare(TributBaseFact(icms_cst="00"))
            self.declare(TributBaseFact(icms_aliquota=float(7)))
        elif codNCM in ('17049020', '19053100', '21069029'):
            self.declare(TributBaseFact(icms_cst="20"))
            if codNCM in ('19053100'):
                self.declare(TributBaseFact(icms_aliquota=float(12)))
                self.declare(TributBaseFact(icms_reducao=41.6667))
            elif codNCM in ('17049020', '21069029'):
                self.declare(TributBaseFact(icms_aliquota=float(18)))
                self.declare(TributBaseFact(icms_reducao=33.33))
        elif codNCM in ('08043000', '10063021'):
            self.declare(TributBaseFact(icms_cst="40"))
        elif codNCM in ('22030000', '22011000'):
            self.declare(TributBaseFact(icms_cst="60"))

    # IPI - Compras
    @Rule(TributBaseFact(tp_mvto='compra'),
          TributBaseFact(car_trib='industria'),
          TributBaseFact(codNCM=MATCH.codNCM), salience=10)
    def ipi_compras(self, codNCM):
        if codNCM in ('22030000', '22011000'):
            self.declare(TributBaseFact(ipi_cst="00"))  #49 - Outras Entradas
            self.declare(TributBaseFact(ipi_aliquota=4.8))
        elif codNCM in ('22041010'):
            self.declare(TributBaseFact(icms_cst="00"))
            self.declare(TributBaseFact(ipi_aliquota=10))