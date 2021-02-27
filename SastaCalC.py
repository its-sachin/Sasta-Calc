# @Created by Sachin


import tkinter as tk
from math import *
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
from PIL import ImageTk, Image
import os, shutil


# Defining the gui
main_app = tk.Tk()
main_app.geometry('800x495')
main_app.resizable(0,0)
main_app.title('Sasta CalC')
main_app.wm_iconbitmap(bitmap = 'icon.ico')



# ------------------------------Menu-------------------------
mainmenu = tk.Menu(main_app)

about_icon = tk.PhotoImage(file = 'icons/icon3.png')
the_creator_icon = tk.PhotoImage(file = 'icons/the_creator.png')

help = tk.Menu(mainmenu, tearoff = 0)

# color menu

light_default_icon = tk.PhotoImage(file = 'icons/light_default.png')
light_plus_icon = tk.PhotoImage(file = 'icons/light_plus.png')
dark_icon = tk.PhotoImage(file = 'icons/dark.png')
monokai_icon = tk.PhotoImage(file = 'icons/monokai.png')
night_blue_icon = tk.PhotoImage(file = 'icons/night_blue.png')
pink_icon = tk.PhotoImage(file = 'icons/red.png')


color_theme = tk.Menu(mainmenu, tearoff = 0)

theme_choice = tk.StringVar()

color_icons = (light_default_icon, light_plus_icon, dark_icon, monokai_icon, night_blue_icon, pink_icon)

color_dict = {
    'Light Default' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Monokai' : ('#474747','#d3b774'),
    'Night Blue' : ('#ededed', '#6b9dc2'),
    'Pink' : ('#2d2d2d', '#ffe8e8')
}





mainmenu.add_cascade(label = 'Color Theme',menu = color_theme)
mainmenu.add_cascade(label = 'Help',menu = help)

# -------------------------------Menu Over----------------------




# -----------------tabs--------------------


nb = ttk.Notebook(main_app)
standard = tk.Frame(nb)

nb.add(standard, text = 'Standard')

nb.pack(expand = True, fill = 'both')

creation_text = f"~Sachin's Creations"

creation = ttk.Label(nb, text = creation_text,foreground = '#9E9696')
creation.grid(row = 0, column = 20,padx = 500)








#------------------- tabs over---------------

#------------------------- The heart----------------------------

worker = tk.LabelFrame(standard,text = 'Standard Calculator')
worker.pack(fil = tk.BOTH,padx = 220,pady = 85)


def correct(inp):
    if inp.isnumeric():
        return True
    elif inp =='':
        return True
    else:
        return False


reg = main_app.register(correct)


value = tk.StringVar()
enter = ttk.Entry(worker,text = value,textvariable = value,width = 55, justify = 'right',validate = 'key',validatecommand = (reg,'%P'))
enter.grid(row = 0,rowspan = 2,padx = 5,pady = 5, column = 0, columnspan = 4, sticky = tk.NW)
value.set('')
enter.focus_set()


output = tk.StringVar()
ans = ttk.Entry(worker,text = output,textvariable = output, width = 55, state = 'readonly', justify = 'right')
ans.grid(row = 2,rowspan = 2 ,column = 0,padx = 5,pady = 5, columnspan = 4, sticky = tk.NW)
output.set('')

label = ttk.Label(worker, text = '=')
label.grid(row= 2,column = 0,pady = 6,padx = 10,sticky = tk.W)



# Functionality of buttons
def ce():
    output.set('')

def clear():
    global value
    value.set('')
    output.set('')

def back():
    global value
    val = value.get()
    value.set(val[0:-1])
    output.set('')


num_dict = {
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
    'zero' : '0',
    'hundred' : '00'

}

def equal():
    value.set(output.get())
    output.set('')


for i in num_dict:
    def num_fun(i):
        def f():
            global value
            val = value.get()
            try:
                if val == '0':
                    value.set(f'{num_dict[i]}')    
                else:
                    value.set(f'{value.get()}{num_dict[i]}')
                    try:
                        int(f'{val}8')
                    except:
                        output.set(eval(value.get()))
            except:
                value.set('ERROR')
        return f

fun_dict = {
    'add' : '+' ,
    'subt' : '-' , 
    'mult' : '*' , 
    'divide' : '/' 
    
}

for i in fun_dict:
    def oper_fun(i):
        def f():
            global value
            val = value.get()
            try:
                try:
                    int(val[-1])
                    value.set(f'{value.get()}{fun_dict[i]}')
                except:
                    if val == '' and fun_dict[i] == '-':
                        value.set('-')
                    else:
                        val[-1] = fun_dict[i]
                        value.set(val)
            except:
                value.set('ERROR')
        return f

def zero():
    global value
    try:
        if value.get() == '0':
            pass
        else:
            value.set(f'{value.get()}0')
            try:
                int(f'{val}8')
            except:
                output.set(eval(value.get()))
    except:
                value.set('ERROR')

def hundred():
    global value
    try:
        if value.get() == '0':
            pass
        elif value.get() == '':
            value.set(f'{value.get()}0')
        else:
            value.set(f'{value.get()}00')
            try:
                int(f'{val}8')
            except:
                output.set(eval(value.get()))
    except:
                value.set('ERROR')

def dec():
    global value
    val= value.get()
    try:
        try:
            int(val[-1])
            value.set(f'{val}.')
        except:
            pass
            
    except:
        value.set('ERROR')



clear_button = ttk.Button(worker, text = 'Clear', command = clear)
clear_button.grid(row=4,padx = 5,pady = 5,column=0)

ce_button = ttk.Button(worker, text = 'CE', command = ce)
ce_button.grid(row=4,padx = 5,pady = 5,column=1)

back_button = ttk.Button(worker, text = 'Back Space', command = back)
back_button.grid(row=4,padx = 5,pady = 5,column=2)

divide_button = ttk.Button(worker, text = '/', command = oper_fun('divide'))
divide_button.grid(row=4,padx = 5,pady = 5,column=3)



seven_button = ttk.Button(worker, text = '7', command = num_fun('seven'))
seven_button.grid(row=5,padx = 5,pady = 5,column=0)

eight_button = ttk.Button(worker, text = '8', command = num_fun('eight'))
eight_button.grid(row=5,padx = 5,pady = 5,column=1)

nine_button = ttk.Button(worker, text = '9', command = num_fun('nine'))
nine_button.grid(row=5,padx = 5,pady = 5,column=2)

mult_button = ttk.Button(worker, text = '*', command = oper_fun('mult'))
mult_button.grid(row=5,padx = 5,pady = 5,column=3)



four_button = ttk.Button(worker, text = '4', command = num_fun('four'))
four_button.grid(row=6,padx = 5,pady = 5,column=0)

five_button = ttk.Button(worker, text = '5', command = num_fun('five'))
five_button.grid(row=6,padx = 5,pady = 5,column=1)

six_button = ttk.Button(worker, text = '6', command = num_fun('six'))
six_button.grid(row=6,padx = 5,pady = 5,column=2)

sub_button = ttk.Button(worker, text = '-', command = oper_fun('subt'))
sub_button.grid(row=6,padx = 5,pady = 5,column=3)



one_button = ttk.Button(worker, text = '1', command = num_fun('one'))
one_button.grid(row=7,padx = 5,pady = 5,column=0)

two_button = ttk.Button(worker, text = '2', command = num_fun('two'))
two_button.grid(row=7,padx = 5,pady = 5,column=1)

three_button = ttk.Button(worker, text = '3', command = num_fun('three'))
three_button.grid(row=7,padx = 5,pady = 5,column=2)

add_button = ttk.Button(worker, text = '+', command = oper_fun('add'))
add_button.grid(row=7,padx = 5,pady = 5,column=3)



hund_button = ttk.Button(worker, text = '00', command = hundred)
hund_button.grid(row=8,padx = 5,pady = 5,column=0)

tens_button = ttk.Button(worker, text = '0', command = zero)
tens_button.grid(row=8,padx = 5,pady = 5,column=1)

dec_button = ttk.Button(worker, text = '.', command = dec)
dec_button.grid(row=8,padx = 5,pady = 5,column=2)

