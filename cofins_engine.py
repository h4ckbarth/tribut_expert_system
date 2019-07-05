from pyknow import *
from tribut_expert_system.tribut_base_fact import TributBaseFact

class CofinsEngine(KnowledgeEngine):
    cofins_aliq_basica = 0

    def __init__(self, product):
        KnowledgeEngine.__init__(self)
        self.product = product

    @DefFacts()
    def _initial_action(self):
        yield TributBaseFact(regime_empresa="Lucro Real")

    @Rule(TributBaseFact(regimeEmpresa="Lucro Real"), salience=10)
    def cofins_aliq_basica_lucro_real(self):
        self.cofins_aliq_basica=7.6

    @Rule(NOT(TributBaseFact(regimeEmpresa="Lucro Real")), salience=10)
    def cofins_aliq_basica_lucro_presumido(self):
        self.cofins_aliq_basica=3

    @Rule(TributBaseFact(cofins_venda_cst="01"), salience=8)
    def cofins_tributacao_01(self):
        self.r_cofins_aliquota = self.cofins_aliq_basica

    @Rule(TributBaseFact(cofins_venda_cst="04"),
          TributBaseFact(codNCM=MATCH.ncm), salience=8)
    def cofins_tributacao_04(self, ncm):
        if ncm in ('22071090'):
            self.declare(TributBaseFact(cofins_natureza="112"))
        elif ncm in ('08119000', '22021000'):
            self.declare(TributBaseFact(cofins_natureza="202"))
        elif ncm in ('22011000', '22029000'):
            self.declare(TributBaseFact(cofins_natureza="420"))
        elif ncm in ('22030000'):
            self.declare(TributBaseFact(cofins_natureza="423"))
        elif ncm in ('22030000'):
            self.declare(TributBaseFact(cofins_natureza="424"))

    @Rule(TributBaseFact(cofins_venda_cst="05"),
          TributBaseFact(codNCM=MATCH.ncm), salience=8)
    def cofins_tributacao_05(self, ncm):
        if ncm in ('24022000'):
            self.declare(TributBaseFact(cofins_natureza="101"))

    @Rule(TributBaseFact(cofins_venda_cst="06"),
          TributBaseFact(codNCM=MATCH.ncm), salience=8)
    def cofins_tributacao_06(self, ncm):
        if ncm in ('04012010', '04012110', '04014010'):
            self.declare(TributBaseFact(cofins_natureza="110"))
        elif ncm in ('08043000'):
            self.declare(TributBaseFact(cofins_natureza="116"))
        elif ncm in ('02012010', '02012020', '02012090'):
            self.declare(TributBaseFact(cofins_natureza="121"))
        elif ncm in ('03038943', '03038955', '03038963', '03038990'):
            self.declare(TributBaseFact(cofins_natureza="122"))

    # COFINS - Vendas
    @Rule(TributBaseFact(tpMvto='venda'),
          TributBaseFact(codNCM=MATCH.ncm), salience=9)
    def cofins_venda_cst(self, codNCM):
        if codNCM in ('19053100', '19059090', '21069090', '17049020'):
            self.declare(TributBaseFact(cofins_cst="01"))
        elif codNCM in ('22030000'):
            self.declare(TributBaseFact(cofins_cst="04"))
        elif codNCM in ('08043000'):
            self.declare(TributBaseFact(cofins_cst="06"))

    # COFINS - Compras
    @Rule(TributBaseFact(tpMvto='compra'),
          OR(TributBaseFact(car_trib='distribuidor'), TributBaseFact(car_trib='simples'), TributBaseFact(car_trib='industria')),
          TributBaseFact(codNCM=MATCH.ncm), salience=9)
    def cofins_compra_cst(self, ncm):
        if ncm in ('19053100', '19059090', '21069090', '17049020'):
            self.declare(TributBaseFact(cofins_cst="50"))  #Operação com direito a crédito
        elif ncm in ('22030000', '08119000', '22021000'):
            self.declare(TributBaseFact(cofins_cst="70"))  #Operação de aquisição sem direito a crédito
        #elif ncm in ('5'):
        #    self.declare(TributBaseFact(cofins_cst="72"))  #Operação de aquisição com isenção
        elif ncm in ('08043000', '02012010', '02012090'):
            self.declare(TributBaseFact(cofins_cst="73"))  #Operação de aquisição com alíquota zero
        elif ncm in ('24022000'):
            self.declare(TributBaseFact(cofins_cst="75"))  #Operação de aquisição por substituição tributária

    # COFINS - Bonificação
    @Rule(TributBaseFact(tpMvto='bonificacao'), salience=9)
    def cofins_transferencia_cst(self, ncm):
        self.declare(TributBaseFact(cofins_cst="70"))

    # COFINS - Perdas
    @Rule(TributBaseFact(tpMvto='perdas'),
          TributBaseFact(codNCM=MATCH.ncm), salience=9)
    def cofins_venda_cst(self, codNCM):
        if codNCM in ('19053100', '19059090', '21069090', '17049020'):
            self.declare(TributBaseFact(cofins_cst="01"))
        elif codNCM in ('22030000'):
            self.declare(TributBaseFact(cofins_cst="04"))
        elif codNCM in ('08043000'):
            self.declare(TributBaseFact(cofins_cst="06"))
