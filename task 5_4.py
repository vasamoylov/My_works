class Building:
    total = 0
    def new_object(self):
        for i in range(1, 41):
            self.total += 1
            print(i)

h = Building()
h.new_object()
print(h.total)