equal_button = ttk.Button(worker, text = '=', command = equal)
equal_button.grid(row=8,padx = 5,pady = 5,column=3)



# square fitting mode
square_fit = tk.Frame(nb)
nb.add(square_fit, text = 'Square Fitting')

worker1 = tk.LabelFrame(square_fit,text = 'X Readings')
worker1.pack(fil = tk.BOTH,side = tk.LEFT,expand = True,pady = 50,padx = 20)

worker2 = tk.LabelFrame(square_fit,text = 'Y Readings')
worker2.pack(fil = tk.BOTH,side = tk.RIGHT,expand = True,pady = 50,padx = 20)


text_editor1 = tk.Text(worker1)
text_editor1.config(wrap = 'word', relief = tk.FLAT)

scroll_bar1 = tk.Scrollbar(text_editor1)
text_editor1.focus_set()
scroll_bar1.pack(side = tk.RIGHT,fill = tk.Y)
text_editor1.pack(fill = tk.BOTH, expand = True)
scroll_bar1.config(command = text_editor1.yview)
text_editor1.config(yscrollcommand=scroll_bar1.set)

text_editor2 = tk.Text(worker2)
text_editor2.config(wrap = 'word', relief = tk.FLAT)

scroll_bar2 = tk.Scrollbar(text_editor2)
scroll_bar2.pack(side = tk.RIGHT,fill = tk.Y)
text_editor2.pack(fill = tk.BOTH, expand = True)
scroll_bar2.config(command = text_editor2.yview)
text_editor2.config(yscrollcommand=scroll_bar2.set)



def action():

    x_read = text_editor1.get(1.0 , tk.END)
    y_read = text_editor2.get(1.0 , tk.END)

    l1 = x_read.splitlines()
    m1 = y_read.splitlines()

    try:

        # l = [float(i) for i in l1]
        # m = [float(i) for i in m1]
        l = []
        m = []
        for i in l1:
            if i != '':
                l.append(float(i))
        for j in m1:
            if j != '':
                m.append(float(j))

        if len(l) == len(m):
            n = len(l)
            a = 0
            for i in l:
                a += i
            b = 0
            for i in l:
                b += i*i
            c = 0
            for i in m:
                c += i
            d = 0
            for i in range (len(l)):
                d += l[i]*m[i]

            sqr_out = tk.Toplevel()
            sqr_out.title('Square fitting')
            sqr_out.geometry('450x250')
            sqr_out.resizable(0,0)


            

            label_frame = tk.LabelFrame(sqr_out, text = 'Square Fitting Slope Finder')
            label_frame.pack(side = tk.LEFT,fill = tk.BOTH,padx = 50,pady = 50)


            a_label = tk.Label(label_frame, text= f"Value of submission x is :              {a}")
            a_label.grid(row= 0, column= 0, sticky = tk.NW, padx = 40, pady = 0) 

            c_label = ttk.Label(label_frame, text= f"Value of submission y is :              {c}")
            c_label.grid(row= 1, column= 0, sticky = tk.NW, padx = 40, pady = 0)

            d_label = ttk.Label(label_frame, text= f"Value of submission xy is :            {d}")
            d_label.grid(row= 2, column= 0, sticky = tk.NW, padx = 40, pady = 0)

            b_label = ttk.Label(label_frame, text= f"Value of submission x^2 is :         {b}")
            b_label.grid(row= 3, column= 0, sticky = tk.NW, padx = 40, pady = 0)

            n_label = ttk.Label(label_frame, text= f"No. of entries are :                              {n}")
            n_label.grid(row= 4, column= 0, sticky = tk.NW, padx = 40, pady = 0)

            slope_label = ttk.Label(label_frame)
            slope_label.grid(row= 5, column= 0, sticky = tk.NW, padx = 40, pady = 0)

            try:
                slope_label.config(text = f"Square fitting slope is :           {(a*c - d*n)/(a*a - n*b)}")
            except ZeroDivisionError:
                slope_label.config(text = 'Zero Division ERROR')
        

            choosen_theme = theme_choice.get()
            try:
                items = [label_frame,a_label,c_label,d_label,b_label,n_label,slope_label]

                choosen_theme = theme_choice.get()
                color_tuple = color_dict.get(choosen_theme)
                fg_color,bg_color = color_tuple[0],color_tuple[1]

                for i in items:
                    i.config(background = bg_color,foreground = fg_color)

                sqr_out.config(bg = bg_color)
            except:
                pass
            sqr_out.mainloop()
        else:
            mbox = messagebox.showerror('Warning', 'Both x and y have same number of Readings')
        
    except ValueError:
        mbox = messagebox.showerror('Warning', 'Input not valid')
    except TypeError:
        mbox = messagebox.showerror('Warning', 'Input not valid')
    except IndexError:
        mbox = messagebox.showerror('Warning', 'Both x and y have same number of Readings')
    except:
        pass









submit_button = ttk.Button(square_fit, text = 'Get Output', command = action,width = 20)
submit_button.pack(side = tk.BOTTOM,fill = tk.BOTH)

# status_bar = ttk.Label(main_app, text = 'Status Bar')
# status_bar.pack(side = tk.BOTTOM, fill = tk.X)

# creation2 = ttk.Label(status_bar, text = creation_text )
# creation2.pack(side = tk.RIGHT)


# Physics mode
physics = tk.Frame(nb)
nb.add(physics, text = 'Physics Mode')

worker1a = tk.LabelFrame(physics,text = 'Input')
worker1a.pack(fil = tk.BOTH,side = tk.LEFT,expand = True,pady = 15,padx = 20)

worker2a = tk.LabelFrame(physics,text = 'Output')
worker2a.pack(fil = tk.BOTH,side = tk.RIGHT,expand = True,pady = 15,padx = 20)


text_editor1a= tk.Text(worker1a)
text_editor1a.config(wrap = 'word', relief = tk.FLAT)

scroll_bar1a = tk.Scrollbar(text_editor1a)
text_editor1a.focus_set()
scroll_bar1a.pack(side = tk.RIGHT,fill = tk.Y)
text_editor1a.pack(fill = tk.BOTH, expand = True)
scroll_bar1a.config(command = text_editor1a.yview)
text_editor1a.config(yscrollcommand=scroll_bar1a.set)

text_editor2a = tk.Text(worker2a)
text_editor2a.config(wrap = 'word', relief = tk.FLAT)

scroll_bar2a = tk.Scrollbar(text_editor2a)
scroll_bar2a.pack(side = tk.RIGHT,fill = tk.Y)
text_editor2a.pack(fill = tk.BOTH, expand = True)
scroll_bar2a.config(command = text_editor2a.yview)
text_editor2a.config(yscrollcommand=scroll_bar2a.set)

def average():
    x_read = text_editor1a.get(1.0 , tk.END)

    l1 = x_read.splitlines()

    try:

        # l = [float(i) for i in l1]
        l = []
        for i in l1:
            if i != '':
                l.append(float(i))

        sum = 0
        for i in l:
            sum = sum + i 
        
        avg_val.set(sum/len(l))
    except:
        mbox = messagebox.showerror('Warning', 'Input not valid')


def rms():
    x_read = text_editor1a.get(1.0 , tk.END)

    l1 = x_read.splitlines()

    try:

        l = []
        for i in l1:
            if i != '':
                l.append(float(i))

        sum = 0
        for i in l:
            sum = sum + i*i 
        
        sqr = sum/len(l)
        rms_val.set(sqrt(sqr))
    except:
        mbox = messagebox.showerror('Warning', 'Input not valid')

def peak():
    x_read = text_editor1a.get(1.0 , tk.END)

    l1 = x_read.splitlines()

    try:

        l = []
        for i in l1:
            if i != '':
                l.append(float(i))

        
        peak_val.set(max(l))
    except:
        mbox = messagebox.showerror('Warning', 'Input not valid')

