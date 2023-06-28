# import statements

import tkinter as tk
import csv
from matplotlib import pyplot as plt
from statistics import mean


global attribute_var
file_name = "./iris.csv";
# csv file reader


def read_csv_file(filename):
    file = open(filename, "r", newline="\n")
    reader = csv.reader(file)
    csv_list = list(reader)  # converts csv file to a list datatype
    return csv_list
    file.close()


# bar-chart function

def bar_plot(id_no):
    X = ["sepal length", "sepal width", "petal length", "petal width"]
    Y = []
    dataset = read_csv_file(file_name)  # to retrieve data from csv file

    for i in range(2, 6):
        Y.append(float(dataset[int(id_no)][i]))  # list of measurement of attributes

    # designing and displaying the barchart

    x_count = range(len(Y))
    plt.bar(x_count, Y, width=0.5, align="center", edgecolor='coral', color='pink', linewidth=2)
    plt.xticks(x_count, X)
    plt.ylim(0, 8)
    plt.xlabel("Attribute", fontweight='bold', fontsize='12')
    plt.ylabel("Length", fontweight='bold', fontsize='12')
    plt.title("Measurement of attributes for sample - " + str(id_no), fontweight='bold', fontsize='12')
    plt.show()


# scatter-chart function

def scatter_plot(attribute):
    # Associating attribute to its index position in the list

    attribute_index = 0

    if attribute == "sepal_length":
        attribute_index = 2
    elif attribute == "sepal_width":
        attribute_index = 3
    elif attribute == "petal_length":
        attribute_index = 4
    elif attribute == "petal_width":
        attribute_index = 5

    # Creating list for x and y axes values

    x = []
    y = []
    y_list = []
    average = 0
    dataset = read_csv_file(file_name)  # to retrieve data from csv file

    for i in range(1, len(dataset)):

        x.append(float(dataset[i][attribute_index]))  # list of measurement of chosen attribute for 150 flowers

        for a in range(2, 6):

            if a != attribute_index:
                y_list.append(float(dataset[i][a]))

        average = round(mean(y_list), 2)
        y_list = []
        y.append(average)  # average of measurement of other attributes for 150 flowers

    # Designing and displaying scatter plot

    plt.subplots(figsize=(12, 7))
    plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
    plt.title("Attribute comparison for " + attribute, fontweight='bold', fontsize='11')
    plt.xlabel("Attribute measurement", fontweight='bold', fontsize='10')
    plt.ylabel("Average of other attributes", fontweight='bold', fontsize='10')
    plt.ylim(0, 8)
    plt.xlim(0, 8)
    plt.scatter(x, y, c=y, cmap='Spectral')
    plt.plot([0, 8], [0, 8], c='black')
    plt.show()


# ----------------------------------------------------------------TKINTER CODE

window = tk.Tk()
window.title("Flower Attribute Analysis")
window.maxsize(800, 650)
window.config(bg="floral white")
window.geometry("800x650")

frame = tk.Frame(window)
frame.config(bg="floral white")  # frame for title and questions displayed to user
frame.pack()

mainframe = tk.Frame(window)  # frame for widgets related to user's response and display of graphs
mainframe.pack()
mainframe.config(bg="floral white")


def clear_frame(frame_name):  # to clear screen

    for child in frame_name.winfo_children():
        child.destroy()


def test_eligibility(value):  # to ensure that values entered by the user are valid

    id_list = []

    for i in range(1, 151):
        id_list.append(i)

    try:  # to check if the input is a string and tackle possible errors related to converting a string to integer

        value = int(value)

    except ValueError:

        message1 = tk.Label(mainframe, text="The value you have entered is not an integer, please try again!",
                            font=('Courier', 12))
        message1.pack()
        message1.config(fg="black")

    else:

        test_Var = tk.BooleanVar()  # to check if the number entered by the user is available in the dataset
        test_Var = int(value) in id_list

        if test_Var == True:

            Flower_id_var = tk.StringVar()
            Flower_id_var.set(str(value))

            true_message = tk.Label(mainframe, text="Choice of Flower ID is: " + Flower_id_var.get(),
                                    font=('Courier', 15), bg='pink', fg="black")
            true_message.pack(fill=tk.X)

            Barplot_button = tk.Button(mainframe, text="Display bar plot", font=('Courier', 15), height=2, width=9,
                                       command=lambda: bar_plot(int(value)))
            Barplot_button.pack(fill=tk.X)  # button to display the bar chart

        else:

            false_message = tk.Text(mainframe, height=4, width=70)
            text = """The value you have entered is not in the flower ID list.
            Integers valid are 1-150, please try again!"""

            false_message.insert(tk.END, text)
            false_message.config(font=('Courier', 12), state=tk.DISABLED, fg="black")
            false_message.pack()


