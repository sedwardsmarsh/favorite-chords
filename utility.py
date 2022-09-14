# A script that modifies the chord graph

class Song:
    '''Represents a song. 
    '''
    def __init__(self, id: str='', chords: dict[str,list[str]]=dict()) -> None:
        self.id: str = id
        self.chords: dict[str,list[str]] = chords

    def __str__(self) -> str:
        s = f'{self.id}\n'
        for chord in self.chords:
            s += f'{chord}-->{self.chords[chord]}\n'
        return s

    def populate(self, new_id: str, new_chords: dict[str,list[str]]) -> None:
        self.id = new_id
        self.chords = new_chords

    def info(self) -> tuple[str, dict[str,list[str]]]:
        return (self.id, self.chords)


class Chord_Graph:
    '''Represents all the songs from the chord graph.
    '''
    def __init__(self, path: str='README.md') -> None:
        self.songs: list[Song] = list()
        # self.graph: dict[str,list[str]] = dict()
        self.path = path

    def add(self, song: Song) -> None:
        self.songs.append(song)
        # write song to file
        with open(self.path, 'r+') as f:
            lines = f.readlines()
            block_end_idx = lines.index('```\n')

            # write id
            lines.insert(block_end_idx, f'\n\t%% {song.id}\n')

            # write chords
            curr_chord_idx = 0
            chords_for_song = list(song.chords)
            starting_num_chords = len(chords_for_song)
            starting_chord = True
            while len(song.chords) > 0:
                first_chord = chords_for_song[curr_chord_idx]
                if len(song.chords[first_chord]) == 0:
                    del song.chords[first_chord]
                else:
                    second_chord = song.chords[chords_for_song[curr_chord_idx]].pop(0)
                    if starting_chord == True:
                        second_chord_str = f'\t{first_chord}(({first_chord}))-->{second_chord}\n'
                        starting_chord = False
                    else:
                        second_chord_str = f'\t{first_chord}-->{second_chord}\n'
                    block_end_idx += 1
                    lines.insert(block_end_idx, second_chord_str)
                # avoid division by zero
                if len(song.chords) > 0:
                    curr_chord_idx = (curr_chord_idx + 1) % starting_num_chords
            lines = ''.join(lines) # create string from list
            f.seek(0) # jump to beginning of file
            f.write(lines) # flush into file
            
    def remove(self, id: str) -> None:
        pass

    def list(self) -> str:
        pass


class Interface:
    '''Handles input and output to the user.
    '''
    pass

graph = Chord_Graph('README.md')
graph.add(Song('test', {'C':['D','Cm'],'D':['G']}))
graph.add(Song('test2', {'C':['Cm'],'D':['G']}))

# user will enter chords as space delimited list of changes: C,A G,D D,Cm
pass