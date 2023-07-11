class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        
        self.ph=philosopher
        self.b=book
        print(self.ph + " wrote the book: " + self.b)

whodunnit = MyFirstClass()
print(MyFirstClass.index)
whodunnit.hand_list("Sun Tzu", "The Art of War")