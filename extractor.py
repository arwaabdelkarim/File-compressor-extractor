import FreeSimpleGUI as gui
import functions
import compressor_extractor

def run_gui():
    gui.theme('Black')

    label1 = gui.Text("Select folder to extract: ")
    input_box1 = gui.Input()
    choose_button1 = gui.FileBrowse("Choose", key="archive")

    label2 = gui.Text("Select destination folder: ")
    input_box2 = gui.Input()
    choose_button2 = gui.FolderBrowse("Choose", key="folder")

    back_button = gui.Button("Back")
    decompress_button = gui.Button("Extract", key="decompress")
    output_label = gui.Text(key='out', text_color='green')


    window = gui.Window("Archive Extractor", layout=[[label1, input_box1,choose_button1],
                                                          [label2, input_box2, choose_button2],
                                                          [decompress_button, output_label, gui.Push(), back_button]])

    while True:
        event, values = window.read()
        match event:
            case 'decompress':
                archive_path = values["archive"]
                dest_dir = values["folder"]
                functions.extract_zip(archive_path, dest_dir)
                window['out'].update(value="Files extracted successfully!")
            case 'Back':
                window.close()
                compressor_extractor.run_gui()
            case gui.WIN_CLOSED:
                break

    window.close()