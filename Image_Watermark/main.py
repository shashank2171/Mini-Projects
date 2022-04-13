import sys
import tkinter as tk
from tkinter import *
from tkinter import filedialog,simpledialog
import tkinter
from PIL import ImageDraw, ImageFont, ImageTk, Image
import os
from tkinter.colorchooser import askcolor
from numpy import size

#adding watermark
def adjust_area(x,y,max_x,max_y):
    global colors,img1,filenme,image2,image1,horizontal,vertical,img3,top,flag1,flag
    if (flag) == 0:
        flag1=1
        top=Toplevel()
        top.geometry("1400x900")
    if (flag1 == 1):
        print(f"flag1={flag1}")
        flag=1
    img3=Image.open(os.getcwd()+'/Watermarked5.png')
    #image2=img1.copy()
    image2=img3.resize((1300,760))
    image2.save(os.getcwd()+'/temp.png')
    image1=ImageTk.PhotoImage(Image.open(os.getcwd()+'/temp.png'))
    #image2.show()
    Label(top,text="Move Slider To Set Watermark Position And Click Adjust",font=('calibre',16, 'bold')).grid(row=0,column=0)
#vertical slider     
    vertical=Scale(top,from_=0,to=max_y,length=760)
    vertical.grid(row=1,column=1)
#image as label
    Label(top,image=image1).grid(row=1,column=0)
#horizontal slider
    horizontal=Scale(top,from_=0,to=max_x,orient=HORIZONTAL,length=1200)
    horizontal.grid(row=2,column=0)
    horizontal.set(x)
    vertical.set(y)
    x=horizontal.get()
    y=vertical.get()
#adjust button
    Button(top,text="ADJUST",command=lambda:process_text(horizontal.get(),vertical.get())).grid(row=0,column=1)
    x=horizontal.get()
#shows new file
   # image.show()
#saves new file
   # image.save("D:/Games/Watermarked5.png")   
def process_text(x,y):
    global colors,img1,filenme,image2,image1,horizonatal,vertical,img3
    image = Image.open(filename)
    img1=ImageTk.PhotoImage(Image.open(filename))
    draw = ImageDraw.Draw(image)
    num=int(clicked.get())
    font = ImageFont.truetype('arial.ttf', num)
    txt=txt_var.get()
    textwidth,textheight=draw.textsize(txt,font)
    width,height=image.size
    margin=10
    #print(x)
    #print(y)
    max_x=width-textwidth-margin
    max_y=height-textheight-margin
    #print (f'{width},{x} , {y}')
    draw.text((x,y), str(txt_var.get()), fill=colors[0], font=font)
    image.save(os.getcwd()+'/Watermarked5.png')
    adjust_area(x,y,max_x,max_y)
#select colour of text watermark
def change_color():
    global colors,txt_entry,font_size,clicked,flag,flag1
    colors=askcolor(title="SELECT A COLOUR FOR TEXT")
    clicked=StringVar()
    clicked.set(26)
#font size options
    font_options=[20,26,30,36,54,64,82,100,125,150,200,300,500]
    Label(main_window,text="Select font size").grid(row=2,column=1)
    font_size=OptionMenu(main_window,clicked,*font_options)
    font_size.grid(row=2,column=2,sticky="w",padx=10)
#label to enter text 
    txt_label=tk.Label(main_window, text = 'TEXT', font=('calibre',10, 'bold')).grid(row=3,column=0)
#field to enter text
    txt_entry=tk.Entry(main_window, textvariable = txt_var,width=12, font=('calibre',10,'normal')).grid(row=3,column=1)
    flag=flag1=0
    
#button to process
    button_process_text=Button(main_window,text="PROCESS",command=lambda:process_text(0,0))
    button_process_text.grid(row=3,column =2,sticky="w",padx=10)
    flag=flag1=0
