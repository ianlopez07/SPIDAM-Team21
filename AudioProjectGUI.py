import tkinter as tk
from tkinter import filedialog

class AudioGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Converting / Modeling")

        self.root.geometry("500x400")

        self.create_widgets()

    def create_widgets(self):
        # Create a label
        self.labeltitle = tk.Label(self.root, text="WIP GUI (Bound to change over course of project)")
        self.labeltitle.pack(pady=10, padx=20, anchor="w")

        tk.Label(self.root, text="").pack() #These are just to make extra spaces between the labels and buttons on the GUI

        self.label1 = tk.Label(self.root, text="No file selected")
        self.label1.pack(pady=10, padx=20, anchor="w")

        # Create a button to open an audio file
        self.open_button1 = tk.Button(self.root, text="Open Audio File", command=self.open_audio_file)
        self.open_button1.pack(pady=5, padx=20, anchor="w")

        tk.Label(self.root, text="").pack()

        self.label2 = tk.Label(self.root, text="Clean")
        self.label2.pack(pady=10, padx=20, anchor="w")

        self.open_button2 = tk.Button(self.root, text="Clean File")
        self.open_button2.pack(pady=0, padx=20, anchor="w")

        tk.Label(self.root, text="").pack()

        self.label3 = tk.Label(self.root, text="Convert File to .Wav")
        self.label3.pack(pady=10, padx=20, anchor="w")

        self.open_button3 = tk.Button(self.root, text="Convert")
        self.open_button3.pack(pady=0, padx=20, anchor="w")

    def open_audio_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if file_path:
            self.label1.config(text=f"Selected file: {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioGUI(root)
    root.mainloop()
