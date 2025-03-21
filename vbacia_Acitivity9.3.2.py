print("=============================================")

movies = []
for i in range(5):
    movie = input(f"Enter a Favorite Movie: ")
    movies.append(movie)
    i + 1

movies_tuple = tuple(movies)
print("\n Top 5 Movies: ", movies_tuple)


try:
    movies_tuple[0] = "new movies"
except TypeError as e:
    print("\nError Tuples is Immutable: ",e)





    

    
     