def option1_display():  # function performed by option-1 radiobutton

    option1_label = tk.Label(mainframe, text="Please enter flower ID number: ", font=('Courier', 15), bg='pink', fg="black")
    option1_label.pack(fill=tk.X)

    user_input = tk.Entry(mainframe, bg="floral white", fg="black")
    user_input.pack(fill=tk.X)
    user_input.insert(0, 0)

    test_button = tk.Button(mainframe, text="Confirm flower ID", font=('Courier', 15),
                            command=lambda: test_eligibility(user_input.get()),
                            height=2, width=9)

    test_button.pack(fill=tk.X)  # button to test the validity of user input and display graph


def option2_display():
    option2_label = tk.Label(mainframe, text="Attribute options are: ", font=('Courier', 15), bg="thistle1", fg="black")
    option2_label.pack(fill=tk.X)

    global attribute_var  # variable to be referenced in different functions

    attribute_var = tk.StringVar()  # radiobuttons associated to a single variable
    attribute_var.set("sepal_length")

    # options of attributes presented to the user

    rb_sl = tk.Radiobutton(mainframe, text="sepal length", variable=attribute_var, value="sepal_length",
                           font=('Courier', 15), fg="black", bg="floral white")
    rb_sw = tk.Radiobutton(mainframe, text="sepal width", variable=attribute_var, value="sepal_width",
                           font=('Courier', 15), fg="black", bg="floral white")
    rb_pl = tk.Radiobutton(mainframe, text="petal length", variable=attribute_var, value="petal_length",
                           font=('Courier', 15), fg="black", bg="floral white")
    rb_pw = tk.Radiobutton(mainframe, text="petal width", variable=attribute_var, value="petal_width",
                           font=('Courier', 15), fg="black", bg="floral white")

    rb_sl.pack(fill=tk.X)
    rb_sw.pack(fill=tk.X)
    rb_pl.pack(fill=tk.X)
    rb_pw.pack(fill=tk.X)


def view_scatterplot():  # function performed by option-2 radiobutton

    option2_display()

    global attribute_var

    scatter_graph = tk.Button(mainframe, text="Display Scatter Plot", font=('Courier', 16), command=

    lambda: scatter_plot(attribute_var.get()), height=3, width=13)

    scatter_graph.pack(fill=tk.X)  # button to display the scatter plot


def option3_display():  # function performed by option-3 radiobutton

    option3_label = tk.Label(mainframe, text="Thank you for viewing the flower attribute analysis!",
                             font=('Courier', 15), bg='powder blue', fg="black")
    option3_label.pack()

    exit_button = tk.Button(mainframe, text="EXIT", font=('Courier', 16), height=2, width=9, command=window.destroy,
                            bg="floral white")
    exit_button.pack()  # button to close window and end the program


def user_display():  # title and queries presented to the user

    title = tk.Label(frame, text="Flower Attribute Analysis", font=('Courier', 20, "bold"), bg='floral white')
    title.pack(fill=tk.X)
    title.config(fg="black")

    query = tk.Text(frame, height=5, width=70, bg='floral white')
    text = """   Please choose one of:
              1 - display flower's measurements
              2 - display scatter plot of attribute's measurements
              3 - exit the system """

    query.insert(tk.END, text)
    query.config(font=('Courier', 16), fg='black', state=tk.DISABLED)
    query.pack()

    query1 = tk.Label(frame, text="Your choice?", font=('Courier', 16), bg='floral white', fg="black")
    query1.pack()

    global user_choice
    user_choice = tk.StringVar()

    # options for the user to choose preferred type of graph or exit the program

    option1 = tk.Radiobutton(frame, text='1', font=('Courier', 18), variable=user_choice,
                             command=lambda: option1_display(),

                             value="option_1", bg='pink1', height=3, width=9, fg="black")  # to display barchart

    option2 = tk.Radiobutton(frame, text='2', font=('Courier', 18), variable=user_choice,
                             command=lambda: view_scatterplot(),

                             value="option_2", bg='Thistle', height=3, width=9, fg="black")  # to display scatterplot

    option3 = tk.Radiobutton(frame, text='3', font=('Courier', 18), variable=user_choice,
                             command=lambda: option3_display(),

                             value="option_3", bg='pale turquoise', height=3, width=9, fg="black")  # to exit

    option1.pack()
    option2.pack()
    option3.pack()

    # button to clear screen to restart the program

    clear_button = tk.Button(frame, text="CLEAR", font=('Courier', 16), height=2, width=9,
                             command=lambda: clear_frame(mainframe))
    clear_button.pack()


# ------------------------

user_display()

window.mainloop()
