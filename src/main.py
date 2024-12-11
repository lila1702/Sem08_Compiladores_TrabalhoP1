# main.py
from lexer import Lexer

if __name__ == "__main__":
    test1 = '''
    personagem "Aragorn" {
        classe: "Guerreiro";
        nivel: 5;
        atributos: "forca" 18, "destreza" 14, "constituicao" 16;
    }
    '''
    
    test2 = '''
    item "Espada Longa" {
        descricao: "Uma espada de ferro com lâmina de 70cm bilateral";
        tipo: "arma";
    }
    '''
    
    test3 = '''
    personagem "Eleonora" {
        classe: "Ladina";
        nivel: 2;
        atributos: "forca" 11, "destreza" 17, "constituicao" 14, "inteligencia" 16;
    }
    
    cenario "Floresta amaldiçoada" {
        descricao: "Um canteiro cheio de árvores, escuro e com uma aura sombria, pesada, parecendo que alguém está perto";
        localizacao: "Continente de Eberron";
    }
    '''
    
    lexer = Lexer(test3)
    
    try:
        tokens = lexer.make_tokens()
        for token in tokens:
            print(token)
    except Exception as e:
        print(e)
