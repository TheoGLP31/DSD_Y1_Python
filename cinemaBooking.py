movies = []

"""
abc, 1 2 3
def, 4 5 6
ghi, 7 8 9
jkl, 10 11 12
mno, 13 14 15
pqr, 16 17 18
stu, 19 20 21
vwx, 22 23 24
yz, 25 26
"""

while True:
    choice = input("(1) View all movies, (2) Add a movie, (3) Remove a movie, (4) Find a movie, (5) Exit: ")
    if choice == "1":
        print(movies)
    elif choice == "2":
        newMovie = input("Enter the new movie name: ")
        movies.append(newMovie)
    elif choice == "3":
        movieToRemove = input("What movie to remove? ")
        movies.remove(movieToRemove)
    elif choice == "4":
        movieToFind = input("What movie would you like to find? ")
        if movieToFind in movies:
            print(movieToFind)
        else:
            print("no.")
    elif choice == "5":
        break
    else:
        print("no")