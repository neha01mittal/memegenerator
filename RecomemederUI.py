from pptx import Presentation
from tkinter import *
from PIL import Image, ImageTk
import urllib.request

# text_runs will be populated with a list of strings,
# one for each text run in presentation
def get_ppt_text(filename):
    prs = Presentation(filename)
    text_runs = []
    for slide in prs.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    text_runs.append(run.text)
    print(text_runs)
    return test_runs

class InputPage(Frame):
    def __init__(self, parent, controller,*args, **kwargs):
        Frame.__init__(self,parent,*args,**kwargs)
        #set frame's app
        self.app = controller

        #create upload presentation frame
        presentationFrame = Frame(self)
        presentationLabel = Label(presentationFrame, text="Enter your presentation filename:",font="Arial 14 bold")
        presentationLabel.pack()
        self.presentationEntry = Entry(presentationFrame, width = 20)
        self.presentationEntry.pack()
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

        presentationFilename = self.presentationEntry.get() + '.pptx'
        print("presentation filename: ", presentationFilename)

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

        #create the output page TODO: call this function somewhere with inputs on the recommended memes to create the output
        self.createOutputPage()

        return presentationFilename, selectedSentiments, selectedAudience

    # TODO: add parameter for recommended memes information
    def createOutputPage(self):
        outputFrame = OutputPage(self.app.container, self)
        outputFrame.pack()
        outputFrame.tkraise()

        #destroy the input frame
        self.destroy()

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
        self.container = Frame(self, background='white')
        self.container.pack(side='top', fill='both', expand=True)

        #create the input page
        inputFrame = InputPage(self.container, self)
        inputFrame.pack()

if __name__ == '__main__':
    app = RecomemederUI()
    app.mainloop()