def pow():
    if pow_val.get() == '':
        messagebox.showinfo('Give the Power','Please write the value of n(corresponding power) in box besides power button')
    else:
        x_read = text_editor1a.get(1.0 , tk.END)

        l1 = x_read.splitlines()


        try:

            l = []
            for i in l1:
                if i != '':
                    l.append(float(i))

            text_editor2a.delete(1.0,tk.END)
            for i in l:
                text_editor2a.insert(tk.END,f'{i**float(pow_val.get())} \n')
        except:
            mbox = messagebox.showerror('Warning', 'Input not valid')

def is_prime():
    try:
        x_read = text_editor1a.get(1.0 , tk.END)
        l1 = x_read.splitlines()

        l = []
        for i in l1:
            if i != '':
                l.append(float(i))

        text_editor2a.delete(1.0,tk.END)
        for i in l:
            k = i//2
            while k > 1:
                if i%k == 0: 
                    text_editor2a.insert(tk.END,f'{i} is not a Prime \n')
                    k = -1
                else:
                    k = k-1
            if k == 1:
                text_editor2a.insert(tk.END,f'{i} is a Prime \n')
            
    except:
        mbox = messagebox.showerror('Warning', 'Input not valid')

def is_perfect():
    try:
        x_read = text_editor1a.get(1.0 , tk.END)
        l1 = x_read.splitlines()

        l = []
        for i in l1:
            if i != '':
                l.append(float(i))

        text_editor2a.delete(1.0,tk.END)
        for i in l:
            a = 0
            k = i//2
            while k > 0:
                if i%k == 0: 
                    a += k
                k = k-1
            if a == i:
                text_editor2a.insert(tk.END,f'{i} is a Perfect number \n')
            else:
                text_editor2a.insert(tk.END,f'{i} is not a Perfect number \n')
            
    except:
        mbox = messagebox.showerror('Warning', 'Input not valid')

def pow():
    if pow_val.get() == '':
        messagebox.showinfo('Give the Power','Please write the value of n(corresponding power) in box besides power button')
    else:
        x_read = text_editor1a.get(1.0 , tk.END)

        l1 = x_read.splitlines()


        try:

            l = []
            for i in l1:
                if i != '':
                    l.append(float(i))

            text_editor2a.delete(1.0,tk.END)
            for i in l:
                text_editor2a.insert(tk.END,f'{i**float(pow_val.get())} \n')
        except:
            mbox = messagebox.showerror('Warning', 'Input not valid')

def sorti():
    try:
        x_read = text_editor1a.get(1.0 , tk.END)
        l1 = x_read.splitlines()

        l = []
        for i in l1:
            if i != '':
                l.append(float(i))
        l.sort()

        text_editor2a.delete(1.0,tk.END)
        for i in l:
            if int(i) == i:
                text_editor2a.insert(tk.END,f'{int(i)} \n')
            else:
                text_editor2a.insert(tk.END,f'{i} \n')
    except:
        mbox = messagebox.showerror('Warning', 'Input not valid')

def sortd():
    try:
        x_read = text_editor1a.get(1.0 , tk.END)
        l1 = x_read.splitlines()

        l = []
        for i in l1:
            if i != '':
                l.append(float(i))
        l.sort()

        text_editor2a.delete(1.0,tk.END)
        for i in l:
            if int(i) == i:
                text_editor2a.insert(1.0,f'{int(i)} \n')
            else:
                text_editor2a.insert(1.0,f'{i} \n')
    except:
        mbox = messagebox.showerror('Warning', 'Input not valid')

def sequence():
    try:
        x_read = text_editor1a.get(1.0 , tk.END)
        l1 = x_read.splitlines()

        l = []
        for i in l1:
            if i != '':
                l.append(float(i))
        def largest_subseq(l):
            out = [[l[0]]]
            i = 1
            while i < len(l): 
                j = len(out)-1
                while j >= 0:
                    # print(out,j)

                    if l[i] > out[j][-1]:
                        # print(1)
                        out[j].append(l[i])
                        if j < len(out) - 1:
                            if len(out[j+1]) == len(out[j]):
                                out.pop(j+1)
                        j = -1


                    elif max(l[i:len(l)]) > out[j][-1]:
                        if len(out[j]) > 1 and l[i] > out[j][-2]:
                            # print(2)
                            out[j][-1] = l[i]
                            j = -1
                        elif len(out[j]) == 1:
                            # print(3)
                            out[0] = [l[i]]
                            j = -1
                        elif j == 0:
                            # print(4)
                            out = [[l[i]]] + out

                    j -= 1

                i += 1
            return out[-1]

        out = largest_subseq(l)
        text_editor2a.delete(1.0,tk.END)
        for i in out:
            if int(i) == i:
                text_editor2a.insert(tk.END,f'{int(i)} \n')
            else:
                text_editor2a.insert(tk.END,f'{i} \n')
    except:
        mbox = messagebox.showerror('Warning', 'Input not valid')

def partition():
    
    try:
        x_read = text_editor1a.get(1.0 , tk.END)
        l1 = x_read.splitlines()

        l = []
        for i in l1:
            if i != '':
                l.append(float(i))

        a= float(partition_val.get())

        h = 0
        k = len(l)-1
        while h < k:
            if l[h] > a and l[k] < a:
                b = l[h]
                l[h] = l[k]
                l[k] = b
                h += 1
                k -= 1
            elif l[h] < a and l[k] > a:
                h += 1
                k -= 1
            elif l[h] >= a and l[k] > a:
                k -= 1
            elif l[h] < a and l[k] <= a:
                h += 1
            elif l[h] == a and l[k] < a:
                b = l[h]
                l[h] = l[k]
                l[k] = b
                h += 1
            elif l[h] > a and l[k] == a:
                b = l[h]
                l[h] = l[k]
                l[k] = b
                k -= 1

            text_editor2a.delete(1.0,tk.END)
            for i in l:
                if int(i) == i:
                    text_editor2a.insert(tk.END,f'{int(i)} \n')
                else:
                    text_editor2a.insert(tk.END,f'{i} \n')

    except:
        mbox = messagebox.showerror('Warning', 'Input not valid')

def kth_smallset_fun():
    if kth_smallest_val.get() == '':
        messagebox.showinfo('Enter k','Please write the value of k in box besides kth smallest button')

    else:
        x_read = text_editor1a.get(1.0 , tk.END)

        l1 = x_read.splitlines()

        def partitioning(l,a):
            h = 0
            k = len(l)-1
            while h < k:
                if l[h] > a and l[k] < a:
                    b = l[h]
                    l[h] = l[k]
                    l[k] = b
                    h += 1
                    k -= 1
                elif l[h] < a and l[k] > a:
                    h += 1
                    k -= 1
                elif l[h] >= a and l[k] > a:
                    k -= 1
                elif l[h] < a and l[k] <= a:
                    h += 1
                elif l[h] == a and l[k] < a:
                    b = l[h]
                    l[h] = l[k]
                    l[k] = b
                    h += 1
                elif l[h] > a and l[k] == a:
                    b = l[h]
                    l[h] = l[k]
                    l[k] = b
                    k -= 1
            return l

        def kth_smallest(l,k):
            import random
            a = l[random.randint(0,len(l)-1)]
            l = partitioning(l,a)
            if l.index(a) == k-1:
                return a
            elif l.index(a) > k-1:
                return kth_smallest(l[0:l.index(a)],k)
            else:
                return kth_smallest(l[l.index(a):len(l)],k-l.index(a))

        try:

            l = []
            for i in l1:
                if i != '':
                    l.append(float(i))
            k = float(kth_smallest_val.get())

            if k > len(l) or k < 0:
                messagebox.showinfo('Enter valid k','Please write the value of k that is in the range')
            else:
                text_editor2a.delete(1.0,tk.END)
                text_editor2a.insert(1.0,kth_smallest(l,k))
        except:
            mbox = messagebox.showerror('Warning', 'Input not valid')

