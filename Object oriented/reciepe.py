class Recipe:

        def __init__(self,dish,items,time) -> None:
                self.dish=dish
                self.items=items
                self.time=time
                pass
        
        def contents(self):
                print("The", self.dish,"has",self.items ,"and takes",self.time,"min to prepare")



Pizza = Recipe("Reciepe",["Cheese","Bread","Tomato"],45)
Pastor = Recipe("Reciepe",["Penne","Tomato"],55)

Pizza.contents()
Pastor.contents()