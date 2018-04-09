class PreciousStone:
    num_of_PS = 0
    PS_collection = []
    def __init__(self, name):
        self.name = name
        
        PreciousStone.num_of_PS += 1
        if PreciousStone.num__of_PS <= 5:
            PreciousStone.PS_collection.append(self)
        else:
            del PreciousStone.PS_collection[0]
            PreciousStone.PS_collection.append(self)
    
    def displayPS():
        for PreciousStone in PreciousStone.PS_collection:
            print(PreciousStone.name, end = " ")
        print()

PS1  = PreciousStone("Diamond")
PS2  = PreciousStone("Opal")
PS3  = PreciousStone("Painite")
PS4  = PreciousStone("Saphire")
PS5  = PreciousStone("Amethest")
PS5.displayPreciousStones()
PS6  = PreciousStone("Emerald")
