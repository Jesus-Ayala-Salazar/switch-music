import sys
import requests

def main():
    song_list = sys.argv[1]
    
    with open(song_list, 'rt') as song_list_file:
        for song_ID in song_list_file:
            url = f'https://smashcustommusic.net/nus3audio/{song_ID}'
            file_dest = './DIRE.nus3audio'

    with open(file_dest, 'wb') as out_file:
        content = requests.get(url, stream=True).content
        out_file.write(content)

if __name__ == '__main__':
    main()
