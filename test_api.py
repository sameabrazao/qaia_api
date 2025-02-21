import unittest
import requests

class MyTestCase(unittest.TestCase):
    #fdefinição do headers e url base para todos os cenários
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request',
        'Content-type' : 'application/json; charset=UTF-8',
    }
    url = "https://jsonplaceholder.typicode.com"

    #get de todos usuário de id 1, as validações das resposta foram apenas para veriricar se o status foi de sucesso e se a resposta não foi vazia
    def test_getAllPosts(self):
        resposta = requests.get(url=MyTestCase.url+"/users/1/todos", headers=MyTestCase.headers)
        conteudo = resposta.json()
        self.assertEqual(resposta.status_code, 200, "Fail")
        self.assertEqual(conteudo is not None, True, "Fail")

    #get de um registro incompleto especifico do usuário com userid 1, as validações foram do stautus e que o campo competed está com valor false
    def test_getAllPostsIncompleted(self):
        resposta = requests.get(url=MyTestCase.url + "/users/1/todos/?id=1", headers=MyTestCase.headers)
        conteudo = resposta.json()
        status = conteudo[0]["completed"]
        self.assertEqual(resposta.status_code, 200, "Fail")
        self.assertEqual(status, False, True)

    # get de um registro completo especifico do usuário com userid 1, as validações foram do stautus e que o campo competed está com valor true
    def test_getAllPostsCompleted(self):
        resposta = requests.get(url=MyTestCase.url + "/users/1/todos/?id=4", headers=MyTestCase.headers)
        conteudo = resposta.json()
        print(conteudo)
        status = conteudo[0]["completed"]
        print(status)
        self.assertEqual(resposta.status_code, 200, "Fail")
        self.assertEqual(conteudo is not None, True, "Fail")
        self.assertEqual(status, True, False)

    # get de um registro do usuário com id 1, as validações foram do nome e email do usuário
    def test_getUser(self):
        resposta = requests.get(url=MyTestCase.url+"/users/1/", headers=MyTestCase.headers)
        conteudo = resposta.json()
        nome = conteudo["name"]
        email = conteudo["email"]
        self.assertEqual(resposta.status_code, 200, "Fail")
        self.assertEqual(nome, "Leanne Graham", "Fail")
        self.assertEqual(email, "Sincere@april.biz", "Fail")

    #get dos registros do album com id 1, validado apenas status e que não está vazio
    def test_getPhotos(self):
        resposta = requests.get(url=MyTestCase.url+"/albums/1/photos", headers=MyTestCase.headers)
        conteudo = resposta.json()
        self.assertEqual(resposta.status_code, 200, "Fail")
        self.assertEqual(conteudo is not None, True, "Fail")

    #get de todos os comentário do post com id 1, validado apenas status e que não está vazio
    def test_getPosts(self):
        resposta = requests.get(url=MyTestCase.url+"/posts/1/comments", headers=MyTestCase.headers)
        conteudo = resposta.json()
        self.assertEqual(resposta.status_code, 200, "Fail")
        self.assertEqual(conteudo is not None, True, "Fail")

    #adição de post, validação de id de status de sucesso e id gerado
    def test_postPosts(self):
        body = {
            'title': 'Samea',
            'body': 'QA',
            'userId': 111
        }
        resposta = requests.post(url=MyTestCase.url+"/posts", headers=MyTestCase.headers, json=body)
        conteudo = resposta.json()
        id = conteudo["id"]
        self.assertEqual(resposta.status_code, 201, "Fail")
        self.assertEqual(id, 101, "Fail")

    #post de photo para album de id 1, validação de status e id
    def test_postAlbumPhoto(self):
        body = {
            'albumId': 1,
            'title': 'Test Samea',
            'url': 'https://miro.medium.com/v2/resize:fit:786/format:webp/1*ylpP9Cq9XuiJ7e7RzLVqfg.png',
            'thumbnailUrl': 'https://miro.medium.com/v2/resize:fit:786/format:webp/1*ylpP9Cq9XuiJ7e7RzLVqfg.png'
        }
        resposta = requests.post(url=MyTestCase.url+"albums/1/photos", headers=MyTestCase.headers, json=body)
        conteudo = resposta.json()
        id = conteudo["id"]
        self.assertEqual(resposta.status_code, 201, "Fail")
        self.assertEqual(id, 5001, "Fail")

    #put de post validações na resposta: status de sucesso, conteudo não vazio e id do post alterado
    def test_postPostsUpdate(self):
        body = {
            'id': '1',
            'title': 'Samea',
            'body': 'QA',
            'userId': 1
        }
        resposta = requests.put(url=MyTestCase.url+"/posts/1", headers=MyTestCase.headers, json=body)
        conteudo = resposta.json()
        id = conteudo["id"]
        self.assertEqual(resposta.status_code, 200, "Fail")
        self.assertEqual(conteudo is not None, True, "Fail")
        self.assertEqual(id, 1, "Fail")

    def test_deletePost(self):
        resposta = requests.delete(MyTestCase.url+"/posts/1", headers=MyTestCase.headers)
        self.assertEqual(resposta.status_code, 200, "Fail")


if __name__ == '__main__':
    unittest.main()
