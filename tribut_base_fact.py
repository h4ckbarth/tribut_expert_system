from pyknow import *
class TributBaseFact(Fact):
    ncm_code = Field(str, mandatory=False)
    regime_empresa = Field(str, mandatory=False)
    tp_mvto = Field(str, mandatory=False)
    car_trib = Field(str, mandatory=False)
    origem = Field(str, mandatory=False)

    icms_cst = Field(str, mandatory=False)
    icms_aliquota = Field(float, mandatory=False)
    icms_reducao = Field(float, mandatory=False)
    icms_pauta = Field(float, mandatory=False)
    icms_mva = Field(float, mandatory=False)
    icms_st_aliquota = Field(float, mandatory=False)

    cofins_cst = Field(str, mandatory=False)
    cofins_aliquota = Field(float, mandatory=False)
    cofins_natureza = Field(str, mandatory=False)



    pass
