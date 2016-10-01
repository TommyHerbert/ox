def tell(userUtterance):
    print 'Hello.'

class Singer:
    name = ''
    tracks = []

class Track:
    title = ''

class Concept:
    lexicalForm = ['']
    referent = None

class Slot:
    category = None

class Category

class Noun(Category)

adele = Singer()
adele.name = 'Adele'
hello = Track()
hello.title = 'hello'
adele.tracks.append(hello)
track = Concept()
track.lexicalForm = ['track']
track.referent = Track
entities = [adele, hello]
favouriteThing = Slot()
favouriteThing.category = Noun
favouriteQuestion = Concept()
favouriteQuestion.lexicalForm = ["What's your favourite ", favouriteThing, '?']
singerSlot = Slot()
