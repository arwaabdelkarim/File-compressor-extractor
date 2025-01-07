import compressor
import extractor
import FreeSimpleGUI as sg

def run_gui():
    sg.theme("Black")

    label1 = sg.Text("Do you want to compress or extract files?")
    compress_button = sg.Button("Compress")
    extract_button = sg.Button("Extract")
    exit_button = sg.Button("Exit")

    window = sg.Window("File-Compressor-Extractor", layout=[[label1],
                                                                 [compress_button,sg.Push(), extract_button],
                                                                 [sg.Push(), exit_button, sg.Push()]])

    while True:
        event, value = window.read()
        match event:
            case 'Compress':
                window.close()
                compressor.run_gui()
            case 'Extract':
                window.close()
                extractor.run_gui()
            case 'Exit':
                break
            case sg.WIN_CLOSED:
                break
    window.close()

if __name__ == "__main__":
    run_gui()

