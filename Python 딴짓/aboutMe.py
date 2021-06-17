from tkinter import *
from tkinter import messagebox

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt # 데이터 시각화(키 표현)

def clickExit():
    root.quit()
    root.destroy()

def onClickLeftImage(event):
    messagebox.showinfo("My Info", "이름: 최서영\n사번: 1745061\n")

root = Tk()
root.wm_title("aboutMe")

# 닫기 버튼 생성
mainMenu = Menu(root)
root.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Exit", command=clickExit)

# 그래프용 데이터
myGrowHeight = [120, 140, 150, 158, 164]
myGrowAge = [5, 10, 13, 16, 26]
# 사진 상단 글씨 데이터
imageNameLabel = Label(root, text="My Picture")
imageNameLabel.pack()
# 사진 데이터
img=PhotoImage(file="myImage.png")
imageLabel=Label(root, image=img)
imageLabel.pack()
imageLabel.bind('<Button-1>', onClickLeftImage)

#fig = Figure(figsize=(5, 4), dpi=100)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(myGrowAge, myGrowHeight)
ax.set_xlabel('Age')
ax.set_ylabel('Height(cm)')
ax.set_title('My Height')

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

root.mainloop()
