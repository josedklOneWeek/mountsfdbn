

import tkinter as tk


class GFkg():
    def __init__(self):

        self.v1 = tk.Tk()

        self.bds1 = tk.Button(self.v1,text="1")
        self.bds1.grid(column=0,row=0)
        
        self.bds2 = tk.Button(self.v1,text="2")
        self.bds2.grid(column=2,row=0)

        self.bds3 = tk.Button(self.v1,text="3", width=20)
        self.bds3.grid(column=3,row=0)




        


        self.v1.mainloop()

        #print("")



# ----------------------------------------------------------
# 
app = GFkg()        