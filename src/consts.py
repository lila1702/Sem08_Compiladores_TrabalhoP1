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
    VARIAVEL   = 'variavel'
    ESCOLHA    = 'escolha'
    OPCAO      = 'opcao'
    CONDICAO   = 'condicao' 
    # Símbolos utilizados
    LBRACE     = '{'
    RBRACE     = '}'
    COLON      = ':'
    SEMICOLON  = ';'
    COMMA      = ','
    STRING     = 'STRING'
    INT        = 'INT'
    FLOAT      = 'FLOAT'
    BOOLEAN    = 'BOOLEAN'
    ASSIGN     = '='
    EOF       = '$EOF'
    
    # Para comparações
    IGUAL      = '=='
    DIFERENTE  = '!='
    MENOR      = '<'
    MAIOR      = '>'
    MENORIGUAL = '<='
    MAIORIGUAL = '>='   
    # Palavras reservadas
    KEYS = [
        PERSONAGEM,
        CENARIO,
        ACAO,
        ITEM,
        VARIAVEL,
        ESCOLHA,
        OPCAO,
        CONDICAO
    ]
    
    # Tipos suportados para as variáveis
    TIPOS = [
        STRING,
        INT,
        FLOAT,
        BOOLEAN
    ]