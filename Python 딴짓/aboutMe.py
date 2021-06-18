from tkinter import *
from tkinter import messagebox
import tkinter.font as font

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt # 데이터 시각화(키 표현)

# 상단 File > Exit 
def clickExit():
    root.quit()
    root.destroy()

# 사진 마우스 왼쪽 버튼 클릭 이벤트
def onClickLeftImage(event):
    global imageNum
    messagebox.showinfo("사진 설명", imageMessageList[imageNum])

# 다음 사진 보기(다음 버튼 클릭 이벤트)
def clickImageNext():
    global imageNum
    imageNum += 1
    if imageNum > 2:
        imageNum = 0
    photo = PhotoImage(file=imageFileList[imageNum])
    photoLabel.config(image=photo)
    photoLabel.image = photo

# 이전 사진 보기(이전 버튼 클릭 이벤트)
def clickImagePrev():
    global imageNum
    imageNum -= 1
    if imageNum < 0:
        imageNum = 2
    photo = PhotoImage(file=imageFileList[imageNum])
    photoLabel.config(image=photo)
    photoLabel.image = photo

root = Tk()
root.wm_title("aboutMe(최서연)") # window 타이틀 지정

# 닫기 버튼 생성
mainMenu = Menu(root)
root.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Exit", command=clickExit)

# 그래프용 데이터
myGrowHeight = [120, 140, 150, 158, 164] # 키 데이터
myGrowWeight = [20, 30, 35, 44, 48] # 몸무게 데이터
myGrowAge = [5, 10, 13, 16, 26] # 나이 데이터

# 이미지용 데이터
imageNum = 0
imageFileList = ['myImage.png', 'myImage2.png', 'myImage3.png']
imageMessageList = ['이건 5살때 입니다.', '이 사진은 10살때 입니다.', '이 사진은 고등학교 졸업식입니다.']

# 인적사항 데이터
myInfo = "[ 기본 인적 사항 ]\n- 이름: 최서연\n- 사번: 1745061\n- 이메일: itsfortheseoyoung@gmail.com"
myFont = font.Font(family='Helvetica', size=15, weight='bold')

# Frame 생성
imageFrame = Frame(root, padx=5, pady=5)
imageFrame.grid(row=1, column=0)

infoFrame = Frame(root, padx = 5, pady = 5)
infoFrame.grid(row=0, column=0)

graphFrame = Frame(root)
graphFrame.grid(row=2, column=0)

# 기본 인적사항 
info = Message(infoFrame, text = myInfo, width=500, font=myFont)
info.config(bg='lightblue')
info.pack()

# Button 생성
btnPrev = Button(imageFrame, text="<< 이전", command=clickImagePrev)
btnNext = Button(imageFrame, text="다음 >>", command=clickImageNext)

# Button 위치 지정
btnPrev.place(x=0, y=0) 
btnNext.place(x=250, y=0)

# 사진 상단 글씨 데이터
imageNameLabel = Label(imageFrame, text="My Picture(사진을 클릭해주세요!)")
imageNameLabel.place(x=330, y=10)
imageNameLabel.pack()

# 사진 데이터
photo = PhotoImage(file=imageFileList[0])
photoLabel = Label(imageFrame, image=photo, width=300, height=200)
photoLabel.place(x=20, y=130)
photoLabel.pack(expand=False)
photoLabel.bind('<Button-1>', onClickLeftImage)
#img=PhotoImage(file="myImage.png")
#imageLabel=Label(imageFrame, image=img)
#imageLabel.pack()
#imageLabel.bind('<Button-1>', onClickLeftImage)

# 키 그래프 만들기
fig = plt.figure(figsize = (10, 5), dpi = 100)
#ax = fig.add_subplot(111)
# subplot의 첫번째 수는 열의 개수, 두번째 수는 행의 개수, 마지막 숫자는 몇 번째 자리인지 의미함
ax_myHeight = plt.subplot(121, xlim=(0,30), ylim=(0, 170))
#ax.plot(myGrowAge, myGrowHeight)
ax_myHeight.set_xlabel('Age')
ax_myHeight.set_ylabel('Height(cm)')
ax_myHeight.set_title('My Height')
ax_myWeight = plt.subplot(122, xlim=(0,30), ylim=(0,60))
ax_myWeight.set_xlabel('Age')
ax_myWeight.set_ylabel('Weight(kg)')
ax_myWeight.set_title('My Weight')

myHeight = ax_myHeight.plot(myGrowAge, myGrowHeight)
myWeight = ax_myWeight.plot(myGrowAge, myGrowWeight)

#graphLabel = Label(graphFrame, text="My Growth").grid(column=0, row=0)
canvas = FigureCanvasTkAgg(fig, master=graphFrame)
canvas.get_tk_widget().grid(column=0,row=1)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, graphFrame)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

root.mainloop()
