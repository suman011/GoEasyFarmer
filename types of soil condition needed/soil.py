

class soil:

    def __init__(self,soiltype, dm1,dm2,om1,om2,ph1,ph2,n1,n2):
        self.soiltype=soiltype
        self.dm1=dm1
        self.dm2=dm2
        self.om1=om1
        self.om2=om2
        self.ph1=ph1
        self.ph2=ph2
        self.n1=n1
        self.n2=n2

    def __repr__(self):
        return "soil('{}','{}','{}','{}','{}','{}','{}','{}','{}',)".format(
        self.soiltype,
        self.dm1,
        self.dm2,
        self.om1,
        self.om2,
        self.ph1,
        self.ph2,
        self.n1,
        self.n2)
