class Building:
    total = 0
    def increase_total(self):
        self.total = self.total + 1

h = Building()
def new_object():
    for i in range(1, 41):
        print(i)
        h.increase_total()

new_object()
print(h.total)