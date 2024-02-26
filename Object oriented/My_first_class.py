class MYFirstClass:
    print("Who wrote this?")

    index="Author-Book"

    def hand_list(self,philosopher,book):
        print(self.index)
        print(philosopher, "wrote the book: " , book)
        pass


whodunnit = MYFirstClass()

whodunnit.hand_list("Thabang",["God is love","You are Loved by God"])