def random():
    if random_val.get() == '':
        messagebox.showinfo('Give the Operation','Please write the operation that you want to perform on the data in box besides power button')
    else:
        x_read = text_editor1a.get(1.0 , tk.END)

        l1 = x_read.splitlines()

        oper = random_val.get()

        try:

            l = []
            for i in l1:
                if i != '':
                    l.append(float(i))

            text_editor2a.delete(1.0,tk.END)
            for i in l:
                val = eval(f'{i}{oper}')
                text_editor2a.insert(tk.END,f'{val} \n')
        except:
            mbox = messagebox.showerror('Warning', 'Input not valid')

worker3a = tk.LabelFrame(physics,text = 'Operations')
worker3a.pack(fil = tk.Y,expand = True,pady = 15)





avg_button = ttk.Button(worker3a, text = 'Average', command = average,width = 12)
avg_button.grid(row = 0,column= 0,pady = 4)

avg_val = tk.StringVar()
avg_entry = ttk.Entry(worker3a, textvariable = avg_val,width = 8,state = 'readonly')
avg_entry.grid(row = 0,column= 1,pady = 4)

rms_button = ttk.Button(worker3a, text = 'RMS', command = rms,width = 12)
rms_button.grid(row = 1,column= 0,pady = 4)

rms_val = tk.StringVar()
rms_entry = ttk.Entry(worker3a, textvariable = rms_val,width = 8,state = 'readonly')
rms_entry.grid(row = 1,column= 1,pady = 4)

peak_button = ttk.Button(worker3a, text = 'Peak', command = peak,width = 12)
peak_button.grid(row = 2,column=0,pady = 4)

peak_val = tk.StringVar()
peak_entry = ttk.Entry(worker3a, textvariable = peak_val,width = 8,state = 'readonly')
peak_entry.grid(row = 2,column= 1,pady = 4)

pow_button = ttk.Button(worker3a, text = 'nth power', command = pow,width = 12)
pow_button.grid(row = 3,column=0,pady = 4)

pow_val = tk.StringVar()
pow_entry = ttk.Entry(worker3a, textvariable = pow_val,width = 8)
pow_entry.grid(row = 3,column= 1,pady = 4)

partition_button = ttk.Button(worker3a, text = 'Partion about: ', command = partition,width = 12)
partition_button.grid(row = 4,column = 0,pady = 4)

partition_val = tk.StringVar()
partition_entry = ttk.Entry(worker3a, textvariable = partition_val,width = 8)
partition_entry.grid(row = 4,column= 1,pady = 4)

kth_smallest_button = ttk.Button(worker3a, text = 'kth smallest', command = kth_smallset_fun,width = 12)
kth_smallest_button.grid(row = 5,column = 0,pady = 4)

kth_smallest_val = tk.StringVar()
kth_smallest_entry = ttk.Entry(worker3a, textvariable = kth_smallest_val,width = 8)
kth_smallest_entry.grid(row = 5,column= 1,pady = 4)

random_button = ttk.Button(worker3a, text = 'Random', command = random,width = 12)
random_button.grid(row = 6,column = 0,pady = 4)

random_val = tk.StringVar()
random_entry = ttk.Entry(worker3a, textvariable = random_val,width = 8)
random_entry.grid(row = 6,column= 1,pady = 4)

prime_button = ttk.Button(worker3a, text = 'Is Prime', command = is_prime,width = 23)
prime_button.grid(row = 7,columnspan = 2,pady = 4)

perfect_button = ttk.Button(worker3a, text = 'Is Perfect', command = is_perfect,width = 23)
perfect_button.grid(row = 8,columnspan = 2,pady = 4)

sorti_button = ttk.Button(worker3a, text = 'Sort in increasing order', command = sorti,width = 25)
sorti_button.grid(row =9,columnspan = 2,pady = 4)

sortd_button = ttk.Button(worker3a, text = 'Sort in decreasing order', command = sortd,width = 25)
sortd_button.grid(row = 10,columnspan = 2,pady = 4)

seq_button = ttk.Button(worker3a, text = 'Largest Increasing Sequence', command = sequence,width = 25)
seq_button.grid(row = 11,columnspan = 2,pady = 4)





# Scientific mode
scientific = tk.Frame(nb)

nb.add(scientific, text = 'Scientific')

worker1b = tk.LabelFrame(scientific,text = 'Scientific Calculator')
worker1b.pack(fil = tk.BOTH,padx = 50,pady = 70)

equa = ''
value1 = tk.StringVar()
enter1 = ttk.Entry(worker1b,textvariable = value1,width = 110, justify = 'right')
enter1.grid(row = 0,rowspan = 2,padx = 5,pady = 5, column = 0, columnspan = 8, sticky = tk.N)
value1.set('')
enter1.focus_set()

def btnPress(num):
    global equa
    equa = equa + str(num)
    value1.set(equa)
def EqualPress():
    global equa
    x=enter1.get()  
    if(equa==""):
               equa=equa+x              
    try:
        total = str(eval(equa))
        value1.set(total)
        if(float(total)==0):
            equa=""
        else:
            equa=total
    except:
        value1.set("ERROR")
        equa=""
        pass                                     
def ClearPress():
    global equa
    equa = ""
    value1.set("")
def back1():
    global equa
    value1.set(value1.get()[0:-1])
    equa = equa[0:-1]



clear_button = ttk.Button(worker1b, text = 'Clear', command = ClearPress)
clear_button.grid(row=4,padx = 5,pady = 5,column=0)

zero_button = ttk.Button(worker1b, text = '0', command = lambda:btnPress(0))
zero_button.grid(row=4,padx = 5,pady = 5,column=1)

back_button = ttk.Button(worker1b, text = 'Back Space', command = back1)
back_button.grid(row=4,padx = 5,pady = 5,column=2)

divide_button = ttk.Button(worker1b, text = '/', command = lambda:btnPress('/'))
divide_button.grid(row=4,padx = 5,pady = 5,column=3)



seven_button = ttk.Button(worker1b, text = '7', command = lambda:btnPress(7))
seven_button.grid(row=5,padx = 5,pady = 5,column=0)

eight_button = ttk.Button(worker1b, text = '8', command = lambda:btnPress(8))
eight_button.grid(row=5,padx = 5,pady = 5,column=1)

nine_button = ttk.Button(worker1b, text = '9', command = lambda:btnPress(9))
nine_button.grid(row=5,padx = 5,pady = 5,column=2)

mult_button = ttk.Button(worker1b, text = '*', command = lambda:btnPress('*'))
mult_button.grid(row=5,padx = 5,pady = 5,column=3)



four_button = ttk.Button(worker1b, text = '4', command = lambda:btnPress(4))
four_button.grid(row=6,padx = 5,pady = 5,column=0)

five_button = ttk.Button(worker1b, text = '5', command = lambda:btnPress(5))
five_button.grid(row=6,padx = 5,pady = 5,column=1)

six_button = ttk.Button(worker1b, text = '6', command = lambda:btnPress(6))
six_button.grid(row=6,padx = 5,pady = 5,column=2)

sub_button = ttk.Button(worker1b, text = '-', command = lambda:btnPress('-'))
sub_button.grid(row=6,padx = 5,pady = 5,column=3)



one_button = ttk.Button(worker1b, text = '1', command = lambda:btnPress(1))
one_button.grid(row=7,padx = 5,pady = 5,column=0)

two_button = ttk.Button(worker1b, text = '2', command = lambda:btnPress(2))
two_button.grid(row=7,padx = 5,pady = 5,column=1)

three_button = ttk.Button(worker1b, text = '3', command = lambda:btnPress(3))
three_button.grid(row=7,padx = 5,pady = 5,column=2)

add_button = ttk.Button(worker1b, text = '+', command = lambda:btnPress('+'))
add_button.grid(row=7,padx = 5,pady = 5,column=3)



lparren_button = ttk.Button(worker1b, text = '(', command = lambda:btnPress('('))
lparren_button.grid(row=8,padx = 5,pady = 5,column=0)

rparren_button = ttk.Button(worker1b, text = ')', command = lambda:btnPress(')'))
rparren_button.grid(row=8,padx = 5,pady = 5,column=1)

dec_button = ttk.Button(worker1b, text = '.', command = lambda:btnPress('.'))
dec_button.grid(row=8,padx = 5,pady = 5,column=2)

