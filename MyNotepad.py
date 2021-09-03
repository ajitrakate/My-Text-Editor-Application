from tkinter import Scrollbar, StringVar, Text, ttk
import tkinter as tk
from tkinter import font, filedialog, colorchooser, messagebox
import os
from tkinter.constants import BOTH


main_application = tk.Tk()
main_application.geometry("1200x800")
main_application.title("Text Editor - Unsaved File")
main_application.wm_iconbitmap('icon.ico')





################################################### Main Menu ########################################################################

main_menu = tk.Menu()

##### File menu ############
file = tk.Menu(main_menu, tearoff=False)

# Icons
new_icon = tk.PhotoImage(file="icons2/new.png")
open_icon = tk.PhotoImage(file="icons2/open.png")
save_icon = tk.PhotoImage(file="icons2/save.png")
save_as_icon = tk.PhotoImage(file="icons2/save_as.png")
exit_icon = tk.PhotoImage(file="icons2/exit.png")


# Url variable

url = ''

## New file
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, 'end')
    main_application.title('Text Editor - Unsaved File')


      
## open file
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(title="Open File", initialdir=os.getcwd(), filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as f_read:
            text_editor.delete(1.0, 'end')
            text_editor.insert(1.0, f_read.read())
            main_application.title(f"Text Editor - {os.path.basename(url)}")
    except:
        mb = messagebox.Message("File not chosen")


# save_file
def save_file(event=None):
    global url
    try:
        if url:
            content = text_editor.get(1.0,'end-1c')
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
                main_application.title(f"Text Editor - {os.path.basename(url)}")
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2 = str(text_editor.get(1.0, 'end-1c'))
            url.write(content2)
            url.close()
            main_application.title(f"Text Editor - {os.path.basename(url)}")
    except:
        return




## save_as file
def save_as_file(event=None):
    global url
    try:
        content = str(text_editor.get(1.0,'end-1c'))
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return



## exit file
def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save this current file ?')
            if mbox is True:
                if url:
                    with open(url, 'w', encoding='utf-8') as fw:
                        content = text_editor.get(1.0,'end-1c')
                        fw.write(content)
                    main_application.destroy()
                else:
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    content2 = str(text_editor.get(1.0, 'end-1c'))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
            else:
                return
        else:
            main_application.destroy()
    except:
        return



file.add_command(label="New", image=new_icon, compound=tk.LEFT, accelerator="Ctrl+N", command=new_file)
file.add_command(label="Open", image=open_icon, compound=tk.LEFT, accelerator="Ctrl+O", command=open_file)
file.add_command(label="Save", image=save_icon, compound=tk.LEFT, accelerator="Ctrl+S", command=save_file)
file.add_command(label="Save As", image=save_as_icon, compound=tk.LEFT, accelerator="Ctrl+Shift+S", command=save_as_file)
file.add_command(label="Exit", image=exit_icon, compound=tk.LEFT, accelerator="Ctrl+Q", command=exit_func)


####### End File Menu #########

###### Edit Menu ###############
edit = tk.Menu(main_menu, tearoff=False)

#Icons
cut_icon = tk.PhotoImage(file="icons2/cut.png")
copy_icon = tk.PhotoImage(file="icons2/copy.png")
paste_icon = tk.PhotoImage(file="icons2/paste.png")
clear_all_icon = tk.PhotoImage(file="icons2/clear_all.png")
find_icon = tk.PhotoImage(file="icons2/find.png")


edit.add_command(label="Cut", image=cut_icon, compound=tk.LEFT, accelerator="Ctrl+X")
edit.add_command(label="Copy", image=copy_icon, compound=tk.LEFT, accelerator="Ctrl+C")
edit.add_command(label="Paste", image=paste_icon, compound=tk.LEFT, accelerator="Ctrl+V")
edit.add_command(label="Clear All", image=clear_all_icon, compound=tk.LEFT, accelerator="Ctrl+Z")
edit.add_command(label="Find", image=find_icon, compound=tk.LEFT, accelerator="Ctrl+F")

##### End Edit Menu #########

###### View menu ##############
view = tk.Menu(main_menu, tearoff=False)

# icons
tool_bar_icon = tk.PhotoImage(file="icons2/tool_bar.png")
status_bar_icon = tk.PhotoImage(file="icons2/status_bar.png")


# show_toolbar = tk.BooleanVar()
# show_toolbar.set(True)

# show_statusbar = tk.BooleanVar()
# show_statusbar.set(True)



# def hide_toolbar():
#     global show_toolbar
#     if show_toolbar:
#         tool_bar.pack_forget()
#         show_toolbar = False
#     else:

#     pass

# def hide_statusbar():
#     pass

# view.add_checkbutton(label="Tool Bar", image=tool_bar_icon, compound=tk.LEFT, onvalue=True, offvalue=False, variable=show_toolbar, command=hide_toolbar)
# view.add_checkbutton(label="Status Bar", image=status_bar_icon, compound=tk.LEFT, onvalue=True, offvalue=False, variable=show_statusbar, command=hide_statusbar)

####### End View Menu ##################

######## Color Theme Menu ################
color_theme = tk.Menu(main_menu, tearoff=False)

#icons
light_default_icon = tk.PhotoImage(file="icons2/light_default.png")
light_plus_icon = tk.PhotoImage(file="icons2/light_plus.png")
dark_icon = tk.PhotoImage(file="icons2/dark.png")
red_icon = tk.PhotoImage(file="icons2/red.png")
monokai_icon = tk.PhotoImage(file="icons2/monokai.png")
night_blue_icon = tk.PhotoImage(file="icons2/night_blue.png")

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' : ('#ededed', '#6b9dc2')
}

