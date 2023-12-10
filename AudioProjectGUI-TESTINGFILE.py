import tkinter as tk
from tkinter import filedialog

import Plotting
from file_computation import File_Comp
from file_handling import File_Handling
from Plotting import Plot, wave_form

class AudioGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Converting / Modeling")

        self.root.geometry("600x600")

        self.create_widgets()

    def create_widgets(self):
        # Create a label
        self.labeltitle = tk.Label(self.root, text="AUDIO CONVERTING AND MODELING GUI")
        self.labeltitle.pack(pady=10, padx=20, anchor="w")

        tk.Label(self.root,text="").pack()  #These are just to make extra spaces between the labels and buttons on the GUI

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

        tk.Label(self.root, text="").pack()

        # LABEL AND BUTTON FOR FILE COMPUTATION INFO
        self.label5= tk.Label(self.root, text="Compute File Info")
        self.label5.pack(pady=10, padx=20, anchor="w")

        self.button5 = tk.Button(self.root, text="Compute File Info", command=self.compute_file_info)
        self.button5.pack(pady=0, padx=20, anchor="w")

        # LABEL AND BUTTON TO DISPLAY THE COMBINED PLOT STRING
        self.label6 = tk.Label(self.root, text="Combined Reverb Plot:")
        self.label6.pack(pady=10, padx=20, anchor="w")

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=5, padx=20, anchor="w")

    def open_audio_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.m4a;*.mp3;*.wav")])
        if file_path:
            self.label1.config(text=f"Selected file: {file_path}")
            self.handle = File_Handling(file_path)
            self.compute_file_info()

    def display_waveform(self):
        if hasattr(self, 'handle'):
            Plotting.wave_form(self.handle.wav_filename)
        else:
            print("No file selected.")

    def display_graphs_and_plots(self):
        if hasattr(self, 'handle'):
            plotter = Plot(self.handle.wav_filename)
            plotter.reverb_high()
            plotter.reverb_mid()
            plotter.reverb_low()
        else:
            print("No file selected.")

    def compute_file_info(self):
        if hasattr(self, 'handle'):
            file_comp = File_Comp(self.handle.wav_filename)
            time_info = file_comp.return_time()
            resonance_info = file_comp.high_resonance()
            self.label5.config(text=f"File Length: {time_info} seconds\nResonance Info: {resonance_info}")
        else:
            print("No file selected.")

    def display_all_reverb(self):
        if hasattr(self, 'handle'):
            plotter = Plot(self.handle.wav_filename)
            result_string = plotter.reverb_combine()
            self.result_label.config(text=result_string)
        else:
            print("No file selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioGUI(root)
    root.mainloop()