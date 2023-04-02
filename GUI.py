#imports
import tkinter as tk
import tkinter.filedialog as filedialog #for the save as file dialogue
from ahkLogo import create #the PIL functions are included here

#COLORS FOR THE GUI
PRIMARY_COLOR = "#b71c1c"
LIGHT_COLOR = "#f05545"
DARK_COLOR = "#7f0000"
DARK_ACTIVE = "#490000" #When a button is clicked (active)

#The entire software: the GUI

    def __init__(self) -> None:
        self.root = tk.Tk()

        self.root.geometry("800x300")
        self.root.config(bg = PRIMARY_COLOR)

        #if icon.ico exists it will set it as the gui's icon
        try:
            self.root.iconbitmap("icon.ico")
        except Exception as e:
            print(e) #prints to the console

        #sets minimum size to 800x300
        self.root.minsize(800, 300)

        self.user_label = tk.Label(self.root,text="AHK Logo Creator", font=("Calibri",30,"bold"), fg="white" ,bg=DARK_COLOR, width=1000)
        self.user_label.pack(pady=0)

        self.username_text = tk.Label(self.root,text="Text For The Logo:", font=("Calibri",15,"bold"), bg=PRIMARY_COLOR, fg="white")
        self.username_text.pack(pady=5)    

        self.user_entry = tk.Entry(self.root, width=60, font=("Calibri",18),fg="white", bg=LIGHT_COLOR, border=0)
        self.user_entry.pack()


        self.copy_bttn = tk.Button(self.root, height=1, width=15,text="PREVIEW LOGO", font=("Calibri",14), command=lambda:self.preview(),fg="white", bg=DARK_COLOR, border=0, activebackground=DARK_ACTIVE, activeforeground='white')
        self.copy_bttn.pack(pady=20)        

        self.download_bttn = tk.Button(self.root, height=1, width=15,text="DOWNLOAD", font=("Calibri",14), command=lambda:self.download_logo(),fg="white", bg=DARK_COLOR, border=0, activebackground=DARK_ACTIVE, activeforeground='white')
        self.download_bttn.pack()


        tk.mainloop()
    
    def preview(self) -> None:
        create(self.user_entry.get()).show()


    def download_logo(self) -> None:
        try:
            file=filedialog.asksaveasfilename(filetypes=[('PNG', '*.png')], defaultextension=".png")
            
            #saves the file to the file path
            create(self.user_entry.get()).save(file)

        #to not show the error when clicking cancel or not saving
        except:
            pass


if __name__ == '__main__':
    try:
        Software()
    except Exception as e:
        print(e) #prints to the console
        input("\n\nPress enter to quit ...")
