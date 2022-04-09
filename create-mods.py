import sys
import requests
import json

def main():
    song_list = sys.argv[1]
    
    with open(song_list, 'rt') as song_list_file:
        data = json.load(song_list_file)

    for entry in data:
        song_name   = entry['name']
        song_id     = entry['id']
        file_dest   = f"./nus3audio-songs/{song_name}.nus3audio"
        url         = f'https://smashcustommusic.net/nus3audio/{str(song_id)}'
        content     = requests.get(url, stream=True).content
        
        with open(file_dest, 'wb') as out_file:    
            out_file.write(content)

if __name__ == '__main__':
    main()