equal_button = ttk.Button(worker1b, text = '=', command = EqualPress)
equal_button.grid(row=8,padx = 5,pady = 5,column=3)


sin_button = ttk.Button(worker1b, text = 'sin', command = lambda:btnPress('sin('))
sin_button.grid(row=9,padx = 5,pady = 5,column=0)

cos_button = ttk.Button(worker1b, text = 'cos', command = lambda:btnPress('cos('))
cos_button.grid(row=9,padx = 5,pady = 5,column=1)

sinh_button = ttk.Button(worker1b, text = 'sinh', command = lambda:btnPress('sinh('))
sinh_button.grid(row=9,padx = 5,pady = 5,column=2)

cosh_button = ttk.Button(worker1b, text = 'cosh', command = lambda:btnPress('cosh('))
cosh_button.grid(row=9,padx = 5,pady = 5,column=3)


asin_button = ttk.Button(worker1b, text = 'asin', command = lambda:btnPress('asin('))
asin_button.grid(row=10,padx = 5,pady = 5,column=0)

acos_button = ttk.Button(worker1b, text = 'acos', command = lambda:btnPress('acos('))
acos_button.grid(row=10,padx = 5,pady = 5,column=1)

asinh_button = ttk.Button(worker1b, text = 'asinh', command = lambda:btnPress('asinh('))
asinh_button.grid(row=10,padx = 5,pady = 5,column=2)

acosh_button = ttk.Button(worker1b, text = 'acosh', command = lambda:btnPress('acosh('))
acosh_button.grid(row=10,padx = 5,pady = 5,column=3)


tan_button = ttk.Button(worker1b, text = 'tan', command = lambda:btnPress('tan('))
tan_button.grid(row=9,padx = 5,pady = 5,column=4)

tanh_button = ttk.Button(worker1b, text = 'tanh', command = lambda:btnPress('tanh('))
tanh_button.grid(row=9,padx = 5,pady = 5,column=5)

atan_button = ttk.Button(worker1b, text = 'atan', command = lambda:btnPress('atan('))
atan_button.grid(row=9,padx = 5,pady = 5,column=6)

atanh_button = ttk.Button(worker1b, text = 'atanh', command = lambda:btnPress('atanh('))
atanh_button.grid(row=9,padx = 5,pady = 5,column=7)


pi_button = ttk.Button(worker1b, text = 'pi', command = lambda:btnPress('pi'))
pi_button.grid(row=10,padx = 5,pady = 5,column=4)

deg_button = ttk.Button(worker1b, text = 'deg', command = lambda:btnPress('degrees('))
deg_button.grid(row=10,padx = 5,pady = 5,column=5)

radian_button = ttk.Button(worker1b, text = 'radian', command = lambda:btnPress('radians('))
radian_button.grid(row=10,padx = 5,pady = 5,column=6)

atan2_button = ttk.Button(worker1b, text = 'atan2', command = lambda:btnPress('atan2('))
atan2_button.grid(row=10,padx = 5,pady = 5,column=7)


gcd_button = ttk.Button(worker1b, text = 'gcd', command = lambda:btnPress('gcd('))
gcd_button.grid(row=8,padx = 5,pady = 5,column=4)

hypot_button = ttk.Button(worker1b, text = 'hypot', command =lambda:btnPress('hypot('))
hypot_button.grid(row=8,padx = 5,pady = 5,column=5)

modf_button = ttk.Button(worker1b, text = 'modf', command = lambda:btnPress('modf('))
modf_button.grid(row=8,padx = 5,pady = 5,column=6)

lgamma_button = ttk.Button(worker1b, text = 'lgamma', command = lambda:btnPress('lgamma('))
lgamma_button.grid(row=8,padx = 5,pady = 5,column=7)


abs_button = ttk.Button(worker1b, text = 'abs', command = lambda:btnPress('abs('))
abs_button.grid(row=7,padx = 5,pady = 5,column=4)

floor_button = ttk.Button(worker1b, text = 'floor', command = lambda:btnPress('floor('))
floor_button.grid(row=7,padx = 5,pady = 5,column=5)

ceil_button = ttk.Button(worker1b, text = 'ceil', command = lambda:btnPress('ceil'))
ceil_button.grid(row=7,padx = 5,pady = 5,column=6)

gamma_button = ttk.Button(worker1b, text = 'gamma', command = lambda:btnPress('gamma'))
gamma_button.grid(row=7,padx = 5,pady = 5,column=7)


div_button = ttk.Button(worker1b, text = 'div', command = lambda:btnPress('%'))
div_button.grid(row=6,padx = 5,pady = 5,column=4)

mod_button = ttk.Button(worker1b, text = 'mod', command = lambda:btnPress('//'))
mod_button.grid(row=6,padx = 5,pady = 5,column=5)

int_button = ttk.Button(worker1b, text = 'int', command = lambda:btnPress('int('))
int_button.grid(row=6,padx = 5,pady = 5,column=6)

float_button = ttk.Button(worker1b, text = 'float', command = lambda:btnPress('float('))
float_button.grid(row=6,padx = 5,pady = 5,column=7)


e_button = ttk.Button(worker1b, text = 'e', command = lambda:btnPress('e'))
e_button.grid(row=5,padx = 5,pady = 5,column=4)

log_button = ttk.Button(worker1b, text = 'log', command = lambda:btnPress('log('))
log_button.grid(row=5,padx = 5,pady = 5,column=5)

log10_button = ttk.Button(worker1b, text = 'log10', command = lambda:btnPress('log10('))
log10_button.grid(row=5,padx = 5,pady = 5,column=6)

exp_button = ttk.Button(worker1b, text = 'exp', command = lambda:btnPress('exp('))
exp_button.grid(row=5,padx = 5,pady = 5,column=7)


comma_button = ttk.Button(worker1b, text = ',', command = lambda:btnPress(','))
comma_button.grid(row=4,padx = 5,pady = 5,column=4)

sqrt_button = ttk.Button(worker1b, text = 'sqrt', command = lambda:btnPress('sqrt('))
sqrt_button.grid(row=4,padx = 5,pady = 5,column=5)

pow_button = ttk.Button(worker1b, text = 'pow', command = lambda:btnPress('pow('))
pow_button.grid(row=4,padx = 5,pady = 5,column=6)

fact_button = ttk.Button(worker1b, text = '!', command = lambda:btnPress('factorial('))
fact_button.grid(row=4,padx = 5,pady = 5,column=7)





# conversion mode

convertor = tk.Frame(nb)

nb.add(convertor, text = 'Convertor')

worker1c = tk.LabelFrame(convertor,text = 'Coversion mode')
worker1c.pack(fil = tk.BOTH,padx = 30,pady = 10)


workeri = tk.LabelFrame(worker1c,text = 'Length Conversion')
workeri.grid(row = 0 ,column = 0,padx = 10,pady = 10)


len_dict = {
    'Kilometer (km)' : 1000,
    'Hectameter (hm)' : 100,
    'Decameter (dam)' : 10,
    'Meter (m)' : 1,
    'Decimeter (dm)' : .1,
    'Centimeter (cm)' : .01,
    'Millimeter (mm)' : .001,
    'Micrometer (um)' : 10**-6,
    'Nanoeter (m)' : 10**-9,
    'Angstrom (A)' : 10**-10,
    'Picoeter (m)' : 10**-12,
    'yard (yd)' : 0.9144,
    'Foot (ft)' : 0.304,
    'Mile (mi)' : 1609.27,
    'Inch (in)' : 0.0254,
    'Fanthom (fm)' : 1.828
    # 'Lunar Distance (ld)' : 1,
    # 'Astronomical Unit (AU)' : 1,
    # 'Parsec (pc)' : 1,
    # "Light Year (ly)" : 1
}
len_list = []
for item in len_dict:
    len_list.append(item)


def len_fun():
    try:
        x =  len_dict[from_length_var.get()]
        y = len_dict[to_length_var.get()]

        a = from_len_val.get()

        ans = float(a)*x/y

        to_len_val.set(ans)
    except:
        messagebox.showinfo('Warning', 'Input valid data')

