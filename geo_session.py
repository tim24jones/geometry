class geo_session:
    def __init__(self,ledger=[],canvas_sizemin=[-500,-500],canvas_sizemax=[500,500],dimension=2):#ordered pairs
        self.ledger=ledger
        self.canvas_maxpt=canvas_sizemax
        self.canvas_minpt=canvas_sizemin
        self.dimens=2
        self.canvas_xwidth=self.canvas_maxpt[0]-self.canvas_minpt[0]
        self.canvas_ywidth=self.canvas_maxpt[1]-self.canvas_minpt[1]
        #including just these two as they will be most likely called for visualization
        #could be generalized to more dimensions if important
    #shapes added to ledger like this:
    #def addtoledger(self,geo_object)
    #    ledger=ledger+(geo_object,)+tuple(geo_object.attributes)
    #
