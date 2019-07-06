from pyknow import *
from tribut_base_fact import TributBaseFact

class CofinsEngine(KnowledgeEngine):
    cofins_aliq_basica = 0
    pis_aliq_basica = 0

    def __init__(self, product):
        KnowledgeEngine.__init__(self)
        self.product = product
        self.aliquota_cofins = 0
        self.cofins_cst = ""
        self.cofins_natureza = ""
        self.aliquota_pis = 0

    @DefFacts()
    def _initial_action(self):
        yield TributBaseFact(regime_empresa='Lucro Real')

    @Rule(TributBaseFact(regime_empresa='Lucro Real'), salience=10)
    def cofins_aliq_basica_lucro_real(self):
        self.cofins_aliq_basica = 7.6
        self.pis_aliq_basica = 1.65

    @Rule(NOT(TributBaseFact(regime_empresa='Lucro Real')), salience=10)
    def cofins_aliq_basica_lucro_presumido(self):
        self.cofins_aliq_basica = 3
        self.pis_aliq_basica = 0.65

    @Rule(OR(TributBaseFact(cofins_cst='01'), TributBaseFact(cofins_cst='50')), salience=8)
    def cofins_tributacao_01_50(self):
        self.aliquota_cofins = self.cofins_aliq_basica
        self.aliquota_pis = self.pis_aliq_basica

    @Rule(TributBaseFact(cofins_cst='04'),
          TributBaseFact(codNCM=MATCH.codNCM), salience=8)
    def cofins_tributacao_04(self, codNCM):
        if codNCM in ('22071090'):
            self.cofins_natureza='112'
        elif codNCM in ('08119000', '22021000'):
            self.cofins_natureza='202'
        elif codNCM in ('22011000', '22029000'):
            self.cofins_natureza='420'
        elif codNCM in ('22030000'):
            self.cofins_natureza='423'
        elif codNCM in ('22011000'):
            self.cofins_natureza='424'

        self.declare(TributBaseFact(cofins_natureza=self.cofins_natureza))

    @Rule(TributBaseFact(cofins_cst='05'),
          TributBaseFact(codNCM=MATCH.codNCM), salience=8)
    def cofins_tributacao_05(self, codNCM):
        if codNCM in ('24022000'):
            self.cofins_natureza='101'

        self.declare(TributBaseFact(cofins_natureza=self.cofins_natureza))

    @Rule(TributBaseFact(cofins_cst='06'),
          TributBaseFact(codNCM=MATCH.codNCM), salience=8)
    def cofins_tributacao_06(self, codNCM):
        if codNCM in ('04012010', '04012110', '04014010'):
            self.cofins_natureza='110'
        elif codNCM in ('08043000', '10063021'):
            self.cofins_natureza='116'
        elif codNCM in ('02012010', '02012020', '02012090'):
            self.cofins_natureza='121'
        elif codNCM in ('03038943', '03038955', '03038963', '03038990'):
            self.cofins_natureza='122'

        self.declare(TributBaseFact(cofins_natureza=self.cofins_natureza))

    # COFINS - Vendas
    @Rule(TributBaseFact(tp_mvto='venda'),
          TributBaseFact(codNCM=MATCH.codNCM), salience=9)
    def cofins_venda_cst_t(self, codNCM):
        if codNCM in ('19053100', '19059090', '21069029', '17049020'):
            self.cofins_cst='01'
        elif codNCM in ('22030000', '22011000'):
            self.cofins_cst='04'
        elif codNCM in ('08043000', '10063021'):
            self.cofins_cst='06'

        self.declare(TributBaseFact(cofins_cst=self.cofins_cst))

    # COFINS - Compras
    @Rule(TributBaseFact(tp_mvto='compra'),
          #OR(TributBaseFact(car_trib='distribuidor'), TributBaseFact(car_trib='simples'), TributBaseFact(car_trib='industria')),
          TributBaseFact(codNCM=MATCH.codNCM), salience=9)
    def cofins_compra_cst_t(self, codNCM):
        if codNCM in ('19053100', '19059090', '21069029', '17049020'):
            self.cofins_cst='50'  #Operação com direito a crédito
        elif codNCM in ('22030000', '08119000', '22021000', '22011000'):
            self.cofins_cst='70'  #Operação de aquisição sem direito a crédito
        #elif ncm in ('5'):
        #    self.cofins_cst='72'  #Operação de aquisição com isenção
        elif codNCM in ('08043000', '02012010', '02012090', '10063021'):
            self.cofins_cst='73'  #Operação de aquisição com alíquota zero
        elif codNCM in ('24022000'):
            self.cofins_cst='75'  #Operação de aquisição por substituição tributária

        self.declare(TributBaseFact(cofins_cst=self.cofins_cst))

    # COFINS - Bonificação
    @Rule(TributBaseFact(tp_mvto='bonificacao'), salience=9)
    def cofins_bonificacao_cst(self):
        self.cofins_cst='70'
        self.declare(TributBaseFact(cofins_cst=self.cofins_cst))

    # COFINS - Perdas
    @Rule(TributBaseFact(tp_mvto='perdas'),
          TributBaseFact(codNCM=MATCH.codNCM), salience=9)
    def cofins_perdas_cst(self, codNCM):
        if codNCM in ('19053100', '19059090', '21069029', '17049020'):
            self.cofins_cst='01'
        elif codNCM in ('22030000', '22011000'):
            self.cofins_cst ='04'
        elif codNCM in ('08043000', '10063021'):
            self.cofins_cst='06'

        self.declare(TributBaseFact(cofins_cst=self.cofins_cst))