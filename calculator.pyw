# Welcome, this is just a very simple tkinter calculator i made. This was the very first thing I made in tkinter, so understandably its not spectacular

# it has a dedicated arithmetic parser, made from scratch. Its actually pretty simple. You can use a library if you would like to do this project yourself, and for most things that is more convinent
# its also good to understand the algorithm to make these yourself
# This is in the public domain so feel free to use this for whatever
import math, random, tkinter as tk, operator
from tkinter import ttk
from tkinter import *

# just a simple python GUI calculator
# utilizes a custom expression parser. Comments will guide you how to make this 

def init(): #boot up the app
    root = Tk()
    root.geometry("420x520+10+10")
    user_input = tk.StringVar(root)

    screen = Entry(root, font=("Arial", 20),borderwidth=4, foreground="blue", textvariable=user_input)
    screen.place(width=400,height=70)
    # you can use a loop to generate the buttons, although for a small scale, it does not really matter, so i just copy and pasted
    # super ugly ik
    Bttn_1 = Button(root, command=lambda:input(screen, '1', user_input),text="1", width=6, height=3, background="lightgrey",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=40, y=77)
    Bttn_2 = Button(root, command=lambda:input(screen, '2', user_input),text="2", width=6, height=3, background="lightgrey",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=120, y=77)
    Bttn_3 = Button(root, command=lambda:input(screen, '3', user_input),text="3", width=6, height=3, background="lightgrey",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=200, y=77)
    Bttn_4 = Button(root, command=lambda:input(screen, '+', user_input),text="+", width=6, height=3, background="aqua",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=280, y=77)
    Bttn_5 = Button(root, command=lambda:input(screen, '4', user_input),text="4", width=6, height=3, background="lightgrey",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=40, y=160)
    Bttn_6 = Button(root, command=lambda:input(screen, '5', user_input),text="5", width=6, height=3, background="lightgrey",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=120, y=160)
    Bttn_7 = Button(root, command=lambda:input(screen, '6', user_input),text="6", width=6, height=3, background="lightgrey",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=200, y=160)
    Bttn_8 = Button(root, command=lambda:input(screen, '-', user_input),text="-", width=6, height=3, background="aqua",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=280, y=160)
    Bttn_9 = Button(root, command=lambda:input(screen, '7', user_input),text="7", width=6, height=3, background="lightgrey",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=40, y=245)
    Bttn_10 = Button(root, command=lambda:input(screen, '8', user_input),text="8", width=6, height=3, background="lightgrey",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=120, y=245)
    Bttn_11 = Button(root, command=lambda:input(screen, '9', user_input),text="9", width=6, height=3, background="lightgrey",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=200, y=245)
    Bttn_12 = Button(root, command=lambda:input(screen, '*', user_input),text="*", width=6, height=3, background="aqua",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=280, y=245)
    Bttn_13 = Button(root, command=lambda:input(screen, '0', user_input),text="0", width=6, height=3, background="lightgrey",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=40, y=330)
    Bttn_14 = Button(root, command=lambda:input(screen, '.', user_input),text=".", width=6, height=3, background="lightgrey",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=120, y=330)
    Bttn_15 = Button(root, command=lambda:input(screen, '^', user_input),text="x^y", width=6, height=3, background="lightgrey",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=200, y=330)
    Bttn_16 = Button(root, command=lambda:input(screen, '/', user_input),text="/", width=6, height=3, background="aqua",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=280, y=330)
    Bttn_17 = Button(root, command=lambda:sqOp(screen,user_input),text="√", width=6, height=3, background="lightgrey",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=40, y=420)
    Bttn_18 = Button(root, command=lambda:percentOp(screen,user_input),text="%", width=6, height=3, background="lightgrey",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=120, y=420)
    Bttn_19 = Button(root, command=lambda:clears(screen),text="CE", width=6, height=3, background="lightgrey",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=200, y=420)
    Bttn_20 = Button(root, command=lambda:parse(screen, user_input),text="=", width=6, height=3, background="lime",takefocus=False, highlightthickness=0, highlightcolor="#37d3ff", highlightbackground="#37d3ff", relief=SUNKEN, borderwidth=0, font=("Arial", 15)).place(x=280, y=420)
    root.mainloop()
def input(e, selection, user_input):
     e.insert(len(user_input.get()),selection)
def clears(e):
    e.delete(0,END)
def percentOp(e, raw_input): # just divides the input by 100. Pretty simple, so i made a dedicated function
    if type(float(raw_input.get())) == float or int:
        ans = float(raw_input.get()) / 100
        puts(e, ans)
    else:
        return
def sqOp(e, raw_input):
    if type(float(raw_input.get())) == float or int:
         puts(e, float(raw_input.get()) ** .5)
    return
def parse(e, raw_input): # basic parsing function, to give a general idea of how it works. Parse and evaluate all in one. Returns the answer to the expression
    ops = set('^+-*/')   # advanced parsing functions would have a better way of handeling negitive integers than I have implemented
    found_ops = []
    found_nums = []
    buffer = []
    if not type(raw_input) == int:
        raw_input = raw_input.get()
        for ch in raw_input:
            if ch in ops:  
                found_nums.append(''.join(buffer))
                buffer = []
                found_ops.append(ch)
            else:
                buffer.append(ch)
        found_nums.append(''.join(buffer))
        nums = list(found_nums)
        ops = list(found_ops)
        operator_order = ('^*/','+-')  # order of operations
        op_dict = {'^':operator.pow,'*':operator.mul,'/':operator.truediv,'+':operator.add,'-':operator.sub}
        Value = None
        for op in operator_order:                  
            while any(o in ops for o in op):       
                idx,oo = next((i,o) for i,o in enumerate(ops) if o in op) 
                if ("-" in found_ops): # Always try to avoid using eval, but since i didnt want to make a super complicated parser i did. 
                    puts(e, eval(raw_input))
                ops.pop(idx)                      
                values = map(float,nums[idx:idx+2])
                value = op_dict[oo](*values)
                nums[idx:idx+2] = [value]  
                puts(e, nums[0])
               
                return 0
    else:
        return 1
        
def puts(e, str):
     e.delete(0,END)
     e.insert(0, str)

if '__main__' == __name__:
    init()
