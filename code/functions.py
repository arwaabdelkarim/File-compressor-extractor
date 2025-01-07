import zipfile
import pathlib


def make_archive(filepaths, destination):
    dest_path = pathlib.Path(destination, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as zipf:
        for file in filepaths:
            file = pathlib.Path(file)
            zipf.write(file, arcname=file.name)



def extract_zip(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as unzip:
        unzip.extractall(
            dest_dir)
