from Tkinter import *
class Application(Frame):
    """this is the good source code for future development"""
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):

        """Create buttons, and associated text and entry"""
        self.instruction = Label(self, text = "Welcome to the world famous IQ test!")
        self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        self.q1Answer = IntVar()
        self.q2Answer = IntVar()
        self.q3Answer = IntVar()
        self.q4Answer = IntVar()

        self.questionN1 = Label(self, text = "1. What is 1 + 2 + 3 + 4 + ......?")
        self.questionN1.grid(row = 1, column = 0, sticky = W)

        self.Radiobutton1 = Radiobutton(self, text="I don't know", variable=self.q1Answer, value=1,
                                        command=self.update_one).grid(row = 2, column = 0, sticky = W)
        self.Radiobutton2 = Radiobutton(self, text="Infinity", variable=self.q1Answer, value=4,
                                        command=self.update_one).grid(row=3, column=0, sticky=W)
        self.Radiobutton3 = Radiobutton(self, text="-1/12", variable=self.q1Answer, value=5,
                                        command=self.update_one).grid(row=4, column=0, sticky=W)

        self.questionN2 = Label (self, text = "2. Which pair of those two words are closest in meaning?")
        self.questionN2.grid(row=5, column=0, sticky=W)

        self.Radiobutton4 = Radiobutton(self, text="talkative and wind", variable=self.q2Answer, value=1,
                                        command=self.update_one).grid(row=6, column=0, sticky=W)
        self.Radiobutton5 = Radiobutton(self, text=" job and angry", variable=self.q2Answer, value=2,
                                        command=self.update_one).grid(row=7, column=0, sticky=W)
        self.Radiobutton6 = Radiobutton(self, text="ecstatic and angry", variable=self.q2Answer, value=4,
                                        command=self.update_one).grid(row=8, column=0, sticky=W)
        self.Radiobutton7 = Radiobutton(self, text="talkative and loquacious", variable=self.q2Answer, value=5,
                                        command=self.update_one).grid(row=9, column=0, sticky=W)

        self.questionN3 = Label(self, text="3. Which one of the following five letters can be arranged to form "
                                           "an english word?")
        self.questionN3.grid(row=10, column=0, sticky=W)

        self.Radiobutton4 = Radiobutton(self, text="H R G S T", variable=self.q3Answer, value=3,
                                        command=self.update_one).grid(row=11, column=0, sticky=W)
        self.Radiobutton5 = Radiobutton(self, text=" R I L S A", variable=self.q3Answer, value=1,
                                        command=self.update_one).grid(row=12, column=0, sticky=W)
        self.Radiobutton6 = Radiobutton(self, text="T O O M T", variable=self.q3Answer, value=5,
                                        command=self.update_one).grid(row=13, column=0, sticky=W)
        self.Radiobutton7 = Radiobutton(self, text="W Q R G S", variable=self.q3Answer, value=2,
                                        command=self.update_one).grid(row=14, column=0, sticky=W)

        self.questionN4 = Label(self, text="4. Which one of the images comes next? Please see the reference below")
        self.questionN4.grid(row=15, column=0, sticky=W)

        self.photo = PhotoImage(file="R2.gif")
        self.P4Label = Label(root, image=self.photo)
        self.P4Label.photo = self.photo
        self.P4Label.grid(row=16, column=0, sticky=W)


        self.Radiobutton8 = Radiobutton(self, text="a", variable=self.q4Answer, value=1,
                                        command=self.update_one).grid(row=21, column=0, sticky=W)
        self.Radiobutton9 = Radiobutton(self, text="b", variable=self.q4Answer, value=2,
                                        command=self.update_one).grid(row=22, column=0, sticky=W)
        self.Radiobutton10 = Radiobutton(self, text="c", variable=self.q4Answer, value=5,
                                        command=self.update_one).grid(row=23, column=0, sticky=W)
        self.Radiobutton11 = Radiobutton(self, text="d", variable=self.q4Answer, value=3,
                                        command=self.update_one).grid(row=24, column=0, sticky=W)

        self.result = Text(self, width = 40, height = 5, wrap = WORD)
        self.result.grid(row = 25, column = 0, columnspan = 3)



    def update_one(self):

        message = "Your total IQ is:"
        q1a = self.q1Answer.get()
        q2a = self.q2Answer.get()
        q3a = self.q3Answer.get()
        q4a = self.q4Answer.get()

        raw_score = 0
        raw_score = raw_score + q1a+q2a+q3a+q4a

        message = message + str(raw_score*6+60)
        """message = message + str(q1a) +str(q2a)+str(q3a)+str(q4a)"""
        self.result.delete(0.0, END)
        self.result.insert(0.0, message)


        """references that I take from the web pages"""
        """http://examples.yourdictionary.com/examples-of-iq-questions.html"""
        """https://puzzling.stackexchange.com/questions/14953/questions-from-iq-test-that-i
        -couldnt-find-reasonable-answers-for"""

root = Tk()
root.title("The 4 Question IQ Test")
root.geometry("550x850")
app = Application(root)

root.mainloop()
