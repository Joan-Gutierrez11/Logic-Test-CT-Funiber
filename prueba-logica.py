from pprint import pprint

## Animals sounds
# frog: brr, birip, brrah, croac
# dragon-fly: fiu, plop, pep
# cricket: cric-cric, trri-trri, bri-bri

## Songs
# brr, fiu, cric-cric, brrah
# pep, birip, trri-trri, croac
# bri-bri, plop, cric-cric, brrah

def create_sounds_dictionary(sounds: list, songs: int):
    soundsD = {}
    for _sound in sounds:
        soundsD[_sound] = [ -1 for i in range(songs) ]
    return soundsD

def generate_music_sequence(soundsD: dict, songs: list):
    for i in range(len(songs)):
        _song = songs[i]
        for idx in range(len(_song)):
            _sound_song = _song[idx]
            soundsD[_sound_song][i] = idx

def get_sequence(soundsD: dict, songs: list, sound: str):
    indices = soundsD.get(sound, None)
    if not indices:
        raise Exception("No existe una cancion que tenga ese sonido")

    idx_song = -1
    idx_sound_in_song = -1

    for i in range(len(indices)):
        if indices[i] != -1:
            idx_song = i
            idx_sound_in_song = indices[i]
    
    if idx_song == -1 or idx_sound_in_song == -1:
        raise Exception("Ese sonido no pertenece a ninguna cancion")
    
    sound_reproduction = songs[idx_song]
    if idx_sound_in_song >= len(sound_reproduction)-1:
        return []
    return sound_reproduction[idx_sound_in_song+1:]

# Main program

def main():
    # Sounds
    frog = ['brr', 'birip', 'brrah', 'croac']
    dragon_fly = ['fiu', 'plop', 'pep']
    cricket = ['cric-cric', 'trri-trri', 'bri-bri']
    
    # Songs
    song1 = ['brr', 'fiu', 'cric-cric', 'brrah']
    song2 = ['pep', 'birip', 'trri-trri', 'croac']
    song3 = ['bri-bri', 'plop', 'cric-cric', 'brrah']

    songs = [song1, song2, song3]
    sounds = frog+dragon_fly+cricket

    D = create_sounds_dictionary(sounds, len(songs))
    generate_music_sequence(D, songs)
    # pprint(D)

    user_sound = input('Ingrese un sonido: ')

    try:
        sequence = get_sequence(D, songs, user_sound)
        if len(sequence) < 1:
            print('...')
            return
            
        print(', '.join(sequence))
    except Exception as e:
        print(e)

main()