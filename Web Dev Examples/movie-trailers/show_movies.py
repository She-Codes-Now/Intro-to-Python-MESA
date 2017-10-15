import readXML

def main():

    # Get all movies from the XML
    aMovieList = readXML.readMoviesXML("movies.xml")

    while True:
      i = 0
      print("\n\n---------------------------------------------")
      print("Movie Trailer App in Python")
      print("(Enter 0 to exit)")
      print("---------------------------------------------")

      for movie in aMovieList:
        i = i + 1
        print("%d. %s" %(i, movie.title))
      print("---------------------------------------------")

      choice = input("Which movie trailer do you want to see? ")

      if choice == 0:
        print("Thank you for trying the app! Bye.")
        print("---------------------------------------------")
        break;

      if choice <= i: # len(aMovieList):
        aMovieList[choice-1].show_trailer()
      else:
        print("Sorry wrong option!. Retry")

main()
