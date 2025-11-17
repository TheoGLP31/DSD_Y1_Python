songs = []

for i in range(1, 6):
    song = input("Enter song number " + str(i) + ": ")
    songs.append(song)


print(songs)
while True:
    print(f"There are {len(songs)} songs.")
    choice = input("(1) Add song, (2) Remove song, (3) Sort list: ")
    if choice == "1":
        newSong = input(f"Enter song number {len(songs) + 1}: ")
        songs.append(newSong)
    elif choice == "2":
        if len(songs) == 0:
            print("No more songs to remove! ")
        else:
            songToRemove = input("What song would you like to remove? ").lower()
            songs.remove(songToRemove)
            print(songs)
    elif choice == "3":
        songs.sort()
        print(songs)
    else:
        print("no")

    print(f"There are {len(songs)} songs.")