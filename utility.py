# A script that modifies the chord graph

class Song:
    def __init__(self, id: str='', chords: dict[str,str]=dict) -> None:
        self.id: str = id
        self.chords: dict[str,str] = chords

    def populate(self, new_id: str, new_chords: dict[str,str]) -> None:
        self.id = new_id
        self.chords = new_chords

    def info(self) -> tuple[str, dict[str,str]]:
        return (self.id, self.chords)

class Chord_Graph:
    def __init__(self) -> None:
        self.songs: list[Song] = list()

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
                    self.songs.append(Song(id))
                    print(f'{id=}')

                elif line == '':
                    continue
                
                # TODO: replace the chord search with a regex
                else:
                    print(line)

graph = Chord_Graph()
graph.load()
pass