# |Задание на выбор или дополнительное про классы (тема 10ого семинара)|
#
# Напишите класс Dragon (Дракон), экземпляр которого при инициализации принимaет аргументы:
# рост, огнеопасность, цвет.
#
class Dragon():
    def __init__ (self, height, danger, color):
        self.height = height
        self.danger = danger
        self.color = color



# Класс обеспечивает выполнение методов (dr — экземпляр класса)
# экземпляры можно сравнивать: сначала по росту. затем по огнеопасности, затем по цвету по алфавиту
#
    def __gt__(self, other):
        return self.height > other.height
    def __eg__(self, other):
        return self.danger == other.danger
    def __le__(self, other):
        return self.color <= other.color

# экземпляры класса можно складывать: dr2 =dr + dr1. при этом возвращается новый экземпляр со значениями атрибутов:
#
# цвет меньший по алфавиту;
# рост - среднее арифметическое из двух округлённое до целого вниз,
# огнеопасность - большее из двух;
#
    def __add__(self, other):
        new_color = self.color if self.color < other.color else other.color
        new_height = (self.height + other.height) // 2
        new_danger = self.danger if self.danger > other.danger else other.danger
        return Dragon(height = new_height, danger = new_danger, color = new_color)


# из экземпляра класса можно вычесть число: dr -= number, из роста вычитается целая честь от деления роста на число, к
# огнеопасности прибавляется остаток от деления огнеопасности на число;
#
    def __sub__(self, other):
        self.height = self.height - (self.height // other)
        self.danger = self.danger + (self.danger % other)
        return self

# Экземпляр можно вызвать с аргументом-строкой - возвращается строка-аргумент, повторенная количество раз, равное
# значению атрибута огнеопасность;
#
    def __call__(self, string):
        return string * self.danger
# change_color() - вызывается c аргументом - цветом, на который нужно поменять имеющийся цвет
#
    def change_color(self, other):
        if type(other)== str:
            self.color = other
        return self

    # str- возвращает строку:
# Dragon with height «рост», danger <огнеопасность> and color «цвет».
#
    def __str__(self):
        return f"Dragon with height {self.height}, danger {self.danger} and color {self.color}"

# repr- возвращaет строку:
# Dragon(‹рост>, <огнеопасность>, <цвет>)
#
    def __repr__(self):
        return f"Dragon: {self.height}, {self.danger}, {self.color}"


dr = Dragon(69, 5, "brown")
dr1 = Dragon(69, 5, "gray")
print (dr > dr1, dr != dr1, dr <= dr1)
print(dr, dr1, sep="\n")
print()

dr.change_color("white")
dr -= 23
dr1 -= 2
dr2 = dr+dr1
print(dr, dr1, dr2, sep="\n")

print(dr.__call__("Welcome "))
#
# Вывод
#
# False True True
# Dragon with height 69, danger 5 and color brown.
# Dragon with height 69, danger 5 and color gray.
#
# Dragon with height 66, danger 10 and color white.
# Dragon with height 35, danger 6 and color gray.
# Dragon with height 50, danger 10 and color brown.
# WelcomeWelcomeWelcomeWelcomeWelcome

