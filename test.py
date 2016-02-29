def hello():
    print("hello")


names = set(['Jim', 'Dennis', 'Mikael', 'Filip', 'David', 'Johan'])
print("Type of names is {0}".format(type(names)))


if 'Jim' in names:
    print("Jim was found")

if 'Patrik' not in names:
    print("Patrik was not found")


moreNames = set(['Jim', 'Dennis', 'Roberto'])

print("Alla namn som finns i någon av setten (union): {}".format(names.union(moreNames)))
print("Alla namn som finns i båda setten (intersection): {}".format(names.intersection(moreNames)))

# Kommentarer i Python görs med "#" tecknet.

# Ta in en sträng och skriv ut antalet gånger ordet "men" förekommer.

searchTerm = "men"
searchString = "Äpplen kan vara gröna men kaniner är sällan blåa. Dock är pengar sweet men potatisar bruna."

count = searchString.find(searchTerm)

print("Söksträng: {}".format(searchString))
print("Ordet '{}' förekommer {} gånger".format(searchTerm, searchString.count(searchTerm)))
print("Capitalize: {}".format(searchString.capitalize()))
print("Låt oss se vad index returnerar: {}".format(searchString.index(searchTerm)))


def contains_letters(term):
    words = term.split(' ')
    try:
        next(word for word in words if word.isalpha())
        answer = True
    except StopIteration:
        answer = False
    except:
        print("Något riktigt kasst inträffade")
    return answer


term = "Jim heter jag, och är tjugofem år gammal"
print(term)
print("Innehåller ovan text endast siffror? {}".format("Ja" if term.isdigit() else "Nej"))
print("Innehåller ovan text endast bokstäver? {}".format("Ja" if term.isalpha() else "Nej"))
print("Innehåller ovan text ett ord bestående av endast bokstäver? {}".format("Ja" if contains_letters(searchTerm) else "Nej"))

