from Django_git.game import Game, Genre


genre1_create = Genre(name='Action')
genre2_create = Genre(name='Adventure')

game1_create = Game(
    title='The Legend of Zelda',
    data='1986-02-21',
    rating=9.2
)

game2_create = Game(
    title='Final Fantasy VII',
    data='1997-01-31',
    rating=9.5
)

genre1_create.save()
genre2_create.save()

game1_create.save()
game2_create.save()


genre1 = Genre.objects.get(id=1)
genre2 = Genre.objects.get(id=2)

game1 = Game.objects.get(id=1)
game2 = Game.objects.get(id=2)

game2.genres.add(genre1)
game1.genres.add(genre1, genre2)


# Перевірка
print(Game.objects.all())
print(Genre.objects.all())