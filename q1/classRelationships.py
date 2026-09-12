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
            print("Error: Cannot add negative streams.")
            return
        
        self.__totalStreams += addedStreams
        print(f"Updated total streams for {self.genreName} to {self.getTotalStreams()}.")

    def updateFamousSong(self, newFamousSong: str):
        self.famousSong = newFamousSong
        print(f"Updated famous song for {self.genreName} to '{self.famousSong}'.")

    def getTotalStreams(self):
        return self.__totalStreams

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
    print("\n BEFORE RELATIONSHIP")
    catalog = GenreCatalog("KMG Music Genre Catalog", 2026)
    genre1= Genre("Pop", 5000000, 120, True, "Blinding Lights - The Weeknd")
    genre2 = Genre("RNB", 3000000, 80, True, "Miss Independent - Ne-Yo")
    genre3 = Genre("Dungeon Synth", 30000, 80, False, "The Knight Who Dreamed of Fire - Dungeon Synth")

    catalog.displayAllGenres()

    print("\n BUILDING RELATIONSHIP")
    catalog.addGenre(genre1)
    catalog.addGenre(genre2)
    catalog.addGenre(genre3)

    print("\n AFTER RELATIONSHIP")
    catalog.displayAllGenres()