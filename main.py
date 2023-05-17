import tkinter as tk
from PIL import ImageTk, Image
import os

class PhotoGallary:
    def __init__(self, master):
        self.master = master
        master.title('Photo gallary')
        
        #frame to hold photo
        self.frame = tk.Frame(master)
        self.frame.pack()
        
        #load the images from a directory
        self.images = []
        self.current_images = 0
        for filename in os.listdir('images'):
            if filename.endswith('.png'):
                image = Image.open(os.path.join("images", filename))
                image = image.resize((400,400), Image.ANTIALIAS)
                self.images.append(ImageTk.PhotoImage(image))
                
        #create a lable to display
        self.label = tk.Label(self.frame, image=self.images[self.current_images])
        self.label.pack()
        
        #create buttons to change images
        prev_button = tk.Button(master, text="prev",command=self.prev_image)
        prev_button.pack(side=tk.LEFT)
        
        next_button = tk.Button(master, text="next",command=self.next_image)
        prev_button.pack(side=tk.RIGHT)
        
    def prev_image(self):
        self.current_images -= 1
        if self.current_images < 0:
            self.current_images = len(self.images) -1
        self.label.config(image=self.images[self.current_images])
        
    def next_image(self):
        self.current_images += 1
        if self.current_images == len(self.images):
            self.current_images = 0
        self.label.config(image=self.images[self.current_images])

root  = tk.Tk()
photo_gallary =  PhotoGallary(root)
root.mainloop()       