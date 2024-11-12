"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

from tkinter import messagebox, simpledialog, Tk

window = Tk()
window.withdraw()

number1 = simpledialog.askinteger("First Number", "Pick a number:")
number2 = simpledialog.askinteger("Second Number", "Pick another number:")
sum = number1 + number2
difference = number1 - number2
product = number1 * number2
quotient = number1 / number2
mathoperation= simpledialog.askstring("Math operation", "Choose a math operation to use:")

if mathoperation == "Addition":
   messagebox.showinfo('Addition', str(number1) + ' + ' + str(number2) + ' = ' + str(sum) )
elif mathoperation == "Subtraction":
   messagebox.showinfo('Subtraction', str(number1) + ' - ' + str(number2) + ' = ' + str(difference) )
elif mathoperation == "Multiplication":
   messagebox.showinfo('Multiplication', str(number1) + ' x ' + str(number2) + ' = ' + str(product) )
elif mathoperation == "Division":
   messagebox.showinfo('Division', str(number1) + ' / ' + str(number2) + ' = ' + str(quotient) )
elif mathoperation == "Unknown":
   messagebox.showerror('Unknown Operation')

# Import the required modules

# Create a window object

# Hide the window, hint: use the withdraw method

# Ask the user for the first number   

# Ask the user for the second number

# Ask the user for the math operation

# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.

# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()

# Keep the window open