from_length_var = tk.StringVar()
from_length_combobox = ttk.Combobox(workeri, width=16, textvariable = from_length_var, state = 'readonly')
from_length_combobox.grid(row=0,column=0,padx = 5)
from_length_combobox['values'] = len_list
from_length_combobox.current(3)

from_len_val = tk.StringVar()
from_len_entry = ttk.Entry(workeri, textvariable = from_len_val,width = 15)
from_len_entry.grid(row = 2,column= 0,pady = 4,padx = 5)
from_len_entry.focus_set()

to_len_val = tk.StringVar()
to_len_entry = ttk.Entry(workeri, text = to_len_val,width = 15,state = 'readonly')
to_len_entry.grid(row = 2,column= 3,pady = 4,padx = 5)


to_length_var = tk.StringVar()
to_length_combobox = ttk.Combobox(workeri, width=16, textvariable = to_length_var, state = 'readonly')
to_length_combobox.grid(row=0,column=3,padx = 5)
to_length_combobox['values'] = len_list
to_length_combobox.current(3)

len_button = ttk.Button(workeri, text = 'Convert', command = len_fun)
len_button.grid(row=1,padx = 5,pady = 5,column=1)



workerii = tk.LabelFrame(worker1c,text = 'Area Conversion')
workerii.grid(row = 0,column = 1,padx = 10,pady = 10)


area_dict = {
    'Square Kilometer' : 10**6,
    'Hectare' : 10**4,
    'are' : 100,
    'Square Metre' : 1,
    'Square Decimeter' : 0.01,
    'Square Centimeter' : 10**-4,
    'Square Millimeter' : 10**-6,
    'Square yard' : 0.8361,
    'Square Foot' : 0.0929,
    'Square Mile' : 2590002.6,
    'Square Inch' : 0.000645,
    'acre' : 4046.94,
    'Square rod' : 25
}
area_list = []
for item in area_dict:
    area_list.append(item)


def area_fun():
    try:
        x =  area_dict[from_area_var.get()]
        y = area_dict[to_area_var.get()]

        a = from_area_val.get()

        ans = float(a)*x/y

        to_area_val.set(ans)
    except:
        messagebox.showinfo('Warning', 'Input valid data')

from_area_var = tk.StringVar()
from_area_combobox = ttk.Combobox(workerii, width=16, textvariable = from_area_var, state = 'readonly')
from_area_combobox.grid(row=0,column=0,padx = 5)
from_area_combobox['values'] = area_list
from_area_combobox.current(3)

from_area_val = tk.StringVar()
from_area_entry = ttk.Entry(workerii, textvariable = from_area_val,width = 15)
from_area_entry.grid(row = 2,column= 0,pady = 4,padx = 5)
from_area_entry.focus_set()

to_area_val = tk.StringVar()
to_area_entry = ttk.Entry(workerii, text = to_area_val,width = 15,state = 'readonly')
to_area_entry.grid(row = 2,column= 3,pady = 4,padx = 5)


to_area_var = tk.StringVar()
to_area_combobox = ttk.Combobox(workerii, width=16, textvariable = to_area_var, state = 'readonly')
to_area_combobox.grid(row=0,column=3,padx = 5)
to_area_combobox['values'] = area_list
to_area_combobox.current(3)

area_button = ttk.Button(workerii, text = 'Convert', command = area_fun)
area_button.grid(row=1,padx = 5,pady = 5,column=1)


workeriii = tk.LabelFrame(worker1c,text = 'Volume Conversion')
workeriii.grid(row = 1,column = 0,padx = 10,pady = 10)


volume_dict = {
    'Meter (m^3)' : 1,
    'Centimeter (cm^3)' : 10**-6,
    'Hectoliter (hl)' : .1,
    'Deciliter (dl)' : 10**-4,
    'Centiliter (cl)' : 10**-5,
    'Liter (l)' : 10**-3,
    'Decimeter (dm^3)' : 10**-3,
    'Milimeter (mm^3)' : 10**-9,
    'Mililiter (ml)' : 10**-6,
    'US ounce (oz)' : .00002927,
    'Feet (ft^3)' : 0.0283,
    'Yard (yd3)' : 0.764,
    'Inch (in^3)' : 0.00001638,
    'acre foot (af^3)' : 1233.501,
    'UK ounce (oz)' : 0.00002841,
    'US gallon' : 0.00378541,
    'UK gallon' : 0.00454609
}
volume_list = []
for item in volume_dict:
    volume_list.append(item)


def volume_fun():
    try:
        x =  volume_dict[from_volume_var.get()]
        y = volume_dict[to_volume_var.get()]

        a = from_volume_val.get()

        ans = float(a)*x/y

        to_volume_val.set(ans)
    except:
        messagebox.showinfo('Warning', 'Input valid data')

from_volume_var = tk.StringVar()
from_volume_combobox = ttk.Combobox(workeriii, width=16, textvariable = from_volume_var, state = 'readonly')
from_volume_combobox.grid(row=0,column=0,padx = 5)
from_volume_combobox['values'] = volume_list
from_volume_combobox.current(5)

from_volume_val = tk.StringVar()
from_volume_entry = ttk.Entry(workeriii, textvariable = from_volume_val,width = 15)
from_volume_entry.grid(row = 2,column= 0,pady = 4,padx = 5)
from_volume_entry.focus_set()

to_volume_val = tk.StringVar()
to_volume_entry = ttk.Entry(workeriii, text = to_volume_val,width = 15,state = 'readonly')
to_volume_entry.grid(row = 2,column= 3,pady = 4,padx = 5)


to_volume_var = tk.StringVar()
to_volume_combobox = ttk.Combobox(workeriii, width=16, textvariable = to_volume_var, state = 'readonly')
to_volume_combobox.grid(row=0,column=3,padx = 5)
to_volume_combobox['values'] = volume_list
to_volume_combobox.current(3)

volume_button = ttk.Button(workeriii, text = 'Convert', command = volume_fun)
volume_button.grid(row=1,padx = 5,pady = 5,column=1)


workeriv = tk.LabelFrame(worker1c,text = 'Weight Conversion')
workeriv.grid(row = 1,column = 1,padx = 10,pady = 10)


weight_dict = {
    'Ton (t)' : 10**6,
    'Quintol (q)' : 10**5,
    'Kilogram (kg)' : 1000,
    'Gram (g)' : 1,
    'Carat (ct)' : 0.2,
    'Microgram (ug)' : 10**-6,
    'Milligram (mg)' : 10**-3,
    'Short ton (st)' : 907194.0488,
    'Long ton (lt)' : 1016053.64763,
    'Ounce (oz)' : 28.34592,
    'Grain (gr)' : 0.06479891,
    'Dram (dr)' : 1.77184519,
    'Pound (lb)' : 453.5923
}
weight_list = []
for item in weight_dict:
    weight_list.append(item)


def weight_fun():
    try:
        x =  weight_dict[from_weight_var.get()]
        y = weight_dict[to_weight_var.get()]

        a = from_weight_val.get()

        ans = float(a)*x/y

        to_weight_val.set(ans)
    except:
        messagebox.showinfo('Warning', 'Input valid data')

from_weight_var = tk.StringVar()
from_weight_combobox = ttk.Combobox(workeriv, width=16, textvariable = from_weight_var, state = 'readonly')
from_weight_combobox.grid(row=0,column=0,padx = 5)
from_weight_combobox['values'] = weight_list
from_weight_combobox.current(3)

from_weight_val = tk.StringVar()
from_weight_entry = ttk.Entry(workeriv, textvariable = from_weight_val,width = 15)
from_weight_entry.grid(row = 2,column= 0,pady = 4,padx = 5)
from_weight_entry.focus_set()

to_weight_val = tk.StringVar()
to_weight_entry = ttk.Entry(workeriv, text = to_weight_val,width = 15,state = 'readonly')
to_weight_entry.grid(row = 2,column= 3,pady = 4,padx = 5)


to_weight_var = tk.StringVar()
to_weight_combobox = ttk.Combobox(workeriv, width=16, textvariable = to_weight_var, state = 'readonly')
to_weight_combobox.grid(row=0,column=3,padx = 5)
to_weight_combobox['values'] = weight_list
to_weight_combobox.current(3)

