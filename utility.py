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
    def __init__(self) -> None:
        self.songs: list[Song] = list()
        self.graph: dict[str,list[str]] = dict()

    def load(self, path: str='README.md') -> None:
        with open(path) as file:
            data = file.read()
            # TODO: replace these two lines with a regex
            start_idx = data.find('```mermaid')
            end_idx = data[start_idx:].find('```', 3)

            for line in data[start_idx:start_idx+end_idx].split('\n')[2:]:
                # TODO: replace the song artist and title search with a regex
                line = line.lstrip()
                if line.startswith('%%'):
                    id = line[3:]
                    new_song = Song(id, dict())
                    print(f'{id=}')

                elif line == '':
                    self.songs.append(new_song)
                
                # TODO: replace the chord search with a regex
                else:
                    # convert starting chord line to normal line
                    if '((' in line:
                        paren_start_idx = line.find('((')
                        paren_end_idx = line[paren_start_idx:].find('))')
                        line = line[:paren_start_idx] + line[paren_start_idx+paren_end_idx+2:]
                    chords = line.split('-->')
                    if chords[0] not in new_song.chords:
                        new_song.chords[chords[0]] = [chords[1]]
                    # don't add duplicate changes
                    elif chords[1] in new_song.chords[chords[0]]:
                        continue
                    else:
                        new_song.chords[chords[0]].append(chords[1])

    def add(self) -> None:
        pass
    
    def remove(self, id: str) -> None:
        pass

    def list(self) -> str:
        pass

graph = Chord_Graph()
graph.load()
print(graph.songs[1])
pass