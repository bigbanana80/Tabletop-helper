import customtkinter 
import random

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

global dice 


#Functions/////////////////////////////////
def dice_type_changer(number):
    if number == "Coin":
        dice_number = 2
    elif number == "D4":
        dice_number = 4
    elif number == "D6":
        dice_number = 6
    elif number == "D8":
        dice_number = 8
    elif number == "D10":
        dice_number = 10
    elif number == "D12":
        dice_number = 12
    elif number == "D20":
        dice_number = 20
    elif number == "D100":
        dice_number = 100
    print(dice_number)
    global dice 
    dice = dice_number

    
def RollTheDice(number):
    global label_value
    token = random.randint(1,number)
    if dice == 2:
        if token == 1:
            label_value = "Head"
        elif token == 2:
            label_value = "Tail"
    else:
        label_value =str(token)
    print("result is "+str(token))
    result.configure(text = label_value)
    
def button_roll():
    RollTheDice(dice)
#//////////////////////////////////////////

# Main app ///////////////////////////////
root=customtkinter.CTk()
root.geometry("700x450")

frame=customtkinter.CTkFrame(master = root)
frame.pack(pady=20 ,padx=60 ,fill="both" ,expand=True )

dice_selector = customtkinter.CTkOptionMenu(master = frame,
                                            values=["Coin","D4","D6","D8","D10","D12","D20","D100"],
                                            command=dice_type_changer)
dice_selector.pack(pady=10,padx=12)

roll_button = customtkinter.CTkButton(master=frame,text="Activate",command=button_roll)
roll_button.pack(pady=10,padx=12)

result = customtkinter.CTkLabel(master = frame, text_color="#349bf1",text ="---",font=("Roboto", 24))
result.pack(pady = 100 , padx=12)



root.mainloop()
#//////////////////////////////////////////