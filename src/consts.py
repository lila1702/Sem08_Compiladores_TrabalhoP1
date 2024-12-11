import string

class Consts:
    # Tokens
    DIGITOS = '0123456789'
    LETRAS = string.ascii_letters
    LETRAS_DIGITOS = DIGITOS + LETRAS

    PERSONAGEM = 'personagem'
    CENARIO    = 'cenario'
    ACAO       = 'acao'
    ITEM       = 'item'

    # Símbolos utilizados
    LBRACE     = '{'
    RBRACE     = '}'
    COLON      = ':'
    SEMICOLON  = ';'
    COMMA      = ','
    STRING     = 'STRING'
    INT        = 'INT'

    EOF       = '$EOF'

    # Palavras reservadas
    KEYS = [
        PERSONAGEM,
        CENARIO,
        ACAO,
        ITEM
    ]