def process_image_watermark(x,y,max_x,max_y):
    global flag,flag1,base_image,watermark_image,image2,image1,img3,top
    flag1=0
    if flag == 0:
        flag1=1
        top=Toplevel()
        top.geometry("1400x900")
    if (flag1 == 1):
        print(f"flag1={flag1}")
        flag=1
    
    img3=Image.open(os.getcwd()+'/Watermarked_image.png')
    #image2=img1.copy()
    image2=img3.resize((1300,760))
    image2.save(os.getcwd()+'/temp.png')
    image1=ImageTk.PhotoImage(Image.open(os.getcwd()+'/temp.png'))
    #image2.show()
    Label(top,text="Move Slider To Set Watermark Position And Click Adjust",font=('calibre',16, 'bold')).grid(row=0,column=0)
   #watermark_image.thumbnail(size)
   #base_image.paste(watermark_image,position)
    Label(top,image=image1).grid(row=1,column=0)
    horizontal=Scale(top,from_=0,to=max_x,orient=HORIZONTAL,length=1200)
    vertical=Scale(top,from_=0,to=max_y,length=760)
    horizontal.grid(row=2,column=0)
    vertical.grid(row=1,column=1)
    horizontal.set(x)
    vertical.set(y)
    x=horizontal.get()
    y=vertical.get()
    Button(top,text="ADJUST",command=lambda:select_logo(horizontal.get(),vertical.get())).grid(row=0,column=1)
#select image water mark
def select_logo(x,y):
    global filename1,label_file_explorer,label_file_explorer1,base_image,watermark_image,flaag,flaag1,width1,height1
    label_file_explorer1.grid(column = 1, row = 2)
    position=(x,y)
    base_image=Image.open(filename)
    watermark_image=Image.open(filename1)
    width,height=base_image.size
    width1,height1=watermark_image.size
    if((width1*height1)>(0.3*(width*height))):
      width1=int(width*0.3)
      height1=int(height*0.3)
      watermark_image=watermark_image.resize((width1,height1))
   #  watermark_image.show()
    base_image.paste(watermark_image,position)
   # base_image.show()
    base_image.save(os.getcwd()+'/Watermarked_image.png')
    #base_image.show()
    #process_image_watermark
    #image=Image.open(filename1)
    #print(width1)
    #print(width)
    max_x=width-width1
    max_y=height-height1
    process_image_watermark(x, y, max_x, max_y)
#on selection of type of watermark asks for input
def select_type(choice):
    global colorButton,label_file_explorer1,filename1,txt_label,txt_entry
#if selectionis text
    if choice == 1:
        image_option_button.destroy()
        colorButton=Button(main_window,text="Pick Colour",command=change_color)
        colorButton.grid(row=2,column=0,pady=7)
#if selection is image
    if choice == 2:
        global watermark_image,filename
        text_option_button.destroy()
        #button_select_logo = Button(main_window,text = "Select Watermark", command = select_logo(0,0))
        filename1 = filedialog.askopenfilename(initialdir =os.getcwd(),title = "Select a Watermark Image",filetypes = (("Image files", ".png"),("all files",".")))
        label_file_explorer1 = Label(main_window, fg = "blue")
        label_file_explorer1.configure(text="WATERMARK IMAGE: "+filename1)
        #button_select_logo.grid(row=2,column=0)
        select_logo(0,0)
#to select main image file then shows option between text and image type
def browseFiles():
    global filename, text_option_button,image_option_button
    filename = filedialog.askopenfilename(initialdir =os.getcwd(),title = "Select a File",filetypes = (("Image files", ".png"),("all files",".")))    
    label_file_explorer.configure(text="BASE IMAGE:\n"+filename)
    r=IntVar()
    #option to select watermark type
    image_option_button=Radiobutton(main_window,text="IMAGE",variable=r,value=2)
    image_option_button.grid(row=1,column=2)
    text_option_button=Radiobutton(main_window,text="TEXT",variable=r,value=1)
    text_option_button.grid(row=1,column=1)
    select_type_button=Button(main_window,text="Select Type",padx=3,command=lambda:select_type(r.get())).grid(row=1,column=0)
#restarts gui
def new_file():
    global main_window,button_explore
#destroy old window
    main_window.destroy()
    main()
def main():    
    #main window created
    global main_window,label_file_explorer,txt_var,flag,flaag
    main_window=tk.Tk()
    main_window.title("Watermark Images")
#window size set
    main_window.geometry('600x200')
    txt_var=tk.StringVar()
    flag=0
    flaag=0
    label_file_explorer = Label(main_window, fg = "blue")
    button_explore = Button(main_window,text = "Select Image", command = browseFiles)
    label_file_explorer.grid(column = 2, row = 0)
    button_explore.grid(column = 1, row = 0)
#new file button
    Button(main_window,text="New File",command=new_file,).grid(row=0,column=0,ipadx=10)
#loop for gui
    main_window.mainloop()
main()
