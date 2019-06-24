from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_criar_uma_lista_acessar_url(self):
        # Fulano ouviu falar de uma nova aplicação online interessante para
        #lista de tarefas. Ele decide verificar sua homepage
        self.browser.get('http://localhost:8000')

        # Ele percebe que o título da página e o cabeçalho mencionam listas
        # de tarefas (to-do)
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test!")

        # Ele é convidado a inserir um ítem na tarefa imediatamente.

        # Ele digita "Cortar a grama" em uma caixa de texto.

        # Quando ele tecla Enter, a página é atualizada, e agora a página listas
        # "1: Cortar a grama" como um ítem em uma lista de tarefas.

        # Ainda continua havendo uma caixa de texto convidando-o a acrescentar outro
        # item. Ele insere "Lavar a louça" e tecla Enter.

        # A página é atualizada e agora aparecem os dois itens em sua lista.

        # Fulano se pergunta se o site lembrará de sua lista. Então ele nota que o site
        # gerou uma URL único para ele --  há um pequeno texto explicativo para isso.

        # Ele acessa esse URL - sua lista de tarefas continua lá.

        # Satisfeito, volta a dormir
if __name__ == "__main__":
    unittest.main(warnings='ignore')
