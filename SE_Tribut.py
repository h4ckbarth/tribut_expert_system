from pyknow import *

class SE_Tribut(KnowledgeEngine):
    #Variáveis internas
    cofins_aliq_basica = 0

    #Variáveis de resultado
    r_icms_aliquota = 0
    r_icms_cst = ""
    r_icms_reducao = 0
    r_icms_st_mva = 0
    r_icms_st_pauta = 0
    r_icms_st_reducao = 0
    r_icms_st_aliq_credito = 0
    r_icms_st_aliq_debito = 0
    r_ipi_aliquota = 0
    r_ipi_cst = ""
    r_pis_aliquota = 0
    r_pis_cst = ""
    r_pis_natureza = ""
    r_cofins_aliquota = 0
    r_cofins_cst = ""
    r_cofins_natureza = ""

    @DefFacts()
    def _initial_action(self):
        #Rever - Carregar com base em arquivo de constantes
        yield Fact(regimeEmpresa="Lucro Real")

    # *****************************************
    # Regras específicas de ICMS
    # *****************************************

    # ICMS - Vendas
    @Rule(Fact(tpMvto='venda'),
          Fact(carTrib='consumidor'), salience=10)
    def icms_cst_venda_consumidor(self):
        #if (codNCM in ['123']):
        self.declare(Fact(icms_cst="00"))
        #    print('XXYY')
        #Senão se estiver na lista dos isentos
        self.declare(Fact(icms_cst="40"))
        self.declare(Fact(icms_aliquota=0))
        #Senão se estiver na lista de ICMS ST
        self.declare(Fact(icms_cst="60"))
        self.declare(Fact(icms_aliquota=0))
        #Senão gerar erro

    @Rule(Fact(tpMvto='venda'),
          OR(Fact(carTrib='distribuidor'), Fact(carTrib='simples'), Fact(carTrib='varejo')), salience=10)
    def icms_cst_venda_distribuidor(self):
        # if (codNCM in ['123']):
        self.declare(Fact(icms_cst="00"))
        # print('XXYY')
        # Senão se estiver na lista dos isentos
        self.declare(Fact(icms_cst="40"))
        self.declare(Fact(icms_aliquota=0))
        # Senão se estiver na lista de ICMS ST
        self.declare(Fact(icms_cst="60"))
        self.declare(Fact(icms_aliquota=0))
        # Senão gerar erro

    @Rule(Fact(tpMvto='venda'),
          Fact(carTrib='consumidor'),
          Fact(icms_cst="00"), salience=9)
    def icms_aliquota_venda_consumidor(self):
        # Se estiver na lista dos itens a 7%
        self.declare(Fact(icms_aliquota=7))
        # Se estiver na lista dos itens a 8.4%
        self.declare(Fact(icms_aliquota=8.4))
        # Se estiver na lista dos itens a 12%
        self.declare(Fact(icms_aliquota=12))
        # Se estiver na lista dos itens a 18%
        self.declare(Fact(icms_aliquota=18))
        # Se estiver na lista dos itens a 29%
        self.declare(Fact(icms_aliquota=29))
        # Senão gerar erro

    @Rule(Fact(tpMvto='venda'),
          OR(Fact(carTrib='distribuidor'),Fact(carTrib='simples'),Fact(carTrib='varejo')),
          Fact(icms_cst="00"), salience=9)
    def icms_aliquota_venda_distrib(self):
        # Se estiver na lista dos itens a 7%
        self.declare(Fact(icms_aliquota=7))
        # Se estiver na lista dos itens a 8.4%
        self.declare(Fact(icms_aliquota=8.4))
        # Se estiver na lista dos itens a 12%
        self.declare(Fact(icms_aliquota=12))
        # Se estiver na lista dos itens a 18%
        self.declare(Fact(icms_aliquota=18))
        # Se estiver na lista dos itens a 29%
        self.declare(Fact(icms_aliquota=29))
        # Senão gerar erro

    # ICMS - Compras
    @Rule(Fact(tpMvto='compra'), Fact(carTrib='simples'), salience=10)
    def icms_cst_compra_simples(self):
        # if (codNCM in ['123']):
        self.declare(Fact(icms_cst="00"))
        # Senão se estiver na lista dos isentos
        self.declare(Fact(icms_cst="40"))
        self.declare(Fact(icms_aliquota=0))
        # Senão se estiver na lista de ICMS ST
        self.declare(Fact(icms_cst="60"))
        self.declare(Fact(icms_aliquota=0))
        # Senão gerar erro

    @Rule(Fact(tpMvto='compra'),
          Fact(carTrib='simples'),
          Fact(icms_cst="00"), salience=9)
    def icms_aliquota_venda_distrib(self):
        # Se estiver na lista dos itens a 7%
        self.declare(Fact(icms_aliquota=7))
        # Se estiver na lista dos itens a 8.4%
        self.declare(Fact(icms_aliquota=8.4))
        # Se estiver na lista dos itens a 12%
        self.declare(Fact(icms_aliquota=12))
        # Se estiver na lista dos itens a 18%
        self.declare(Fact(icms_aliquota=18))
        # Se estiver na lista dos itens a 29%
        self.declare(Fact(icms_aliquota=29))
        # Senão gerar erro

    @Rule(Fact(tpMvto='compra'),
          Fact(carTrib='simples'),
          Fact(icms_cst="20"), salience=9)
    def icms_aliquota_venda_distrib(self):
        # Se estiver na lista dos itens a 7%
        self.declare(Fact(icms_aliquota=7))
        # Se estiver na lista dos itens a 8.4%
        self.declare(Fact(icms_aliquota=8.4))
        # Se estiver na lista dos itens a 12%
        self.declare(Fact(icms_aliquota=12))
        # Se estiver na lista dos itens a 18%
        self.declare(Fact(icms_aliquota=18))
        # Se estiver na lista dos itens a 29%
        self.declare(Fact(icms_aliquota=29))
        # Senão gerar erro

    # ICMS - Transferências

    # *****************************************
    # Regras específicas de IPI
    # *****************************************

    # *****************************************
    # Regras específicas de PIS/PASEP
    # *****************************************
    # PIS - Vendas

    @Rule(Fact(tpMvto='vendas'))
    def pis_venda(self):
        print("venda pis")

    # *****************************************
    # Regras específicas de COFINS
    # *****************************************
    @Rule(Fact(regimeEmpresa="Lucro Real"), salience=10)
    def cofins_aliq_basica_lucro_real(self):
        self.cofins_aliq_basica=7.6
        print(str(self.cofins_aliq_basica))

    @Rule(NOT(Fact(regimeEmpresa="Lucro Real")), salience=10)
    def cofins_aliq_basica_lucro_presumido(self):
        self.cofins_aliq_basica=3
        print(str(self.cofins_aliq_basica))

    # COFINS - Vendas
    @Rule(Fact(tpMvto='venda'), Fact(codNCM=MATCH.ncm), salience=9)
    def cofins_venda_cst(self, ncm):
        is_valid = True
        if ncm in ('1', '2'):
            self.r_cofins_cst = "01"
        elif ncm in ('4'):
            self.r_cofins_cst = "04"
        elif ncm in ('5'):
            self.r_cofins_cst = "05"
        elif ncm in ('6'):
            self.r_cofins_cst = "06"
        else:
            is_valid = False

        if is_valid:
            self.declare(Fact(cofins_venda_cst=self.r_cofins_cst))
        else:
            print('Não foi possível definir o CST de COFINS para a operação')

    @Rule(Fact(tpMvto='venda'),
          Fact(cofins_venda_cst="01"), salience=8)
    def cofins_tributacao_venda_01(self):
        self.r_cofins_aliquota = self.cofins_aliq_basica

    @Rule(Fact(tpMvto='venda'),
          Fact(cofins_venda_cst="04"), Fact(codNCM=MATCH.ncm), salience=8)
    def cofins_tributacao_venda_04(self, ncm):
        is_valid = True
        if ncm in ('1', '2'):
            self.r_cofins_natureza = "101"
        elif ncm in ('4'):
            self.r_cofins_natureza = "102"
        elif ncm in ('5'):
            self.r_cofins_natureza = "103"
        else:
            is_valid = False

        if not is_valid:
            print('Não foi possível definir o Código de Natureza de COFINS para a operação')

    @Rule(Fact(tpMvto='venda'),
          Fact(cofins_venda_cst="05"), Fact(codNCM=MATCH.ncm), salience=8)
    def cofins_tributacao_venda_05(self, ncm):
        is_valid = True
        if ncm in ('1', '2'):
            self.r_cofins_natureza = "101"
        elif ncm in ('4'):
            self.r_cofins_natureza = "102"
        elif ncm in ('5'):
            self.r_cofins_natureza = "103"
        else:
            is_valid = False

        if not is_valid:
            print('Não foi possível definir o Código de Natureza de COFINS para a operação')

    @Rule(Fact(tpMvto='venda'),
          Fact(cofins_venda_cst="06"), Fact(codNCM=MATCH.ncm), salience=8)
    def cofins_tributacao_venda_06(self, ncm):
        is_valid = True
        if ncm in ('1', '2'):
            self.r_cofins_natureza = "101"
        elif ncm in ('4'):
            self.r_cofins_natureza = "102"
        elif ncm in ('5'):
            self.r_cofins_natureza = "103"
        else:
            is_valid = False

        if not is_valid:
            print('Não foi possível definir o Código de Natureza de COFINS para a operação')

    # COFINS - Compras
    @Rule(Fact(tpMvto='compra'), Fact(codNCM=MATCH.ncm), salience=9)
    def cofins_compra_cst(self, ncm):
        is_valid = True
        if ncm in ('1', '2'):
            self.r_cofins_cst = "50"  #Operação com direito a crédito
        elif ncm in ('4'):
            self.r_cofins_cst = "70"  #Operação de aquisição sem direito a crédito
        elif ncm in ('5'):
            self.r_cofins_cst = "72"  #Operação de aquisição com isenção
        elif ncm in ('6'):
            self.r_cofins_cst = "73"  #Operação de aquisição com alíquota zero
        elif ncm in ('6'):
            self.r_cofins_cst = "75"  #Operação de aquisição por substituição tributária
        else:
            is_valid = False

        if is_valid:
            self.declare(Fact(cofins_venda_cst=self.r_cofins_cst))
        else:
            print('Não foi possível definir o CST de COFINS para a operação')

    # COFINS - Transferências
    @Rule(Fact(tpMvto='transferencia'), salience=9)
    def cofins_transferencia_cst(self, ncm):
        self.r_cofins_cst = "70"