weight_button = ttk.Button(workeriv, text = 'Convert', command = weight_fun)
weight_button.grid(row=1,padx = 5,pady = 5,column=1)



workerv = tk.LabelFrame(worker1c,text = 'Speed Conversion')
workerv.grid(row = 2,column = 0,padx = 10,pady = 10)


speed_dict = {
    'mile/h' : 0.44704,
    'km/s' : 1000,
    'Mach Ma' : 340.2981,
    'm/s' : 1,
    'inch/s' : 0.0253999,
    'km/h' : 0.27777778,
    'Speed if light c' : 299796138.6257345
}
speed_list = []
for item in speed_dict:
    speed_list.append(item)


def speed_fun():
    try:
        x =  speed_dict[from_speed_var.get()]
        y = speed_dict[to_speed_var.get()]

        a = from_speed_val.get()

        ans = float(a)*x/y

        to_speed_val.set(ans)
    except:
        messagebox.showinfo('Warning', 'Input valid data')

from_speed_var = tk.StringVar()
from_speed_combobox = ttk.Combobox(workerv, width=16, textvariable = from_speed_var, state = 'readonly')
from_speed_combobox.grid(row=0,column=0,padx = 5)
from_speed_combobox['values'] = speed_list
from_speed_combobox.current(3)

from_speed_val = tk.StringVar()
from_speed_entry = ttk.Entry(workerv, textvariable = from_speed_val,width = 15)
from_speed_entry.grid(row = 2,column= 0,pady = 4,padx = 5)
from_speed_entry.focus_set()

to_speed_val = tk.StringVar()
to_speed_entry = ttk.Entry(workerv, text = to_speed_val,width = 15,state = 'readonly')
to_speed_entry.grid(row = 2,column= 3,pady = 4,padx = 5)


to_speed_var = tk.StringVar()
to_speed_combobox = ttk.Combobox(workerv, width=16, textvariable = to_speed_var, state = 'readonly')
to_speed_combobox.grid(row=0,column=3,padx = 5)
to_speed_combobox['values'] = speed_list
to_speed_combobox.current(3)

speed_button = ttk.Button(workerv, text = 'Convert', command = speed_fun)
speed_button.grid(row=1,padx = 5,pady = 5,column=1)


workervi = tk.LabelFrame(worker1c,text = 'Temerature Conversion')
workervi.grid(row = 2,column = 1,padx = 10,pady = 10)

temp_list = ['°Celcius','°Fahrenheit','Kelvin','°Reaumur','°Raukine']



def temp_fun():
    try:
        x =  from_temp_var.get()
        y = to_temp_var.get()
        a = float(from_temp_val.get())
        conv = [
            [a,(a-32)*5/9,a-273.15,5*a/9 - 273.15,5*a/9],
            [9*a/5+32,a,9*(a-273.15)/5 +32,a-459.67,a+32],
            [a+273.15,(a-32)*5/9 +273.15,a,5*a/9,5*a/9 +273.15],
            [(a+273.15)*9/5,a+459.67,9*a/5,a,a+491.67],
            [9*a/5,a-32,9*(a-273.15)/5,a-491.67,a]
        ]

        i = temp_list.index(x)
        j = temp_list.index(y)

        to_temp_val.set(conv[i][j])
    except:
        messagebox.showinfo('Warning', 'Input valid data')

    

from_temp_var = tk.StringVar()
from_temp_combobox = ttk.Combobox(workervi, width=16, textvariable = from_temp_var, state = 'readonly')
from_temp_combobox.grid(row=0,column=0,padx = 5)
from_temp_combobox['values'] = temp_list
from_temp_combobox.current(2)

from_temp_val = tk.StringVar()
from_temp_entry = ttk.Entry(workervi, textvariable = from_temp_val,width = 15)
from_temp_entry.grid(row = 2,column= 0,pady = 4,padx = 5)
from_temp_entry.focus_set()

to_temp_val = tk.StringVar()
to_temp_entry = ttk.Entry(workervi, text = to_temp_val,width = 15,state = 'readonly')
to_temp_entry.grid(row = 2,column= 3,pady = 4,padx = 5)


to_temp_var = tk.StringVar()
to_temp_combobox = ttk.Combobox(workervi, width=16, textvariable = to_temp_var, state = 'readonly')
to_temp_combobox.grid(row=0,column=3,padx = 5)
to_temp_combobox['values'] = temp_list
to_temp_combobox.current(3)

temp_button = ttk.Button(workervi, text = 'Convert', command = temp_fun)
temp_button.grid(row=1,padx = 5,pady = 5,column=1)


#-----------------------------Main menu functionality-----------------------------



def guide():
    guide_win = tk.Toplevel()
    guide_win.title('Guide')
    guide_win.geometry('600x530')
    guide_win.resizable(0,0)

    label_frame = tk.LabelFrame(guide_win, text = 'How to use!!')
    label_frame.grid(row = 0, column = 0, padx = 25, pady = 20)

    label1 = tk.Label(label_frame, text= 'User Mannual ',font = 'Times 20')
    label1.grid(row= 1, column= 1, sticky = tk.N, padx = 40, pady = 0) 

    label2 = tk.Label(label_frame, text= 'This is an all in one calculator that is divided in following tabs for better user interface:')
    label2.grid(row= 2, column= 1, sticky = tk.W, padx = 20, pady = 20) 


    label3 = tk.Label(label_frame, text= '1. Standard mode : ', font = 'Times 15')
    label3.grid(row= 4, column= 1, sticky = tk.W, padx = 20, pady = 0) 

    label4 = tk.Label(label_frame, text= 'This mode is built to perform normal calculations. Just type the number and operations in first')
    label4.grid(row= 5, column= 1, sticky = tk.W, padx = 20) 

    label5 = tk.Label(label_frame, text= 'box and you will automatically get answer in second one. Press = to get ans in first block.')
    label5.grid(row= 6, column= 1, sticky = tk.W, padx = 20)

    label6 = tk.Label(label_frame, text= '2. Square Fitting mode : ', font = 'Times 15')
    label6.grid(row= 7 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20) 

    label7 = tk.Label(label_frame, text= f"This mode is the attraction point of this calculator, you won't find such mode in any other ")
    label7.grid(row= 8 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20, pady = 0)

    label8 = tk.Label(label_frame, text= f"device. You have to just write x and y readings in left and right blanks respectively each  ")
    label8.grid(row= 9 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20, pady = 0) 

    label9 = tk.Label(label_frame, text= f"individual reading in different lines. And you will get square fitting slope in just one click")
    label9.grid(row= 10 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20, pady = 0)

    label10 = tk.Label(label_frame, text= '3. Physics mode : ', font = 'Times 15')
    label10.grid(row= 11 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20) 

    label11 = tk.Label(label_frame, text= 'In this mode you can perform operations like average ,rms value on bulk data and can also sort')
    label11.grid(row= 12 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20, pady = 0) 

    label12 = tk.Label(label_frame, text= f"data and perform some cool stuffs like partitioning and largest increasing subsequence, Just ")
    label12.grid(row= 13 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20, pady = 0)

    label18 = tk.Label(label_frame, text= f"write data in first balnk with each individual reading in different line and get ans in second.")
    label18.grid(row= 14 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20, pady = 0)

    label13 = tk.Label(label_frame, text= '4. Scientific mode : ', font = 'Times 15')
    label13.grid(row= 15 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20) 

    label14 = tk.Label(label_frame, text= 'This mode is just like any oyher scientific calculator capable of performing any scientific')
    label14.grid(row= 16 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20, pady = 0)

    label15 = tk.Label(label_frame, text= f"or trigonometric operation. ")
    label15.grid(row= 17 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20, pady = 0)

    label16 = tk.Label(label_frame, text= '5. Conversion mode : ', font = 'Times 15')
    label16.grid(row= 18 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20) 

    label17 = tk.Label(label_frame, text= 'This mode is made to do conversion of multiple datas from one unit to another.')
    label17.grid(row= 19 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20, pady = 0)

    try:
        items = [label_frame,label1,label2,label3,label4,label5,label6,label7,label8,label9,label10,label11,label12,label13,label14,label15,label16,label17,label18]

        choosen_theme = theme_choice.get()
        color_tuple = color_dict.get(choosen_theme)
        fg_color,bg_color = color_tuple[0],color_tuple[1]

        for i in items:
            i.config(background = bg_color,foreground = fg_color)

        guide_win.config(bg = bg_color)
    except:
        pass










