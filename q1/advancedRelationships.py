class Genre:
    def __init__(self, genreName: str, totalStreams: int, averageBpm: int, isMainstream: bool, famousSong: str):
        self.genreName = genreName
        self.__totalStreams = totalStreams
        self.averageBpm = averageBpm
        self.isMainstream = isMainstream
        self.famousSong = famousSong

    def displayGenreInfo(self):
        status = "Yes" if self.isMainstream else "No"
        print(f"Genre: {self.genreName} | Streams: {self.getTotalStreams()} | Average BPM: {self.averageBpm} | Mainstream: {status} | Famous Song: {self.famousSong}")

    def updateStreamCount(self, addedStreams: int):
        if addedStreams < 0:
            print(f"Genre: {self.genreName} | Error: Cannot add negative streams.")
            return
        self.__totalStreams += addedStreams
        print(f"Genre: {self.genreName} | Updated total streams to {self.getTotalStreams()}.")

    def getTotalStreams(self):
        return self.__totalStreams

class ElectronicGenre(Genre):
    def __init__(self, genreName: str, totalStreams: int, averageBpm: int, isMainstream: bool, famousSong: str, primarysynth: str):
        super().__init__(genreName, totalStreams, averageBpm, isMainstream, famousSong)
        self.primarysynth = primarysynth

    def displayGenreInfo(self):
        super().displayGenreInfo()
        print(f"Primary Synth: {self.primarysynth}")

class GenreCatalog:
    def __init__(self, catalogName: str, establishedYear: int):
        self.catalogName = catalogName
        self.establishedYear = establishedYear
        self.genres = []

    def addGenre(self, genre: Genre):
        self.genres.append(genre)
        print(f"Added genre: {genre.genreName} to {self.catalogName} (Est. {self.establishedYear})")

    def displayAllGenres(self):
        print(f"Genre Catalog: {self.catalogName} (Established: {self.establishedYear})")
        if not self.genres:
            print("No genres in the catalog.")
            return
        for genre in self.genres:
            genre.displayGenreInfo()

if __name__ == "__main__":
    pop = Genre("Pop", 5000000, 120, True, "Blinding Lights - The Weeknd")
    rnb = Genre("RNB", 3000000, 80, True, "Miss Independent - Ne-Yo")
    dungeon_synth = ElectronicGenre(
        genreName = "Dungeon Synth",
        totalStreams = 30000, 
        averageBpm = 80, 
        isMainstream = False, 
        famousSong = "The Knight Who Dreamed of Fire - Dungeon Synth", 
        primarysynth = "FM Synthesizer"
    )


    catalog = GenreCatalog("KMG Music Genre Catalog", 2026)
    catalog.addGenre(pop)
    catalog.addGenre(rnb)
    catalog.addGenre(dungeon_synth)
    catalog.displayAllGenres()


print("\n--- Testing Aggregation ---")
print("Destroying GenreCatalog Object to Verify Aggregation ---")
del catalog
pop.displayGenreInfo()
dungeon_synth.displayGenreInfo()

print("\nVerifcation: Objects still exist in memory.")
dungeon_synth.displayGenreInfo()