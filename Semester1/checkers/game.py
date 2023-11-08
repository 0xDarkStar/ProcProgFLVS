# Make a checkers game
from tkinter import *
from tkinter import ttk

# Made by: 0xDarkStar

# My own work:
whiteKingDic = {}
whiteQueenDic = {}
whiteKnightDic = {}
whiteBishopDic = {}
whiteRookDic = {}
whitePawnDic = {}
blackKingDic = {}
blackQueenDic = {}
blackKnightDic = {}
blackBishopDic = {}
blackRookDic = {}
blackPawnDic = {}

global deleteMode
deleteMode = False

def main():
    global root
    root = Tk()
    frm = Frame(master=root, padx=20, pady=20)
    frm.pack(side=RIGHT)
    checkerBoard = Label(master=frm, 
text=
"""\u250F\u2501\u2501\u2501\u2533\u2501\u2501\u2501\u2533\u2501\u2501\u2501\u2533\u2501\u2501\u2501\u2533\u2501\u2501\u2501\u2533\u2501\u2501\u2501\u2533\u2501\u2501\u2501\u2533\u2501\u2501\u2501\u2513
        \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503        
\u2523\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u252B
 \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503 
\u2523\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u252B
 \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503 
\u2523\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u252B
 \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503 
\u2523\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u252B
 \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503 
\u2523\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u252B
 \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503 
\u2523\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u252B
 \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503 
\u2523\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u252B
 \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503      \u2503 
\u2517\u2501\u2501\u2501\u253B\u2501\u2501\u2501\u253B\u2501\u2501\u2501\u253B\u2501\u2501\u2501\u253B\u2501\u2501\u2501\u253B\u2501\u2501\u2501\u253B\u2501\u2501\u2501\u253B\u2501\u2501\u2501\u251B""")
    checkerBoard.pack(side=RIGHT)
    # Make all the chess pieces for the user to use
    buttonFrame = Frame(root)
    wKingButton = Button(buttonFrame, text="Make white King", command=lambda: chessPieces("white king"))
    wKingButton.grid(row=0, column=0)
    wQueenButton = Button(buttonFrame, text="Make white Queen", command=lambda: chessPieces("white queen"))
    wQueenButton.grid(row=1, column=0)
    wKnightButton = Button(buttonFrame, text="Make white Knight", command=lambda: chessPieces("white knight"))
    wKnightButton.grid(row=2, column=0)
    wBishopButton = Button(buttonFrame, text="Make white Bishop", command=lambda: chessPieces("white bishop"))
    wBishopButton.grid(row=3, column=0)
    wRookButton = Button(buttonFrame, text="Make white Rook", command=lambda: chessPieces("white rook"))
    wRookButton.grid(row=4, column=0)
    wPawnButton = Button(buttonFrame, text="Make white Pawn", command=lambda: chessPieces("white pawn"))
    wPawnButton.grid(row=5, column=0)
    bKingButton = Button(buttonFrame, text="Make black King", command=lambda: chessPieces("black king"))
    bKingButton.grid(row=0, column=1)
    bQueenButton = Button(buttonFrame, text="Make black Queen", command=lambda: chessPieces("black queen"))
    bQueenButton.grid(row=1, column=1)
    bKnightButton = Button(buttonFrame, text="Make black Knight", command=lambda: chessPieces("black knight"))
    bKnightButton.grid(row=2, column=1)
    bBishopButton = Button(buttonFrame, text="Make black Bishop", command=lambda: chessPieces("black bishop"))
    bBishopButton.grid(row=3, column=1)
    bRookButton = Button(buttonFrame, text="Make black Rook", command=lambda: chessPieces("black rook"))
    bRookButton.grid(row=4, column=1)
    bPawnButton = Button(buttonFrame, text="Make black Pawn", command=lambda: chessPieces("black pawn"))
    bPawnButton.grid(row=5, column=1)
    buttonFrame.pack(side=LEFT)
    deleteButton = Button(root, text="Delete piece", command=lambda: toggleDelete(deleteButton))
    deleteButton.pack(side=BOTTOM)
    root.mainloop()

def toggleDelete(widget):
    global deleteMode
    if deleteMode == False:
        if isinstance(widget, Button):
            root.configure(cursor="target")
            deleteMode = True
    elif deleteMode == True:
        widget.destroy()
        root.configure(cursor="arrow")
        deleteMode = False

