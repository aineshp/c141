from flask import Flask, json,jsonify,request
import csv
all_movies=[]
with open(r"C:\Users\aines\Desktop\Python\c141\moviedata.csv", encoding= 'utf-8') as f:
  file1=csv.reader(f)
  allData=list(file1)
  all_movies=allData[1:]
likedMovies=[]
dislikedMovies=[]
didNotWatch=[]
app = Flask(__name__)
@app.route("/get-movies")
def getMovies():
  return jsonify({'data':all_movies[0],
  'status':'success'})


@app.route("/liked-movies",methods=["POST"])
def likedMoviesF():
  global all_movies
  movie=all_movies[0]
  all_movies=all_movies[1:]
  likedMovies.append(movie)
  return jsonify({'status':'success'}),201

@app.route("/disliked-movies",methods=["POST"])
def dislikedMoviesF():
  global all_movies
  movie=all_movies[0]
  all_movies=all_movies[1:]
  dislikedMovies.append(movie)
  return jsonify({'status':'success'}),201

@app.route("/did-not-watch",methods=['POST'])
def didNotWatchMovies():
  global all_movies
  movie=all_movies[0]
  all_movies=all_movies[1:]
  didNotWatch.append(movie)
  return jsonify({'status':'success'}),201  
  
if __name__=="__main__":
  app.run()  