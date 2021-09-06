import csv
with open("c141\moviedata.csv", encoding= 'utf-8') as f:
    data1=csv.reader(f)
    allData=list(data1)
    allMovies=allData[1:]
    header=allData[0]
header.append('posterlink')
with open('finalmovie.csv',"a",encoding="utf-8") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerows(header)
with open(r"C:\Users\aines\Desktop\Python\c141\movie_links.csv", encoding= 'utf-8') as f:
    reader=csv.reader(f)
    movielinkdata=list(reader)
    allmovielink=allMovies[1:] 
for movieitem in allMovies:
    posterfound=any(movieitem[8] in movielinkitem for movielinkitem in allmovielink)
    if posterfound:
        for movielinkitem in allmovielink:
            if movieitem[8]==movielinkitem[0]:
                movieitem.append(movielinkitem[1])     
                if len(movieitem==28):
                    with open('finalmovie.csv') as f:
                        csv_writer=csv.writer(f)
                        csv_writer.writerow(movieitem)
                    print("writing done")