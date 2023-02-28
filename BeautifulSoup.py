from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html5lib')
print(bs.h1)

bs.h1
bs.html.body.h1
bs.body.h1
bs.html.h1

try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
    # devolve null, executa um break ou algum outro "plano B"
else:
    # o programa continua. Nota: se você retornar ou executar um break no
    # catch da exceção, não será necessária a instrução "else"

    try:
        html = urlopen('http://pythonscrapingthisurldoesnotexist.com')
    except HTTPError as e:
        print(e)
    except URLError as e:
        print('The server could not be found!')
    else:
        print('It Worked!')
        print(bs.nonExistentTag)
        print(bs.nonExistentTag.someTag)
        
        try:
            badContent = bs.nonExistentTag.anotherTag
        except AttributeError as e:
            print('Tag was not found')
        else:
            if badContent == None:
                print(badContent)