from pptx import Presentation
from tkinter import *
from PIL import Image, ImageTk
import urllib.request
prs = Presentation('test.pptx')

class InputPage(Frame):
    def __init__(self, parent, controller,*args, **kwargs):
        Frame.__init__(self,parent,*args,**kwargs)
        #set frame's app
        self.app = controller

        #create upload presentation frame
        presentationFrame = Frame(self)
        presentationLabel = Label(presentationFrame, text="Upload your presentation:",font="Arial 14 bold")
        presentationLabel.pack()
        presentationFrame.pack(pady=10)

        #create sentiment frame
        sentimentsFrame = Frame(self)
        sentimentsLabel = Label(sentimentsFrame, text="Select the intended sentiment(s):",font="Arial 14 bold")
        sentimentsLabel.pack()
        sentimentsFrame.pack(pady=10)

        # create dictionary with sentiments
        self.sentiments = {'Joy':"",
        'Sadness':"",
        'Anger':"",
        'Disgust':"",
        'Surprise':"",
        'Anticipation':"",
        'Trust':"",
        'Sarcasm':"",
        'Shame':"",
        'Fear':"",
        'Triumphant':"",
        'Confused':""}

        #create checkboxes for sentiments
        for item in self.sentiments:
            value = IntVar()
            checkbox = Checkbutton(sentimentsFrame, text=item, variable=value)
            checkbox.var = value
            self.sentiments[item]=checkbox
            checkbox.pack()

        #create audience frame
        audienceFrame = Frame(self)
        audienceLabel = Label(audienceFrame, text="Select the intended audience(s):", font="Arial 14 bold")
        audienceLabel.pack()
        audienceFrame.pack(pady=10)

        # create dictionary with audience
        self.audience = {'Friends':"",
        'Class - Peers':"",
        'Class - Internals and Faculty':"",
        'Work - Internals':"",
        'Work - Clients':""}

        #create checkboxes for audience
        for item in self.audience:
            value = IntVar()
            checkbox = Checkbutton(audienceFrame, text=item, variable=value)
            checkbox.var = value
            self.audience[item]=checkbox
            checkbox.pack()

        submitButton = Button(self, text="Reco-meme!", command=lambda : self.sendRequest())
        submitButton.pack()

    # send request for selected inputs and presentation
    def sendRequest(self):
        selectedSentiments = []
        selectedAudience = []

        for item in self.sentiments:
            value = self.sentiments[item].var.get()
            if value != 0:
                selectedSentiments.append(item)
        print("selected sentiments: ", selectedSentiments)

        for item in self.audience:
            value = self.audience[item].var.get()
            if value != 0:
                selectedAudience.append(item)
        print("selected audience: ", selectedAudience)

        self.app.show_frame(OutputPage)

        return selectedSentiments, selectedAudience

class OutputPage(Frame):
    def __init__(self, parent, controller,*args, **kwargs):
        Frame.__init__(self,parent,*args,**kwargs)

        #create recommendations frame
        recommendationsFrame = Frame(self)
        recommendationsLabel = Label(recommendationsFrame, text="Your Top 5 Recommended Memes",font="Arial 16 bold")
        recommendationsLabel.pack(fill=X)
        recommendationsFrame.pack(fill=X)

        #create dictionary for recommended memes, TODO: need recommended memes and somehow get their urls and name
        recommendations = ['1','2','3','4','5']

        #retrieve the images
        for i in range(len(recommendations)):
            memeFrame = Frame(self)
            memeFrame.pack(fill=X, pady=10)

            #download meme image. TODO: need to replace with meme's url and meme's filename
            urllib.request.urlretrieve("http://i.qkme.me/353mvs.jpg","testimagename" + recommendations[i] + ".jpg")

            basewidth = 200
            image = Image.open("testimagename1.jpg") #TODO: input meme's filename
            wpercent = (basewidth / float(image.size[0]))
            hsize = int((float(image.size[1]) * float(wpercent)))
            image = image.resize((basewidth, hsize), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)

            memeImage = Label(memeFrame, image=photo)
            memeImage.image = photo
            memeImage.pack(fill=X)

            memeLabel = Label(memeFrame, text="Meme" + "ID/category") #TODO: replace with meme's metadata
            memeLabel.pack(fill=X)


class RecomemederUI(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("The Reco-MEME-der")
        self.minsize(width=800, height=800)
        self.maxsize(width=1000, height=1000)
        self.configure(background='#E1ECF4')

        #create the main container to that other frames will be raised into
        self.container = Frame(self, background='#444444')
        self.container.pack(side='top', fill='both', expand=True)
        #create the dictionary of frames
        self.frames = {}

        #create the static pages
        for F in (InputPage, OutputPage):
            #create the frame and add it to the application's frames dictionary
            frame = F(self.container, self, width=1000, height=1000, bg='white')
            self.frames[F] = frame
            frame.grid(row=0, column=0)
        self.show_frame(InputPage)

    def show_frame(self, cont):
        '''Function to display a certain frame. Takes in the name of the frame.'''
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == '__main__':
    app = RecomemederUI()
    app.mainloop()
