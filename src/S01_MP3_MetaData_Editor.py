# Shree KRISHNAya Namaha
# Copies mp3 files into artist/album folder Renames files, adds artist, album & comments in the metadata of audio file.
# Author: Nagabhushan S N
# Last Modified: 19/01/2020


from pathlib import Path
import pandas
import eyed3
import shutil


DATA_FILEPATH = Path('E:\Film Songs\Film Songs Audio\Kannada\Abachi CDs\Idhe Namma Uttara\Volume 04\MetaData.csv')
DIRPATH = Path('E:\Film Songs\Film Songs Audio\Kannada\Abachi CDs\Idhe Namma Uttara\Volume 04')


def update_metadata(datapath: Path, dirpath: Path):
    # https://stackoverflow.com/a/102285/3337089
    metadata = pandas.read_csv(datapath.as_posix())
    for i, row in metadata.iterrows():
        file_num = row['File Num']
        title = row['Title']
        artist = row['Artist']
        album = row['Album']
        year = row['Year']
        comments = 'Vocalist: P B Shreenivas'

        old_filename = f'{file_num:02} Track {file_num}.mp3'
        old_filepath = dirpath / old_filename
        new_filepath = dirpath / 'Sorted' / artist / album / f'{title}.mp3'
        new_filepath.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(old_filepath.as_posix(), new_filepath.as_posix())

        mp3_file = eyed3.load(new_filepath.as_posix())
        mp3_file.tag.title = title
        mp3_file.tag.artist = artist
        mp3_file.tag.album = album
        # mp3_file.tag.year = year
        mp3_file.tag.comments.set(comments)
        mp3_file.tag.save()
    return


def main():
    update_metadata(DATA_FILEPATH, DIRPATH)
    return


if __name__ == '__main__':
    main()
