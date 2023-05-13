from controller import *

def main():
    window = Tk()
    window.title("Lab 10")
    window.geometry('700x600')
    window.resizable(False, False)
    GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()