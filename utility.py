# A script that modifies the chord graph

class Song:
    def __init__(self) -> None:
        self.artist: str = ''
        self.title: str = ''
        self.chords: dict[str] = dict()

    def populate(self, new_artist: str, new_title: str, new_chords: dict[str]) -> None:
        self.artist = new_artist
        self.title = new_title
        self.chords = new_chords

    def info(self) -> tuple[str, str, dict[str]]:
        return (self.artist, self.title, self.chords)

class Chord_Graph:
    def __init__(self) -> None:
        self.songs: dict[dict[Song]] = dict()

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
                    id = line.split('-')
                    artist = id[0][3:].strip()
                    title = id[1][1:]
                    # print(f'{artist=} {title=}')

                elif line == '':
                    continue
                
                # TODO: replace the chord search with a regex
                else:
                    print(line)
                    self.songs[artist][title].append(line)

graph = Chord_Graph()
graph.load()