def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)

count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icons[count], compound=tk.LEFT, variable=theme_choice, command=change_theme)
    count += 1

######### End Color Theme Menu ###########

main_menu.add_cascade(label="File", menu=file)
main_menu.add_cascade(label="Edit", menu=edit)
main_menu.add_cascade(label="View", menu=view)
main_menu.add_cascade(label="Color Theme", menu=color_theme)

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& End Main Menu $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



################################################### Tool Bar ########################################################################

tool_bar = tk.Label(main_application, background="light blue")
tool_bar.pack(side=tk.TOP, fill=tk.X)

## font combobox
font_tuple = font.families()
font_family = tk.StringVar()
font_family.set("Arial")
font_box = ttk.Combobox(tool_bar, textvariable=font_family, width=30, state='readonly')
font_box.grid(row=0, column=0, padx=5)
font_box['values'] = font_tuple
font_box.current(font_tuple.index(font_family.get()))

## Text size
size_var = tk.IntVar()
size_var.set(12)
font_size = ttk.Combobox(tool_bar, textvariable=size_var, width=15, state='readonly')
font_size.grid(row=0,column=1,padx=5)
font_size['values'] = tuple(range(8,81))
font_size.current(font_size.index(size_var.get()))

## Bold Button
bold_var = tk.StringVar()
bold_var.set('normal')
bold_icon = tk.PhotoImage(file="icons2/bold.png")
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0,column=2, padx=5)

## Italic Button
italic_var = tk.StringVar()
italic_var.set('roman')
italic_icon = tk.PhotoImage(file="icons2/italic.png")
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0,column=3, padx=5)

## Underline Button
underline_var = tk.StringVar()
underline_var.set(0)
underline_icon = tk.PhotoImage(file="icons2/underline.png")
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0,column=4, padx=5)

# Color Button 
font_color_icon = tk.PhotoImage(file="icons2/font_color.png")
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0,column=5, padx=5)

## Align Left Button
align_left_icon = tk.PhotoImage(file="icons2/align_left.png")
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0,column=6, padx=5)

## Align center Button
align_center_icon = tk.PhotoImage(file="icons2/align_center.png")
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0,column=7, padx=5)

## Align right button
align_right_icon = tk.PhotoImage(file="icons2/align_right.png")
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0,column=8, padx=5)

# check_button = tk.Button(tool_bar, text="Check")
# check_button.grid(row=0, column=9)

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& End Tool Bar $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



################################################### Text Editor Window ########################################################################

text_editor = tk.Text(main_application)
scrollbar = tk.Scrollbar(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)
text_editor.focus_set()
scrollbar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scrollbar.set)
scrollbar.pack(fill=tk.Y, side=tk.RIGHT)
text_editor.config(font=(font_family.get(), size_var.get()))
text_editor.pack(fill=BOTH, expand=True)