def chessPieces(piece):
    match piece:
        case "white king":
            pieceCount = list(whiteKingDic.keys())
            if len(pieceCount) == 0:
                whiteKingDic[0] = Label(master=root, text='\u2654')
                whiteKingDic[0].pack()
                make_draggable(whiteKingDic[0])
            else:
                pieces = (pieceCount[-1]+1)
                whiteKingDic[pieces] = Label(master=root, text='\u2654')
                whiteKingDic[pieces].pack()
                make_draggable(whiteKingDic[pieces])
        case "white queen":
            pieceCount = list(whiteQueenDic.keys())
            if len(pieceCount) == 0:
                whiteQueenDic[0] = Label(master=root, text='\u2655')
                whiteQueenDic[0].pack()
                make_draggable(whiteQueenDic[0])
            else:
                pieces = (pieceCount[-1]+1)
                whiteQueenDic[pieces] = Label(master=root, text='\u2655')
                whiteQueenDic[pieces].pack()
                make_draggable(whiteQueenDic[pieces])
        case "white knight":
            pieceCount = list(whiteKnightDic.keys())
            if len(pieceCount) == 0:
                whiteKnightDic[0] = Label(master=root, text='\u2658')
                whiteKnightDic[0].pack()
                make_draggable(whiteKnightDic[0])
            else:
                pieces = (pieceCount[-1]+1)
                whiteKnightDic[pieces] = Label(master=root, text='\u2658')
                whiteKnightDic[pieces].pack()
                make_draggable(whiteKnightDic[pieces])
        case "white bishop":
            pieceCount = list(whiteBishopDic.keys())
            if len(pieceCount) == 0:
                whiteBishopDic[0] = Label(master=root, text='\u2657')
                whiteBishopDic[0].pack()
                make_draggable(whiteBishopDic[0])
            else:
                pieces = (pieceCount[-1]+1)
                whiteBishopDic[pieces] = Label(master=root, text='\u2657')
                whiteBishopDic[pieces].pack()
                make_draggable(whiteBishopDic[pieces])
        case "white rook":
            pieceCount = list(whiteRookDic.keys())
            if len(pieceCount) == 0:
                whiteRookDic[0] = Label(master=root, text='\u2656')
                whiteRookDic[0].pack()
                make_draggable(whiteRookDic[0])
            else:
                pieces = (pieceCount[-1]+1)
                whiteRookDic[pieces] = Label(master=root, text='\u2656')
                whiteRookDic[pieces].pack()
                make_draggable(whiteRookDic[pieces])
        case "white pawn":
            pieceCount = list(whitePawnDic.keys())
            if len(pieceCount) == 0:
                whitePawnDic[0] = Label(master=root, text='\u2659')
                whitePawnDic[0].pack()
                make_draggable(whitePawnDic[0])
            else:
                pieces = (pieceCount[-1]+1)
                whitePawnDic[pieces] = Label(master=root, text='\u2659')
                whitePawnDic[pieces].pack()
                make_draggable(whitePawnDic[pieces])
        case "black king":
            pieceCount = list(blackKingDic.keys())
            if len(pieceCount) == 0:
                blackKingDic[0] = Label(master=root, text='\u265A')
                blackKingDic[0].pack()
                make_draggable(blackKingDic[0])
            else:
                pieces = (pieceCount[-1]+1)
                blackKingDic[pieces] = Label(master=root, text='\u265A')
                blackKingDic[pieces].pack()
                make_draggable(blackKingDic[pieces])
        case "black queen":
            pieceCount = list(blackQueenDic.keys())
            if len(pieceCount) == 0:
                blackQueenDic[0] = Label(master=root, text='\u265B')
                blackQueenDic[0].pack()
                make_draggable(blackQueenDic[0])
            else:
                pieces = (pieceCount[-1]+1)
                blackQueenDic[pieces] = Label(master=root, text='\u265B')
                blackQueenDic[pieces].pack()
                make_draggable(blackQueenDic[pieces])
        case "black knight":
            pieceCount = list(blackKnightDic.keys())
            if len(pieceCount) == 0:
                blackKnightDic[0] = Label(master=root, text='\u265E')
                blackKnightDic[0].pack()
                make_draggable(blackKnightDic[0])
            else:
                pieces = (pieceCount[-1]+1)
                blackKnightDic[pieces] = Label(master=root, text='\u265E')
                blackKnightDic[pieces].pack()
                make_draggable(blackKnightDic[pieces])
        case "black bishop":
            pieceCount = list(blackBishopDic.keys())
            if len(pieceCount) == 0:
                blackBishopDic[0] = Label(master=root, text='\u265D')
                blackBishopDic[0].pack()
                make_draggable(blackBishopDic[0])
            else:
                pieces = (pieceCount[-1]+1)
                blackBishopDic[pieces] = Label(master=root, text='\u265D')
                blackBishopDic[pieces].pack()
                make_draggable(blackBishopDic[pieces])
        case "black rook":
            pieceCount = list(blackRookDic.keys())
            if len(pieceCount) == 0:
                blackRookDic[0] = Label(master=root, text='\u265C')
                blackRookDic[0].pack()
                make_draggable(blackRookDic[0])
            else:
                pieces = (pieceCount[-1]+1)
                blackRookDic[pieces] = Label(master=root, text='\u265C')
                blackRookDic[pieces].pack()
                make_draggable(blackRookDic[pieces])
        case "black pawn":
            pieceCount = list(blackPawnDic.keys())
            if len(pieceCount) == 0:
                blackPawnDic[0] = Label(master=root, text='\u265F')
                blackPawnDic[0].pack()
                make_draggable(blackPawnDic[0])
            else:
                pieces = (pieceCount[-1]+1)
                blackPawnDic[pieces] = Label(master=root, text='\u265F')
                blackPawnDic[pieces].pack()
                make_draggable(blackPawnDic[pieces])



# These three functions are from an answer on this page:
# https://stackoverflow.com/questions/37280004/tkinter-how-to-drag-and-drop-widgets
def make_draggable(widget: Label):
    def handle(event):
        toggleDelete(widget)
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)
    widget.bind("<ButtonRelease-1>", handle)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)

main()


# , command=root.destroy
    # image1 = Image.open("/home/uuhhhhhh/Pictures/hand.png")
    # image1 = image1.resize((200,125), Image.ANTIALIAS)
    # test = ImageTk.PhotoImage(image1)
    # imageLabel = Label(master=frm, image=test)
    # imageLabel.grid(row=5, column=5)
    # make_draggable(imageLabel)