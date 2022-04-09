import sys
import subprocess
import json

def main():
    song_list       = sys.argv[1]
    nus3bank_list   = sys.argv[2]
    
    with open(song_list, 'rt') as song_list_file:
        new_songs_list = json.load(song_list_file)

    with open(nus3bank_list, 'rt') as nus3bank_file:
        nus3bank_list = json.load(nus3bank_file)

    subprocess.call("mkdir ./mods", shell=True)

    for i in range(52):
        new_song_name   = new_songs_list[i]['name']
        nus3audio_name  = 'bgm_' + nus3bank_list[i]['nus3bank']
        nus3bank_name   = nus3audio_name.replace('.nus3audio', '.nus3bank')


        subprocess.call(f'cp "./nus3audio-songs/{new_song_name}.nus3audio" "./mods/{new_song_name}/stream;/sound/bgm/"', shell=True)
        subprocess.call(f'mv "./mods/{new_song_name}/stream;/sound/bgm/{new_song_name}.nus3audio" "./mods/{new_song_name}/stream;/sound/bgm/{nus3audio_name}"', shell=True)


    for entry in new_songs_list:
        song_name   = entry['name']
        subprocess.call(f'mkdir -p "./mods/{song_name}/stream;/sound/bgm/"', shell=True)

if __name__ == '__main__':
    main()