def change_font_family(event=None):
    Desired_font = tk.font.Font(family = font_family.get(), size = size_var.get(), weight = bold_var.get(), slant=italic_var.get(), underline=underline_var.get())
    text_editor.configure(font=Desired_font)
    

font_box.bind("<<ComboboxSelected>>", change_font_family)


def change_font_size(event=None):
    Desired_font = tk.font.Font(family = font_family.get(), size = size_var.get(), weight = bold_var.get(), slant=italic_var.get(), underline=underline_var.get())
    text_editor.configure(font=Desired_font) 

font_size.bind("<<ComboboxSelected>>", change_font_size)




def check_bold():
    text_property = tk.font.Font(font=text_editor['font']).actual()
    if text_property['weight'] == 'normal':
        bold_var.set('bold')
        Desired_font = tk.font.Font(family = font_family.get(), size = size_var.get(), weight = bold_var.get(), slant=italic_var.get(), underline=underline_var.get())
        text_editor.configure(font=Desired_font)      
    if text_property['weight'] == 'bold':
        bold_var.set('normal')
        Desired_font = tk.font.Font(family = font_family.get(), size = size_var.get(), weight = bold_var.get(), slant=italic_var.get(), underline=underline_var.get())
        text_editor.configure(font=Desired_font)

bold_btn.configure(command=check_bold)


def check_italic():
    text_property = tk.font.Font(font=text_editor['font']).actual()
    if text_property['slant'] == 'roman':
        italic_var.set('italic')
        Desired_font = tk.font.Font(family = font_family.get(), size = size_var.get(), weight = bold_var.get(), slant=italic_var.get(), underline=underline_var.get())
        text_editor.configure(font=Desired_font)
    if text_property['slant'] == 'italic':
        italic_var.set('roman')
        Desired_font = tk.font.Font(family = font_family.get(), size = size_var.get(), weight = bold_var.get(), slant=italic_var.get(), underline=underline_var.get())
        text_editor.configure(font=Desired_font)

italic_btn.configure(command=check_italic)


def check_underline():
    text_property = tk.font.Font(font=text_editor['font']).actual()
    if text_property['underline'] == 0:
        underline_var.set(1)
        Desired_font = tk.font.Font(family = font_family.get(), size = size_var.get(), weight = bold_var.get(), slant=italic_var.get(), underline=underline_var.get())
        text_editor.configure(font=Desired_font)
    if text_property['underline'] == 1:
        underline_var.set(0)
        Desired_font = tk.font.Font(family = font_family.get(), size = size_var.get(), weight = bold_var.get(), slant=italic_var.get(), underline=underline_var.get())
        text_editor.configure(font=Desired_font)

underline_btn.configure(command=check_underline)


def select_font_color():
    color_var = colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_color_btn.configure(command=select_font_color)


####### Alignment Functions  #########

# Left Alignment
def left_align():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command=left_align)


# Center Alignment
def center_align():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=center_align)


# right Alignment
def right_align():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=right_align)






#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& End Text Editor Window $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



################################################### Status Bar ########################################################################

status_bar = ttk.Label(main_application, text="Status Bar")
status_bar.pack(side=tk.BOTTOM)

text_changed = False
def text_modified(event=None):
    global text_changed, url
    if text_editor.edit_modified():
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f'Characters : {characters} words : {words}')
        text_changed = True
        text_editor.edit_modified(False)
        main_application.title(f"Text Editor - {os.path.basename(url)}*")


text_editor.bind("<<Modified>>", text_modified)

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& End Status Bar $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$




show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)



def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(expand=True, fill=tk.BOTH)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True

view.add_checkbutton(label="Tool Bar", image=tool_bar_icon, compound=tk.LEFT, onvalue=True, offvalue=False, variable=show_toolbar, command=hide_toolbar)
view.add_checkbutton(label="Status Bar", image=status_bar_icon, compound=tk.LEFT, onvalue=True, offvalue=False, variable=show_statusbar, command=hide_statusbar)




################################################### Main Menu Functionality ########################################################################
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& End Main Menu Functionality $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


main_application.config(menu=main_menu)

################ shortcut binding

main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-Alt-s>", save_as_file)

main_application.mainloop()