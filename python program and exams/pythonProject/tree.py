# In a forest, trees grow with unique patterns. Define a Tree class with
# growth() method generating tree patterns. Derive Pine and Oak classes
# inheriting Tree. Implement recursion to visualize the growth pattern of
# each tree. Instructions: Define a Tree class with a growth() method
# generating tree patterns. Derive Pine and Oak classes inheriting Tree,
# overriding the growth() method. Use recursion to visualize the growth
# pattern of both a Pine tree and an Oak tree.

import turtle


class Tree:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.screen = turtle.Screen()
        self.screen.bgcolor("white")

    def growth(self, branch_length):
        if branch_length > 5:
            self.t.forward(branch_length)
            self.t.right(20)
            self.growth(branch_length - 15)
            self.t.left(40)
            self.growth(branch_length - 15)
            self.t.right(20)
            self.t.backward(branch_length)


class Pine(Tree):
    def growth(self, branch_length):
        if branch_length > 5:
            self.t.forward(branch_length)
            self.t.right(30)
            self.growth(branch_length - 15)
            self.t.left(60)
            self.growth(branch_length - 15)
            self.t.right(30)
            self.t.backward(branch_length)


class Oak(Tree):
    def growth(self, branch_length):
        if branch_length > 5:
            self.t.forward(branch_length)
            self.t.right(25)
            self.growth(branch_length - 15)
            self.t.left(50)
            self.growth(branch_length - 15)
            self.t.right(25)
            self.t.backward(branch_length)


def main():
    pine = Pine()
    pine.t.left(90)
    pine.t.up()
    pine.t.backward(100)
    pine.t.down()
    pine.growth(100)

    pine.screen.clear()

    oak = Oak()
    oak.t.left(90)
    oak.t.up()
    oak.t.backward(100)
    oak.t.down()
    oak.growth(100)

    oak.screen.mainloop()


if __name__ == "__main__":
    main()

