import requests

def test_status_and_body(id_, title_):
    headers = {
        'Accept' : '*/*',
        'User-Agent' : 'request',
    }
    url = "https://jsonplaceholder.typicode.com/users/"+id_+"/todos"

    resposta = requests.get(url, headers=headers)

    conteudo = resposta.json()

    id = conteudo[0]
    title = conteudo[0]["title"]

    print (id)

    if resposta.status_code==200:
        assert len(conteudo) > 0 and id is not None
        assert title == title_
    else:
        assert False

if __name__ == '__main__':
    test_status_and_body("1", "delectus aut autem")