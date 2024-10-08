import sys
import os
import threading

if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    import Tkinter as tk
else:
    import tkinter as tk

from flask import Flask

print(f"DISPLAY: !{os.environ.get('DISPLAY')}!")
#if os.environ.get('DISPLAY','') == '':
#    print('no display found. Using :0.0')
#    os.environ.__setitem__('DISPLAY', ':0.0')
#print(f"DISPLAY: !{os.environ.get('DISPLAY')}!")

app = Flask(__name__)

root = tk.Tk()
root.geometry('800x400')

#frame
frameCnt = 2
#frames = [PhotoImage(file='/home/poppy/image_view/eyes1.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
labelText = tk.StringVar()

def update(ind):
    #frame = frames[ind]
    labelText.set("Hello\n안녕1\n23")
    #label.configure(image=frame)
    #root.after(100, update, ind)

# fullscreen
# F11: fullscreen toggle, Esc : exit fullscreen mode
root.attributes("-fullscreen", True)
#root.bind("<F11>", lambda event: root.attributes("-fullscreen",
#                                    not root.attributes("-fullscreen")))
#root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

#window center position
positionRight = root.winfo_screenwidth()/2
positionDown = root.winfo_screenheight()/2
print(positionRight, positionDown)
#set image
#label = tk.Label(root, text="Hello", bg='black', fg="white", font="arial 25 bold", width=200)
label = tk.Label(root, textvariable=labelText, bg='black', fg="white", font="NanumGothic 55 bold")
# label.place(x=200,y=300,anchor=tk.CENTER)
label.place(relx = 0.5, rely = 0.5, anchor = 'center')
# label.pack(padx=20, pady=160)
root.after(0, update, 0)

#background color
root.configure(bg='black')

btnClose = tk.Button(root, text="Close", command=root.destroy)
btnClose.place(relx = 0.5, rely = 0.95, anchor = 'center')
# btnClose.pack()



def flask_main():
    app.run(debug=False, host="0.0.0.0", port=5000)


@app.route("/")
def hello_world():
    return "Hello, World@!"

@app.route("/msg/<msg>")
def display_msg(msg):
    labelText.set(msg)
    return f"Display message: {msg}"


if __name__ == "__main__":
    flask_thread = threading.Thread(target=flask_main)
    flask_thread.daemon = True
    flask_thread.start()
    root.mainloop()

