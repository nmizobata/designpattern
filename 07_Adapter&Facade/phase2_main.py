import phase2_facade as fc
import phase2_device as dv

homeTeater = fc.HomeTheaterFacade(dv.amp(), 
                                  dv.player(), 
                                  dv.projector(),
                                  dv.screen(),
                                  dv.lights(), 
                                  dv.Popper())
homeTeater.watchMovie("レイダース／失われたアーク《聖櫃》")
homeTeater.endMovie()

