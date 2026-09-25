class Genre:
    def __init__(self, name, totalStreams):
        self.genreName = name
        self.__totalStreams = totalStreams
        self.averageBpm = self.averageBpm
        self.isMainstream = isMainstream
        self.famousSong = famousSong

    def displayGenreInfo(self):
        status = "Yes" if self.isMainstream else "No"
        print(f"Genre: {self.genreName} | Total Streams: {self.__totalStreams} | Average BPM: {self.averageBpm} | Mainstream: {status} | Famous Song: {self.famousSong}")

    def updateStreamCount(self, addedStreams: int):
        if addedStreams < 0:
            print("Error: Cannot add negative streams.")
            return
        self.__totalStreams += addedStreams
        print(f"Updated Total Streams for {self.genreName}: {self.__totalStreams}")

    def updateFamousSong(self, newFamousSong: str):
        self.famousSong = newFamousSong
        print(f"Updated Famous Song for {self.genreName}: {self.famousSong}")

    def getTotalStreams(self):
        return self.__totalStreams

    class ElectronicGenre(Genre):
        def __init__(self, genreName: str, totalStreams: int, averageBpm: int, isMainstream: bool, famousSong: str, primarysynth: str):
            super().__init__(genreName, totalStreams, averageBpm, isMainstream, famousSong)
            self.primarysynth = primarysynth

    def displayGenreInfo(self):
        status = "Yes" if self.isMainstream else"No"
        print(f"Genre: {self.genreName}  | Total Streams: {self.__getTotalStreams()} | Average BPM: {self.averageBpm} | Mainstream: {status} | Famous Song: {self.famousSong} | Primary Synth: {self.primarysynth}")
    

    classGenreCatalog:
    def __init__(self, catalogName:str,establishedYear:int):
        self.catalogName = catalogName
        self.establishedYear = establishedYear
        self.genres = []

    def addGenre(self, genre: Genre):
        self.genres.append(genre)
        print(f"Added {genre.genreName} to {self.catalogName} catalog.")

    def displayCatalog(self):
        print(f"Catalog: {self.catalogName} | Established: {self.establishedYear}")
        if not self.genres:
            print("No genres in the catalog.")
            return
        for genre in self.genres:
            genre.displayGenreInfo()


if __name__ == "__main__":
    print("== TEST 1 - INHERITANCE SYSTEM ==")
    synthwave = ElectronicGenre("Synthwave", 1200000, 115, False, "Resonance - HOME", "Wave Synthesizer")
    print(f"Inhertied Attribute (averageBpm): {synthwave.averageBpm}")
    print(f"Inherited Private Accesor (getTotalStreams): {synthwave.getTotalStreams()}")
    synthwave.updareStreamCount(50000)

    print("\n== TEST 2 - AGGREGATION SYSTEM ==")
    pop_genre = Genre("Pop", 5000000, 120, True, "Blinding Lights - The Weeknd")
    catalog = GenreCatalog("KMG Music Global Catalog", 2026)
    catalog.addGenre(pop_genre)
    catalog.addGenre(synthwave)
    catalog.displayCatalog()