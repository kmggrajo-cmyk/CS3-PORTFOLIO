# SG4 - Understanding Classes and Objects

## Class Name

`Genre`

## Class Description

This class represents a musical genre within a music management or streaming system, capturing its identifying traits, global statistics, and cultural trends.

## Properties

| Property | Data Type | Description |
| --- | --- | --- |
| genreName | string | The official name of the music genre (e.g., Jazz, OPM, Rock). |
| totalStreams | int | The total number of streams or listeners accumulated globally as of the current year. |
| averageBpm | int | The typical average tempo or beats per minute (BPM) associated with the genre. |
| isMainstream | boolean | Indicates whether the genre currently holds mainstream/commercial popularity. |
| famousSong | string | The title and artist/artists of the genre's current top hit or most commercially streamed song. |

## Methods

| Method | Description |
| --- | --- |
| displayGenreInfo() | Prints a formatted summary of the genre's name, stream count, and mainstream status. |
| updateStreamCount(addedStreams: int) | Updates the total stream count by adding newly accumulated streams. |
| updateFamousSong(songInfo: string) | Takes a new song title and its artist/artists as a parameter to update the current top hit based on that genre. |


## Class Diagram
[Class Diagram](images/classDiagram.png)

## Design Explanation

### Why did you choose this class?

I chose this class because I really like discovering new artists and trying out new genres. It is a fun yet intricate way to explore and listen to different kinds of music, allowing me to further delve into the vast diversity of the music industry.

### Which property is the most important? Why?

The `genreName` property is the most important because it encapsulates the primary identity of the object. It primarily is an identifier that helps the system distinguish between different genre records and properly sort them in a music catalog database.

### Which method is the most useful? Why?

The `updateFamousSong(songInfo: string)` method is the most useful because musical trends and hits are continuously changing. Having a method with a parameter allows the system to easily keep up with new trends and update the representative top track whenever a fresh song takes over the charts.
