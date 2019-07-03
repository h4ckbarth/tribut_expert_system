from pyknow import *
from tribut_base_fact import TributBaseFact

class IcmsFact(TributBaseFact):
    icms_cst = Field(str, mandatory=False)
    icms_aliquota = Field(int, mandatory=False)
