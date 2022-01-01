class cricketer:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def current_match(self,score):
        self.score = self.score + score

shewag = cricketer("shewag",1000)
gambheer = cricketer("gambheer",800)
pant = cricketer("pant",900)
shewag.current_match(120)
gambheer.current_match(80)
pant.current_match(150)
shewag.current_match(15)
gambheer.current_match(19)
pant.current_match(17)
print(shewag.__dict__)
print(gambheer.__dict__)
print(pant.__dict__)
