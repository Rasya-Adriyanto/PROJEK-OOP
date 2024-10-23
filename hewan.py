class hewan:
    def suara(self):
        raise NotImplementedError("subclass harus mengimplentasikan metode ini")
    
class kucing(hewan):
    def suara(self):
        return "meong:"
    
class sapi(hewan):
    def suara(self):
        return "maou:"

def cetak_suara(hewan):
    print(hewan.suara())
    
    hewan1 = kucing()
    hewan2 = sapi()
    
    cetak_suara(hewan1)
    cetak_suara(hewan2)
    
    