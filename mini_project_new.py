from tkinter import *
from tkinter import filedialog
import wave, struct
from pygame import mixer
import numpy as np

global string3
string3=[]
global string1
string1=[]
global string2
string2=[]
global string_text
string_text=[]
global string_result
string_result=[]
global quote
quote=[]
global flag
flag=[]

    
def play_(string11):
        mixer.init()
        mixer.music.load(string11)
        mixer.music.play()
    
def stop_():
        mixer.music.stop()
        
class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        #Setup Menu
        MainMenu(self)
        #Setup Frame
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.title('mini project  b.tech eie  sastra university')
        

        for F in (preStart,StartPage_decryption,StartPage_e, encrypt):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(preStart)    
    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()

class preStart(Frame):                  
    def __init__(self, parent, controller):
                Frame.__init__(self, parent)
                label = Label(self, text="AUDIO  BASED  STEGANOGRAPHY  CALCULATOR :",font=("Segoe UI", 15),bg='#000',fg='white').place(x = 150, y = 50)
                Button(self, text='                          Quit                         ',font=("Segoe UI", 19),borderwidth=3, relief=RIDGE, command=lambda:controller.destroy()).place(x = 160, y =325)
                page_one = Button(self, text="           proceed to encryption           ",font=("Segoe UI", 19),borderwidth=3, relief=RIDGE, command=lambda:controller.show_frame(StartPage_e))
                page_one.place(x = 160, y = 125)
                page_two = Button(self, text="           proceed to decryption           ",font=("Segoe UI", 19),borderwidth=3, relief=RIDGE, command=lambda:controller.show_frame(StartPage_decryption))
                page_two.place(x = 160, y = 225)


class StartPage_decryption(Frame):                  
    def __init__(self, parent, controller):
                Frame.__init__(self, parent)
                def hello_RAMU():
                    fil_1=filedialog.askopenfile()
                    Label(self,text=fil_1.name,font=("Segoe UI", 10),borderwidth=3,relief=FLAT,wraplength=235).place(x=350,y=125)
                    
                    string2.clear()
                    string2.append(fil_1.name)            
                label = Label(self, text="-------------------decryption page------------------",font=("Segoe UI", 15),bg='#000',fg='white').place(x = 150, y = 50)
                
                q1=Button(self, text=" SELECT AUDIO FILE     : ",font=("Segoe UI", 11),borderwidth=3,relief=RIDGE,command =hello_RAMU)
                q1.place(x=150,y=130)
                

                def PRINT_OUTPUT():
                        decryp_T()
                        textBox.insert(END,quote[0]);
                    
                    
                
                textBox=Text(self, height=5, width=55)
                textBox.place(x=150,y=220)
                
                                
                Button(self, text='        QUIT       ',font=("Segoe UI", 13),borderwidth=3, relief=RIDGE, command=lambda:controller.destroy()).place(x = 150, y =360)
                page_ONE = Button(self, text="        DECRYPT        ",font=("Segoe UI", 13),borderwidth=3, relief=RIDGE, command=PRINT_OUTPUT)
                page_TWO = Button(self, text="     BACK     ",font=("Segoe UI", 13),borderwidth=3, relief=RIDGE, command=lambda:controller.show_frame(preStart))
                page_ONE.place(x = 300, y = 360)
                page_TWO.place(x = 485, y = 360)
5

class StartPage_e(Frame):                  
    def __init__(self, parent, controller):
                Frame.__init__(self, parent)

                def hello():
                    fil=filedialog.askopenfile()
                    Label(self,text=fil.name,font=("Segoe UI", 10),borderwidth=3,relief=FLAT,wraplength=235).place(x=350,y=125)
                    
                    string1.clear()
                    string1.append(fil.name)            
                label = Label(self, text="-------------------Encryption page------------------",font=("Segoe UI", 15),bg='#000',fg='white').place(x = 150, y = 50)
                
                q=Button(self, text=" SELECT AUDIO FILE     : ",font=("Segoe UI", 11),borderwidth=3,relief=RIDGE,command =hello)
                q.place(x=150,y=130)
                q=Button(self, text=" SELECT FILE NAME      : ",font=("Segoe UI", 11),borderwidth=3,relief=RIDGE,command =hello)
                q.place(x=150,y=310)
                #q.bind('<Button-1>', hello)

                def retrieve_input():
                    inputValue=textBox.get("1.0","end-1c")
                    string_text.append(inputValue)
                    inputValue=textBox1.get("1.0","end-1c")
                    string3.append(inputValue)
                    string3[0]+='.wav'

                textBox1=Text(self, height=2, width=30)
                textBox1.place(x=350,y=310)                    
                
                textBox=Text(self, height=5, width=30)
                textBox.place(x=350,y=200)
                Button(self, text=" ENTER THE MESSAGE : ",font=("Segoe UI", 11),borderwidth=3,relief=RIDGE,command=retrieve_input).place(x = 150, y = 200)
                                
                Button(self, text='           QUIT           ',font=("Segoe UI", 13),borderwidth=3, relief=RIDGE, command=lambda:controller.destroy()).place(x = 150, y =400)
                page_one = Button(self, text="        ENCRYPT       ",font=("Segoe UI", 13),borderwidth=3, relief=RIDGE, command=lambda:controller.show_frame(encrypt))
                
                page_one.place(x = 340, y = 400)
                page_TWO = Button(self, text=" BACK ",font=("Segoe UI", 13),borderwidth=3, relief=RIDGE, command=lambda:controller.show_frame(preStart))
                page_TWO.place(x = 525, y = 400)
  
