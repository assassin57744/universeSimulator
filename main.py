from tkinter import *
from tkinter import messagebox
import friedmann as fd

#TODO: transfer the parameter entered into friedmann.py for furthur calculation

#declaring the UI
class userInterface:
    def __init__(self, root):
        root.title("Universe Simulator")
        root.geometry("600x600")

        #making the title for the UI
        largeTitle = Label(root, text="Universe Simulator")
        largeTitle.config(font=("Computer Modern", 30))
        largeTitle.pack()

        #defining the place to input parameters
        radiationPrompt = Label(root, text="Radiation Parameter", font=("Computer Modern", 15))
        radiationPrompt.pack()

        self.inputRadiation = Entry(root, width=50, bg="light yellow", font=("Computer Modern", 12))
        self.inputRadiation.pack(pady=(2,10))

        matterPrompt = Label(root, text="Matter Parameter", font=("Computer Modern", 15))
        matterPrompt.pack()

        self.inputMatter = Entry(root, width=50, bg="light yellow", font=("Computer Modern", 12))
        self.inputMatter.pack(pady=(2,10))

        lambdaPrompt = Label(root, text="Dark Energy Parameter", font=("Computer Modern", 15))
        lambdaPrompt.pack()

        self.inputLambda = Entry(root, width=50, bg="light yellow", font=("Computer Modern", 12))
        self.inputLambda.pack(pady=(2,10))

        hubblePrompt = Label(root, text="Hubble Constant (km/s/Mpc)", font=("Computer Modern", 15))
        hubblePrompt.pack()

        self.inputHubble = Entry(root, width=50, bg="light yellow", font=("Computer Modern", 12))
        self.inputHubble.pack(pady=(2,10))

        boundPrompt = Label(root, text="Terminating Time (Gyr)", font=("Computer Modern", 15))
        boundPrompt.pack()

        self.inputBound = Entry(root, width=50, bg="light yellow", font=("Computer Modern", 12))
        self.inputBound.pack(pady=(2,10))

        accuracyPrompt = Label(root, text="Sample Space", font=("Computer Modern", 15))
        accuracyPrompt.pack()

        self.inputAccuracy = Entry(root, width=50, bg="light yellow", font=("Computer Modern", 12))
        self.inputAccuracy.pack(pady=(2,10))

        #adding button to the UI
        self.btn = Button(root, text="Simulate", font=("Computer Modern", 20), command=self.getAndRun)
        self.btn.pack()

        self.defaultHubble = False
        self.defaultBound = False
        self.defaultAccuracy = False

    def getAndRun(self):
        hubble = self.inputHubble.get()
        bound = self.inputBound.get()
        accuracy = self.inputAccuracy.get()

        omegaR = self.inputRadiation.get()
        omegaM = self.inputMatter.get()
        omegaL = self.inputLambda.get()

        if(omegaR == "" or omegaM == "" or omegaL == ""):
            messagebox.showerror("VALUE ERROR", "Must enter radiation parameter, matter parameter and dark energy parameter")
            return

        try:
            omegaR = float(omegaR)
            omegaM = float(omegaM)
            omegaL = float(omegaL)
                     
        except ValueError:
            messagebox.showerror("VALUE ERROR", "Please enter number only")
            return
        
        if (omegaR < 0 or omegaM < 0):
            messagebox.showerror("VALUE ERROR", "Radiation parameter and matter parameter must be greater than 0")
            return
        
        try:
            if(hubble == ""):
                hubble = 70.0
            else:
                hubble = float(hubble)
            
            if(bound == ""):
                bound = 5.0
            else:
                bound = float(bound)

            if(accuracy == ""):
                accuracy = 0.0005
            else:
                accuracy = float(accuracy)

        except ValueError:
            messagebox.showerror("VALUE ERROR", "Please enter number only")
            return

        uni = fd.universe(omegaR, omegaM, omegaL, hubble)

        uni.plotResult(bound, accuracy)

if __name__ == "__main__":
    root = Tk()
    app = userInterface(root)
    root.mainloop()
