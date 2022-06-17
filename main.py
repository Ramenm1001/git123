import turtle as t
t.color("red")
for i in range(12):
    t.forward(100)
    t.right(30)

t.color("salmon")
for i in range(99):
    t.forward(i)
    t.left(89)

t.mainloop()