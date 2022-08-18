from tkinter import ttk # design frame 
import tkinter as tk # design frame 
from tkinter import messagebox # message , file chosen (browse)
import phonenumbers
from phonenumbers import carrier, geocoder , timezone

root = tk.Tk() # Frame structure
root.geometry("850x400") # height , width
root.title("OI True Caller") # title
root.minsize(850,400)
root.maxsize(850,400) 
root.resizable(False,False) # control in width and height

# Creating A Frame
frame = ttk.LabelFrame(root,text="Phone Number Input")
frame.grid(row=0,column=0,padx=70,pady=90)

# Entery lable
get_info = ttk.Label(frame,text="Enter Your Phone Number")
get_info.grid(row=0,column=0,padx=3,pady=20,sticky=tk.W)

# Recive A URL
number = tk.StringVar()

# Entry Field
ph_num = ttk.Entry(frame,width=60,textvariable=number,font=('Times',"18","bold"))
ph_num.grid(row=1,columnspan=3,padx=3,pady=3)
ph_num.focus()


# back-end
def truecaller():
    got_num = number.get()
    mob_num = phonenumbers.parse(got_num)
    country=timezone.time_zones_for_number(mob_num)[0]
    messagebox.showinfo("Number Information",f"""
    [1] Continent : {country[0:country.index('/')]}
    [2] Country : {geocoder.description_for_number(mob_num,'en')}
    [3] Network : {carrier.name_for_number(mob_num,'en')} 
    [4] Valid Mobile Number : {phonenumbers.is_valid_number(mob_num)}
    [5] Checking Possibilty of number : {phonenumbers.is_possible_number(mob_num)}
    """)
button = ttk.Button(frame,text="Get Number Info",width=15,command=truecaller)
button.grid(row=4,columnspan=3,padx=13,pady=8)    

root.mainloop() # Run Frame