from urllib.request import urlopen
from urllib.error import HTTPError
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
#else:
    # o programa continua. Nota: se você retornar ou executar um break no
    # catch da exceção, não será necessária a instrução "else"