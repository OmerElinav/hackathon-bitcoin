from create_wallet import create_wallet
from Tkinter import Tk, Button, END, Text
import tkFileDialog

root = Tk()
root.geometry("1500x400")


def update_values():
    seed, spend, view, addr = create_wallet()
    seed_e.insert(END, seed)
    spend_e.insert(END, spend)
    view_e.insert(END, view)
    addr_e.insert(END, addr)


def choose_dir():
    return tkFileDialog.askdirectory(title="Choose root directory for website files")


print_button = Button(root, text='Create Wallet', command=update_values)
print_button.pack()
dir_button = Button(root, text='Add miner to website pages', command=choose_dir)
dir_button.pack()
seed_e = Text(root, height=2, width=200)
seed_e.insert(END, 'secret seed: ')
seed_e.pack()
spend_e = Text(root, height=2, width=200)
spend_e.insert(END, 'secret spend key: ')
spend_e.pack()
view_e = Text(root, height=2, width=200)
view_e.insert(END, 'secret view key: ')
view_e.pack()
addr_e = Text(root, height=2, width=200)
addr_e.insert(END, 'public address: ')
addr_e.pack()
root.mainloop()
