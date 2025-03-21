def movie_title():
    movies = {}
    unique_titles = set()

    
    while len(movies) < 3:
        movie_title = input("Enter the title of your favorite movie: ").strip()
        release_year = input("Enter the release year of the movie: ").strip()

        
        if movie_title in unique_titles:
            print("This movie is already in your collection. Please enter a different movie.")
        else:
            unique_titles.add(movie_title)
            movies[movie_title] = release_year
            print(f"Added '{movie_title}' ({release_year}) to your collection.")


    while True:
        remove_movie = input("Do you want to remove a movie from your collection? (yes/no): ").strip().lower()
        if remove_movie == 'yes':
            movie_to_remove = input("Enter the title of the movie you want to remove: ").strip()
            if movie_to_remove in movies:
                del movies[movie_to_remove]
                unique_titles.remove(movie_to_remove)
                print(f"Removed '{movie_to_remove}' from your collection.")
            else:
                print("This movie is not in your collection.")
        elif remove_movie == 'no':
            break
        else:
            print("Please answer with 'yes' or 'no'.")

   
    print("\nUpdated Movie Collection:")
    for title, year in movies.items():
        print(f"{title} ({year})")
    
    print("\nUnique Movie Titles:")
    print(unique_titles)

movie_title()