def sasta_calc():

    sasta_message = tk.Toplevel()
    sasta_message.title('About Sasta CalC')
    sasta_message.geometry('500x370')
    sasta_message.resizable(0,0)

    label_frame = tk.LabelFrame(sasta_message, text = 'About Sasta CalC ')
    label_frame.grid(row = 0, column = 0, padx = 25, pady = 20)

    canvas = tk.Canvas(label_frame,width = 130, height = 130)
    canvas.grid(row = 0,rowspan = 6,column = 0, padx = 10, pady = 20)
    photo = tk.PhotoImage(file = 'icons\icon3.png')
    canvas.create_image(0,0, image = photo, anchor ='nw')

    label1 = tk.Label(label_frame, text= 'Sasta CalC ',font = 'Times 20')
    label1.grid(row= 1, column= 1, sticky = tk.N, padx = 40, pady = 0) 

    label2 = tk.Label(label_frame, text= 'Unregistered')
    label2.grid(row= 2, column= 1, sticky = tk.N, padx = 40, pady = 0) 


    label4 = tk.Label(label_frame, text= 'Copyright @ Birth of Universe - 2020')
    label4.grid(row= 4, column= 1, sticky = tk.N, padx = 40, pady = 0) 

    label5 = tk.Label(label_frame, text= 'Version 1.0.0, Built 007')
    label5.grid(row= 5, column= 1, sticky = tk.N, padx = 40, pady = 10) 

    label6 = tk.Label(label_frame, text= 'Sasta CalC is a free and open source calculator, values convertor, ')
    label6.grid(row= 8 , column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0) 

    label7 = tk.Label(label_frame, text= 'and capable of doing various operations made by very talented programmer')
    label7.grid(row= 9 , column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0) 

    label8 = tk.Label(label_frame, text= 'Mr. Sachin of IITD Community.  ')
    label8.grid(row= 10 , column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0) 

    label9 = tk.Label(label_frame, text= 'This ClaC ironically to its name is a top class performer that can perform ')
    label9.grid(row= 11 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20, pady = 0) 

    label10 = tk.Label(label_frame, text= 'any operation that you want a ideal calculator to perform. Stay updated with ')
    label10.grid(row= 12 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20, pady = 0) 

    label11 = tk.Label(label_frame, text= 'our resources you will soon get one of the best softwares in the whole world.')
    label11.grid(row= 13 , column = 0,columnspan = 2 ,sticky = tk.W, padx = 20, pady = 0)

    try:
        items = [label_frame,label1,label2,label4,label5,label6,label7,label8,label9,label10,label11]

        choosen_theme = theme_choice.get()
        color_tuple = color_dict.get(choosen_theme)
        fg_color,bg_color = color_tuple[0],color_tuple[1]

        for i in items:
            i.config(background = bg_color,foreground = fg_color)

        sasta_message.config(bg = bg_color)
        canvas.config(background = bg_color)
    except:
        pass




    sasta_message.mainloop()





def creator():
    global the_creator_icon
    creator = tk.Toplevel()
    creator.title('About The Creator')
    creator.geometry('565x450')
    creator.resizable(0,0)

    label_frame = tk.LabelFrame(creator, text = 'About The Creator ')
    label_frame.grid(row = 0, column = 0, padx = 25, pady = 20)

    canvas = tk.Canvas(label_frame,width = 120, height = 150)
    canvas.grid(rowspan = 10,columnspan = 1, padx = 10, pady = 20)
    # photo = tk.PhotoImage(file = 'icons\the_creator.png')
    canvas.create_image(0,0, image = the_creator_icon, anchor ='nw')


    label1 = tk.Label(label_frame, text= 'SACHIN ',font = 'Times 25 bold')
    label1.grid(row= 3, column= 1, sticky = tk.N, padx = 40, pady = 0) 

    label2 = tk.Label(label_frame, text= '                   - the creator')
    label2.grid(row= 4, column= 1, sticky = tk.N, padx = 40, pady = 0)
   
 
    label6 = tk.Label(label_frame, text= 'Mr. Sachin is a top class devoloper currently studying in one of the most prestigious ')
    label6.grid(row= 10 , column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0) 

    label7 = tk.Label(label_frame, text= 'institutes of India, going to complete his degree in 2023.')
    label7.grid(row= 11, column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0) 

    label8 = tk.Label(label_frame, text= 'This software is his one of the earliest work.Stay updated with his work you are definately ')
    label8.grid(row= 13 , column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0) 

    label9 = tk.Label(label_frame, text= 'going to get astonished with his every creation. ')
    label9.grid(row= 14 , column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0) 

    label11 = tk.Label(label_frame, text= 'You can follow his works from these direct links: ')
    label11.grid(row= 15, column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0) 

    label10 = tk.Label(label_frame, text= 'Facebook:  ')
    label10.grid(row= 16 , column = 0 ,sticky = tk.NW, padx = 20, pady = 0)

    data = tk.StringVar()
    data.set('https://www.facebook.com/profile.php?id=100010131825138')
    w = tk.Entry(label_frame, text = data, width = 55,state = 'read')
    w.grid(row = 16,column = 0,columnspan = 2,sticky = tk.NW, padx = 80)

    label12 = tk.Label(label_frame, text= 'Instagram:')
    label12.grid(row= 17, column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0)

    data2 = tk.StringVar()
    data2.set('https://www.instagram.com/_.mr._sachin._/')
    w2 = tk.Entry(label_frame, textvariable = data2, state = 'readonly', width = 55)
    w2.grid(row = 17,column = 0,columnspan = 2,sticky = tk.NW, padx = 80)

    label13 = tk.Label(label_frame, text= 'Youtube: Under Construction........')
    label13.grid(row= 18, column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0)

    label14 = tk.Label(label_frame, text= 'WebPage: Under Construction........')
    label14.grid(row= 19, column = 0,columnspan = 2 ,sticky = tk.NW, padx = 20, pady = 0)
    

    try:
        items = [label_frame,label1,label2,label6,label7,label8,label9,label10,label11,label12,label13,label14]

        choosen_theme = theme_choice.get()
        color_tuple = color_dict.get(choosen_theme)
        fg_color,bg_color = color_tuple[0],color_tuple[1]

        for i in items:
            i.config(background = bg_color,foreground = fg_color)

        creator.config(bg = bg_color)
        canvas.config(background = bg_color)
    except:
        pass

    creator.mainloop()

help.add_command(label = 'Guide', compound = tk.LEFT, command = guide)
help.add_separator()
help.add_command(label = 'About Sasta CalC', compound = tk.LEFT, command = sasta_calc)
help.add_separator()
help.add_command(label = 'About The Creator', compound = tk.LEFT, command = creator)


working_area = [worker,worker1,worker2,worker1a,worker2a,worker3a,worker1b,worker1c,workeri,workerii,workeriii,workeriv,workerv,workervi]
mode_list = [standard,square_fit,physics,scientific,convertor]

def change_theme():
    choosen_theme = theme_choice.get()
    color_tuple = color_dict.get(choosen_theme)
    fg_color , bg_color = color_tuple[0], color_tuple[1]
    for item in working_area:
        item.config(background = bg_color, foreground = fg_color)
    for item in mode_list:
        item.config(background = bg_color)


count = 0
for i in color_dict:
    color_theme.add_radiobutton(label = i, image = color_icons[count], variable = theme_choice,  compound = tk.LEFT,command = change_theme)
    count += 1



# -----------------------------END MAIN MENU FUNCTIONALITY----------------------------


main_app.config(menu=mainmenu)


main_app.mainloop()
