from ast import arg
from pytube import Playlist, YouTube
import sys


def main():
    youtube_playlist = sys.argv[1]
    save_path = sys.argv[2]

    print("-----------------")    
    print(youtube_playlist)
    print(save_path)

    try:
        p = Playlist(youtube_playlist)
        print(f'Downloading: {p.title}')

        for v in p.videos:
            print(f'{v.title}')
            st = v.streams.get_highest_resolution()
            file_num = v.title.split(' ')[0].replace(".", "-") + "_"
            st.download(save_path, None, file_num)

        print('Playlist is downloaded !!!')
    except: 
        v = YouTube(youtube_playlist)
        print(f'{v.title}')
        st = v.streams.get_highest_resolution()
        file_num = v.title.split(' ')[0].replace(".", "-") + "_"
        st.download(save_path, None, file_num)
        print("Downloaded !!!")

if __name__ == "__main__":
    main()
