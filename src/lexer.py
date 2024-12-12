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
            elif (self.current == "="):
                self.__advance()
                # Comparação de Igualdade
                if (self.current == "="):
                    self.__advance()
                    tokens.append(Token(Consts.IGUAL))
                # Atribuição
                else:
                    tokens.append(Token(Consts.ASSIGN))
            elif (self.current in "<>!="):
                char = self.current
                self.__advance()
                # Para <=, >=, !=
                if (self.current == "="):
                    if (char == ">"):
                        tokens.append(Token(Consts.MAIORIGUAL))
                    elif (char == "<"):
                        tokens.append(Token(Consts.MENORIGUAL))
                    else:
                        tokens.append(Token(Consts.DIFERENTE))
                    self.__advance()
                else:
                    tokens.append(Token(Consts.MAIOR if char == ">" else Consts.MENOR))
            else:
                raise Exception(f"Erro: Símbolo '{self.current}' desconhecido na linha {self.linha + 1}")
        tokens.append(Token(Consts.EOF))
        return tokens

    def __make_number(self):
        num_str = ''
        is_float = False
        while (self.current is not None and (self.current in Consts.DIGITOS or self.current == ".")):
            if (self.current == "."):
                # Caso encontre dois pontos decimais
                if (is_float == True):
                    raise Exception("Erro: Numéro inválido")
                is_float = True
                
            num_str += self.current
            self.__advance()
            
        if (is_float == True):
            return Token(Consts.FLOAT, float(num_str))
            
        return Token(Consts.INT, int(num_str))

    def __make_boolean(self):
        if (self.code[self.index:self.index+4] == "True"):
            self.index += 4
            self.__advance()
            return Token(Consts.BOOLEAN, True)
        elif (self.code[self.index:self.index + 5] == "False"):
            self.index += 5
            self.__advance()
            return Token(Consts.BOOLEAN, False)
        
        return None

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
        # Palavra-Chave
        if (id_str in Consts.KEYS):
            return Token(id_str)
        # Palavra reservada
        elif (id_str in Consts.TIPOS or id_str == ("True" or "False")):
            return Token(id_str)
        # Genérico
        return Token("IDENTIFIER", id_str)
