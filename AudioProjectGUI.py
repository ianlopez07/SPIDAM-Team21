import tkinter as tk
from tkinter import filedialog
from file_computation import File_Comp
from file_handling import File_Handling
from Plotting import Plot
import wave

class AudioGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Converting / Modeling")

        self.root.geometry("500x450")

        self.create_widgets()

    def create_widgets(self):
        # Create a label
        self.labeltitle = tk.Label(self.root, text="AUDIO CONVERTING AND MODELING GUI")
        self.labeltitle.pack(pady=10, padx=20, anchor="w")

        tk.Label(self.root,text="").pack()  # These are just to make extra spaces between the labels and buttons on the GUI

        # LABEL AND BUTTON FOR SELECTING THE FILE
        self.label1 = tk.Label(self.root, text="No file selected")
        self.label1.pack(pady=10, padx=20, anchor="w")

        # Create a button to open an audio file
        self.open_button1 = tk.Button(self.root, text="Open Audio File", command=self.open_audio_file)
        self.open_button1.pack(pady=5, padx=20, anchor="w")

        tk.Label(self.root, text="").pack()

        # LABEL AND BUTTON TO DISPLAY THE .WAV FILE
        self.label2 = tk.Label(self.root, text="Display the waveform")
        self.label2.pack(pady=10, padx=20, anchor="w")

        self.button2 = tk.Button(self.root, text="Display", command=self.display_waveform)
        self.button2.pack(pady=0, padx=20, anchor="w")

        tk.Label(self.root, text="").pack()

        # LABEL AND BUTTON FOR THE GRAPH AND PLOTS
        self.label3 = tk.Label(self.root, text="Display Graphing and Plotting")
        self.label3.pack(pady=10, padx=20, anchor="w")

        self.button3 = tk.Button(self.root, text="Display Graph & Plots", command=self.display_graphs_and_plots)
        self.button3.pack(pady=0, padx=20, anchor="w")

        tk.Label(self.root, text="").pack()

        # LABEL AND BUTTON TO DISPLAY THE .WAV FILE
        self.label4 = tk.Label(self.root, text="Combine the plots")
        self.label4.pack(pady=10, padx=20, anchor="w")

        self.button4 = tk.Button(self.root, text="Combine", command=self.display_all_reverb)
        self.button4.pack(pady=0, padx=20, anchor="w")
    def open_audio_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if file_path:
            self.label1.config(text=f"Selected file: {file_path}")
        handle = File_Handling(file_path)

    def display_waveform(self):
        file_comp = File_Comp(File_Handling(self.label1.cget("text").replace("Selected File: ", "")))
        file_comp.wave_file()

    def display_graphs_and_plots(self):
        plotter = Plot(self.label1.cget("text").replace("Selected file: ", ""))
        plotter.display_graphs_and_plots()

    def display_all_reverb(self):
        plotter = Plot(self.label1.cget("text").replace("Selected file: ", ""))
        plotter.reverb_high()
        plotter.reverb_mid()
        plotter.reverb_low()

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioGUI(root)
    root.mainloop()
