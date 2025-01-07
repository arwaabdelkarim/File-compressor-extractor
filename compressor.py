import FreeSimpleGUI as gui
import functions
import compressor_extractor

def run_gui():
    gui.theme("Black")
    label1 = gui.Text("Select files to compress: ")
    input_box1 = gui.Input()
    button1 = gui.FilesBrowse("Choose",
                              key="files")

    label2 = gui.Text("Select destination folder: ")
    input_box2 = gui.Input()
    button2 = gui.FolderBrowse("Choose", key="folder")

    back_button = gui.Button("Back")
    compress_button = gui.Button("Compress")
    output_label = gui.Text(key='out', text_color='green')

    window = gui.Window("File Zipper", background_color="black",
                        layout=[[label1, input_box1, button1],
                                [label2, input_box2, button2],
                                [compress_button, output_label, gui.Push(), back_button]])
    while True:
        event, values = window.read()

        match event:
            case 'Compress':
                filepaths = values['files'].split(";")
                folderpath = values['folder']
                functions.make_archive(filepaths, folderpath)
                window['out'].update(value="Files compressed successfully!")
            case 'Back':
                window.close()
                compressor_extractor.run_gui()
            case gui.WIN_CLOSED:
                break
    window.close()