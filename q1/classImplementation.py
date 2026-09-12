class Genre:
    def __init__(self, genreName: str, totalStreams: int, averageBpm: int, isMainstream: bool, famousSong: str):
        self.genre_name = genreName
        self.__total_streams = totalStreams
        self.average_bpm = averageBpm
        self.is_mainstream = isMainstream
        self.famous_song = famousSong

    def displayGenreInfo(self):
        status = "Yes" if self.is_mainstream else "No"
        print(f"Genre: {self.genre_name} | Streams: {self.__total_streams} | Generalized BPM of Genre: {self.average_bpm} | Mainstream: {status} | Famous Song: {self.famous_song}")
# I just wanted to say that genre and the stream numbers are entirely distinct. I associated the famous song component with a song that topped the charts or is basically famous. The mainstream part is for the genres, which desribes whether the genre as a whole dominates commerical radio and mass media compared to niche genres (such as Vaporwave).

    def updateStreamCount(self, addedStreams: int):
        if addedStreams < 0:
            print("Error: Cannot add negative streams.")
            return
        self.__total_streams += addedStreams
        if addedStreams> 999999:
            self.is_mainstream = True
        print(f"Updated total streams for {self.genre_name}: {self.__total_streams}")

    def updateFamousSong(self, new_song: str):
        self.famous_song = new_song
        print(f"Updated famous song for {self.genre_name}: {self.famous_song}")

    def getTotalStreams(self):
        return self.__total_streams     

if __name__ == "__main__":
    object1 = Genre("Pop", 5000000, 120, True, "Blinding Lights - The Weeknd")
    object2 = Genre("RNB", 3000000, 80, True, "Miss Independent - Ne-Yo")

    print("---BEFORE---")
    print("Object 1 (Pop):")
    object1.displayGenreInfo()
    print("Object 2 (RNB):")
    object2.displayGenreInfo()

    print("\nUpdating streams and famous song on Object 1 (Pop) only:")
    object1.updateStreamCount(1000000)
    object1.updateFamousSong("Say So - Doja Cat")

    print("---AFTER---")
    print("Object 1 (Pop):")
    object1.displayGenreInfo()
    print("Object 2 (RNB):")
    object2.displayGenreInfo()