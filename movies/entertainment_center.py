import media, fresh_tomatoes

reservoir_dogs = media.Movie("Reservoir Dogs", "You don't need proof when you got instinct.", "https://i.jeded.com/i/reservoir-dogs.13151.jpg", "https://www.youtube.com/watch?v=vayksn4Y93A")
insomnia = media.Movie("Insomnia", "You can sleep when you are dead", "http://www.martindonovan.org/graphics/insomniaposter.jpg", "https://www.youtube.com/watch?v=1OY5J11CWrE")
fargo = media.Movie("Fargo", "Blood has been shed, Jerry.", "http://vignette3.wikia.nocookie.net/fargo/images/d/d7/Fargo_movieposter.jpg/revision/latest?cb=20140226224031", "https://www.youtube.com/watch?v=h2tY82z3xXU")
no_country_for_oldmen = media.Movie("No country for old men", "Call it, friendo.", "http://static.rogerebert.com/uploads/movie/movie_poster/no-country-for-old-men-2007/large_6o0UWX2naW7HK45PDNYmoMIk5qs.jpg", "https://www.youtube.com/watch?v=qnwNuG1ayno")
american_beauty = media.Movie("American Beauty", "I'm just an ordinary guy with nothing to lose.", "http://lastnerdstanding.altervista.org/wp-content/uploads/2016/02/american-beauty-poster.jpg", "https://www.youtube.com/watch?v=3ycmmJ6rxA8")
seven = media.Movie("Se7en", " If you kill him, he will win.", "https://citelighter-cards.s3.amazonaws.com/p16qev16ib1fj710ol1jlak28llj0_72922.jpg", "https://www.youtube.com/watch?v=J4YV2_TcCoE")


movies = [reservoir_dogs, insomnia, fargo,no_country_for_oldmen,american_beauty,seven]
#fresh_tomatoes.open_movies_page(movies)
print "The class " + media.Movie.__name__ + " in the module "+media.Movie.__module__   + " has the following doc : " +media.Movie.__doc__