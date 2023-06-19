from tkinter import *
import math

root = Tk()
root.title("Calculator")
root.configure(background='#e9e9d8')
lbl = Label(root, text = "Scientific Calculator", font=('Helvetica', 20, 'bold'), height = 2,
            bg = '#e9e9d8', width = 20)
calc = Frame(root)
lbl.grid()
calc.grid()

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ''
        self.user_input = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def numberInput(self, num):
        self.result = False
        numInput1 = txtDisplay.get()
        numInput2 = str(num)
        if self.user_input:
            self.current = numInput2
            self.user_input = False
        else:
            if numInput2 == '.':
                if numInput2 in numInput1:
                    return
            self.current = numInput1 + numInput2
        self.display(self.current)

    def totalSum(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.mainFunction()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def mainFunction(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.user_input = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.mainFunction()
        elif not self.result:
            self.total = self.current
            self.user_input = True
        self.check_sum = True
        self.op = op
        self.result = False

    def clearScreen(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.user_input = True

    def clearAllEntry(self):
        self.clearScreen()
        self.total = 0

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def sqrt(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)
    def squared(self):
        self.result = False
        self.current = math.pow(float(txtDisplay.get()), 2)
        self.display(self.current)
    def inv(self):
        self.result = False
        self.current = math.pow(float(txtDisplay.get()), (-1))
        self.display(self.current)
    def pow10(self):
        self.result = False
        self.current = math.pow(10, float(txtDisplay.get()))
        self.display(self.current)
    def fact(self):
        self.result = False
        self.current = math.factorial(int(txtDisplay.get()))
        self.display(self.current)
    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)
added_value = Calc()

txtDisplay = Entry(calc, font=('Helvetica', 21, 'bold'),
                   bg='black', fg='white',
                justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=5)
txtDisplay.insert(0, "0")

numberpad = "789456123"
i = 0
btn = []
for j in range(4, 7):
    for k in range(1,4):
        btn.append(Button(calc, width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberInput(x)
        i += 1

btnClear = Button(calc, text='C', width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=added_value.clearScreen
                  ).grid(row=1, column=3, pady=1)

btnAllClear = Button(calc, text='CE',
                     width=5,
                     height=2, bg='#e9e9d8',
                     font=('Calibri', 15),
                     bd=0.5,
                     command=added_value.clearAllEntry
                     ).grid(row=1, column=4, pady=1)

btnsqrt = Button(calc, text="\u221A", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=added_value.sqrt
               ).grid(row=3, column=0, pady=1)

btnsq = Button(calc, text="x\u00b2", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=added_value.squared
               ).grid(row=2, column=0, pady=1)

btninv = Button(calc, text="1/x", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=added_value.inv
               ).grid(row=4, column=0, pady=1)

btnipow10 = Button(calc, text="10^x", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=added_value.pow10
               ).grid(row=5, column=0, pady=1)

btnfact = Button(calc, text="n!", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=added_value.fact
               ).grid(row=3, column=3, pady=1)

btnAdd = Button(calc, text="+", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=lambda: added_value.operation("add")
                ).grid(row=6, column=4, pady=1)

btnSub = Button(calc, text="-", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=lambda: added_value.operation("sub")
                ).grid(row=5, column=4, pady=1)

btnMul = Button(calc, text="x", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=lambda: added_value.operation("multi")
                ).grid(row=4, column=4, pady=1)

btnDiv = Button(calc, text="/", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=lambda: added_value.operation("divide")
                ).grid(row=3, column=4, pady=1)

btnZero = Button(calc, text="0", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=lambda: added_value.numberInput(0)
                 ).grid(row=7, column=2, pady=1)

btnDot = Button(calc, text=".", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=lambda: added_value.numberInput(".")
                ).grid(row=7, column=3, pady=1)
btnPM = Button(calc, text=chr(177), width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=added_value.mathPM
               ).grid(row=7, column=1, pady=1)

btnEquals = Button(calc, text="=", width=5,
                  height=2, bg='#1985f2', fg = 'White',
                  font=('Calibri', 15),
                  bd=0.5, command=added_value.totalSum
                   ).grid(row=7, column=4, pady=1)

btnPi = Button(calc, text="pi", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=added_value.pi
               ).grid(row=1, column=1, pady=1)

btnCos = Button(calc, text="Cos", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=added_value.cos
                ).grid(row=2, column=2, pady=1)

btntan = Button(calc, text="tan", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=added_value.tan
                ).grid(row=3, column=1, pady=1)

btnsin = Button(calc, text="sin", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=added_value.sin
                ).grid(row=2, column=1, pady=1)

btn2Pi = Button(calc, text="2pi", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=added_value.tau
                ).grid(row=1, column=0, pady=1)

btnlog = Button(calc, text="ln", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=added_value.log
                ).grid(row=7, column=0, pady=1)

btnExp = Button(calc, text="exp", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=added_value.exp
                ).grid(row=2, column=3, pady=1)

btnMod = Button(calc, text="Mod", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=lambda: added_value.operation("mod")
                ).grid(row=2, column=4, pady=1)

btnE = Button(calc, text="e", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=added_value.e
              ).grid(row=1, column=2, pady=1)

btnlog10 = Button(calc, text="log", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=added_value.log10
                  ).grid(row=6, column=0, pady=1)

btndeg = Button(calc, text="deg", width=5,
                  height=2, bg='#e9e9d8',
                  font=('Calibri', 15),
                  bd=0.5, command=added_value.degrees
                ).grid(row=3, column=2, pady=1)

root.mainloop()