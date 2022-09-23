from modelo import Filme, Serie, Playlist

#Filme Duro de Matar
duro_de_matar = Filme("Duro de Matar", 1988, 132)
duro_de_matar.dar_like()

#Serie Sherlock
sherlock = Serie("Sherlock", 2010, 4)
sherlock.dar_like()

#Serie Os três patetas
tres_patetas = Serie("Os três patetas", 1922, 26)

#Filme Scary Movie
todo_mundo_em_panico = Filme("Todo mundo em pânico", 2000, 88)

#Filme Pirats do Vale do Silicio
piratas_do_vale_do_silico = Filme("Piratas do vale do silicio", 1999, 97)

#Serie Star Trek: The Original Series
star_trek_original_series = Serie("Star Trek: The Original Series", 1969, 3)

#Filme Star Wars: A Ameaça Fantasma
star_wars_a_ameaca_fantasma = Filme("Star Wars: A Ameaça Fantasma", 1999, 136)

#Filme Tron (1982)
tron = Filme("Tron", 1982, 96)

#Criando a lista de filmes e series
filmes_e_series = [duro_de_matar, sherlock, tres_patetas, todo_mundo_em_panico, piratas_do_vale_do_silico, star_trek_original_series, star_wars_a_ameaca_fantasma, tron]

#Criando uma playlist
playlist_fim_de_semana = Playlist("Playlist fim de semana", filmes_e_series)

#Imprimindo o tamanho da playlist
print("Tamanho da playlist: {}.".format(len(playlist_fim_de_semana)))

#Mostrando a playlist
for programa in playlist_fim_de_semana:
    print(programa)

#Verificando se o filme Duro de Matar esta contido na lista
print("Duro de matar está nessa playlist? {}.".format(duro_de_matar in playlist_fim_de_semana))