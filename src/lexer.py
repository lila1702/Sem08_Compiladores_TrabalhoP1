# lexer.py
from consts import Consts
from my_tokens import Token

class Lexer:
    def __init__(self, source_code):
        self.code = source_code
        self.current = None
        self.index, self.coluna, self.linha = -1, -1, 0
        self.__advance()

    def __advance(self):
        self.index += 1
        self.coluna += 1
        if (self.index < len(self.code)):
            self.current = self.code[self.index]
        else:
            self.current = None

    def make_tokens(self):
        tokens = []
        while (self.current is not None):
            if (self.current in ' \t\n'):
                self.__advance()
            elif (self.current in Consts.DIGITOS):
                tokens.append(self.__make_number())
            elif (self.current == '"'):
                tokens.append(self.__make_string())
            elif (self.current in Consts.LETRAS):
                tokens.append(self.__make_identifier_or_keyword())
            elif (self.current in [Consts.LBRACE, Consts.RBRACE, Consts.COLON, Consts.SEMICOLON, Consts.COMMA]):
                tokens.append(Token(self.current))
                self.__advance()
            else:
                raise Exception(f"Erro: Símbolo '{self.current}' desconhecido na linha {self.linha + 1}")
        tokens.append(Token(Consts.EOF))
        return tokens

    def __make_number(self):
        num_str = ''
        while (self.current is not None and self.current in Consts.DIGITOS):
            num_str += self.current
            self.__advance()
        return Token(Consts.INT, int(num_str))

    def __make_string(self):
        string_value = ""
        self.__advance()
        while (self.current is not None and self.current != '"'):
            string_value += self.current
            self.__advance()
        self.__advance()  # Fechar a string
        return Token(Consts.STRING, string_value)

    def __make_identifier_or_keyword(self):
        id_str = ''
        while (self.current is not None and self.current in Consts.LETRAS_DIGITOS + '_'):
            id_str += self.current
            self.__advance()
        if (id_str in Consts.KEYS):
            return Token(id_str)
        return Token(Consts.STRING, id_str)
