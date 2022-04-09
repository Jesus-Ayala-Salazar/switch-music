import sys
import os
import nus3volume
import subprocess
import json

def main():
    song_list   = sys.argv[1]
    
    with open(song_list, 'rt') as nus3file:
        data = json.load(nus3file)
    
    for entry in data:
        nus3bank_name = entry['nus3bank']
        # nus3bank_name = nus3bank_name.replace('.nus3audio', '.nus3bank')
        nus3bank_name = 'bgm_' + nus3bank_name   

        # subprocess.call(f"python3 nus3volume.py ~/smash-dump/stream/sound/bgm/{nus3bank_name} 0 4.7", shell=True)

if __name__ == '__main__':
    main()
