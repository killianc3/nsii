import os
albumsPath = os.path.abspath("./albums")
albumsList = os.listdir(albumsPath)

liste = ["ozajhpofg.txt","zeafza.txt","a.txt"]


print(albumsPath)
print(albumsList)

AlbumName = "caca"

with open("./albums"+ '/' + AlbumName + '.txt', "w") as nAlbums:
	nAlbums.write("bouj"+'\n')
	nAlbums.write("bouj"+'\n')
	nAlbums.write("bouj"+'\n')

with open("./albums"+ '/' + AlbumName + '.txt', "r") as nAlbums:
	ola = nAlbums.readlines()

lo = ola + liste

with open("./albums"+ '/' + AlbumName + '.txt', "w") as nAlbums:
	for element in ola:
		nAlbums.write(element)
	for element in liste:
		
		nAlbums.write(element+'\n')
	

print(ola)

albumsPath = os.path.abspath("./albums")
albumsList = os.listdir(albumsPath)

print(albumsList)


albumName = albumsList.pop(0)
os.remove(os.path.join(albumsPath, albumName))