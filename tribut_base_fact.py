from pyknow import *
class TributBaseFact(Fact):
    ncm_code = Field(str, mandatory=False)
    regime_empresa = Field(str, mandatory=False)
    tp_mvto = Field(str, mandatory=False)
    car_trib = Field(str, mandatory=False)

    pass