def encryp_T():
    waveFile = wave.open(string1[0], 'r')
    file = open("binary_data.txt","w+")


    length = waveFile.getnframes()
    for i in range(0,length):
        waveData = waveFile.readframes(1)
        data = struct.unpack("<h", waveData)
        file.write(bin(data[0]))
        file.write("\n")


    file = open("binary_data.txt", "r") 
    lst = file.readlines() 

    lst2=[]
    for number in lst:
        newstr2=number.replace("\n","")
        lst2.append(newstr2)
    lst2 = [i.replace("'", "") for i in lst2]
    print("input sequence")
    print(lst2)

    
    name = string_text[0]
    ord_list=[]
    bit_list=[]
    for char_name in name :
        ord_name = ord(char_name)+2
        ord_name_b =bin(ord_name)
        ord_name_b_wb = ord_name_b.replace("b","")
        ord_list.append(ord_name_b_wb)

    print("data in binary form")
    print(ord_list)

    for var_list in ord_list :
        for bit in var_list :
            bit_list.append(bit)

    for i in range(len(lst2)-len(bit_list)) :
        bit_list.append(0)

    print("encoded data is:")
    print(bit_list)
    init_encrypt_2=[]


    print("encrypting..............")
    for i in range(len(lst2)):
        if bit_list[i]=='1':
            if int(lst2[i],2)%2 ==1:
                a=int(lst2[i],2);
            else :
                a=int(lst2[i],2)-1;
        else :
            if int(lst2[i],2)%2 ==1:
                a=int(lst2[i],2)-1;
            else :
                a=int(lst2[i],2);
        init_encrypt_2.append(a)
    print("output sequence")
    print(init_encrypt_2)
    wavef = wave.open(string3[0],'w')
    wavef.setnchannels(waveFile.getnchannels())
    wavef.setsampwidth(waveFile.getsampwidth())
    wavef.setframerate(waveFile.getframerate())
    for i in init_encrypt_2:
        data__ = struct.pack('<h',i)
        wavef.writeframesraw( data__)
    wavef.close()
    file.close()
    waveFile.close()
    print("success")
    flag.clear()
    flag.append(1)
        
def decryp_T():
        waveFile = wave.open(string2[0], 'r')
        length1 = waveFile.getnframes()
        decrypt_me=np.zeros(length1).tolist()
        print(len(decrypt_me))
        j=0
        for i in range(0,length1):
                waveData = waveFile.readframes(1)
                data = struct.unpack("<h", waveData)
                if data[0]%2==1 :
                        decrypt_me[j]=1
                        j=j+1
                else :
                        decrypt_me[j]=0
                        j=j+1
        print(decrypt_me)
        x= len(decrypt_me)
        if x%8==0 :
                y=int(x/8)
        else :
                y=int((x/8)+1)

        z=(8*y)-x
        print(x)
        print(y)
        print(z)
        decrypt_me_=np.array(decrypt_me)
        decrypt_me_=np.append(decrypt_me_,np.zeros(z))

        decrypt_me_=decrypt_me_.reshape(y,8)
        print(decrypt_me_)
        decrypt_me_2=np.zeros(y).tolist()
        for i in range(0,y) :
                for j in range(0,8) :
                        decrypt_me_2[i]=decrypt_me_2[i]+(decrypt_me_[i][j]*(2**(7-j)))
                        decrypt_me_2[i]=int(decrypt_me_2[i])

        print(decrypt_me_2)

        for i in range(0,y) :
                decrypt_me_2[i]=chr(decrypt_me_2[i])

        t=0
        T=''
        U=''
        while(decrypt_me_2[t]!='\x00'):
                T+=(decrypt_me_2[t])
                t+=1
        for l in range(0,len(T)):
                temp=0
                temp=ord(T[l])
                temp-=2
                U+=chr(temp)
        quote.append(U)
        
        
        
class encrypt(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        def check():
                if(len(flag)==1): 
                        Label(self, text="encryption SUCCESS             ",font=("Segoe UI", 15)).place(x = 150, y = 270)
                        btn = Button(self, text="Play original file",font=("Segoe UI", 13),borderwidth=3,relief=RIDGE,command = lambda:  play_(string1[0])).place(x = 150, y = 120)
                        btn = Button(self, text="Play encrypted file",font=("Segoe UI", 13),borderwidth=3,relief=RIDGE,command = lambda:  play_(string3[0])).place(x = 150, y = 200)
                        Button(self, text="stop playing original file",font=("Segoe UI", 13),borderwidth=3,relief=RIDGE,command = stop_).place(x = 290, y = 120)
                        Button(self, text="stop playing encrypted file",font=("Segoe UI", 13),borderwidth=3,relief=RIDGE,command = stop_).place(x = 310, y = 200)

                else:
                        Label(self, text="↓↓↓ please begin encryption ",font=("Segoe UI", 15)).place(x = 150, y = 270)


        Button(self, text="BEGIN ENCRYPTION",font=("Segoe UI", 13),borderwidth=3,relief=RIDGE,command=encryp_T).place(x = 150, y = 360)
        Button(self, text="REFRESH",font=("Segoe UI", 13),borderwidth=3,relief=RIDGE,command=check).place(x = 400, y = 360)
        label = Label(self, text="----------------Encryption result-----------------",font=("Segoe UI", 15),bg='#000',fg='white').place(x = 150, y = 50)
        Button(self, text='QUIT',font=("Segoe UI", 13),borderwidth=3, relief=RIDGE, command=lambda:controller.destroy()).place(x = 335, y =360)
        start_page = Button(self, text=" BACK ",font=("Segoe UI", 13),borderwidth=3, relief=RIDGE, command=lambda:controller.show_frame(StartPage_e)).place(x = 490, y = 360)


class MainMenu:
    def __init__(self, master):
        master.iconbitmap('sastra.ico')
        master.geometry("760x480+100+100")
        
   
        
        

app = App()
app.mainloop()
