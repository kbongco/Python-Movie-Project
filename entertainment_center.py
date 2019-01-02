import media

your_name = media.Movie("Your Name",
                        "A teenage boy and girl embark on a quest to meet each other after they began swapping bodies",
                        "https://en.wikipedia.org/wiki/File:Your_Name_poster.png",
                        "https://www.youtube.com/watch?v=o4-URMnBOPU")
Pokemon_first = media.Movie("Pokemon: Mewtwo Strikes Back",
                            "MewTwo vs Mew",
                            "https://en.wikipedia.org/wiki/Pok%C3%A9mon:_The_First_Movie#/media/File:Pokemon-mewtwo-strikes-back.jpg",
                            "https://www.youtube.com/watch?v=sSLuNZFa_3k")
print(Pokemon_first.storyline)
#print(your_name.storyline)
#media is previous file, Movie is class, your_name is instance
Pokemon_first.show_trailer()
