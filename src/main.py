from os import path
from lexer import Lexer

if __name__ == "__main__":
    filename = 0
    
    while (filename != "q"):
    
        filename = input("Digite o nome do arquivo de teste desejado: ")
        if (filename == "q"):
            quit()
        elif (not filename.endswith(".txt")):
            filename = filename + ".txt"
            
        file_path = path.abspath(path.join(path.dirname(__file__), "tests", filename))
        try:
            with open(file_path, 'r') as f:
                test_file = f.read()
                print(test_file)
                print("--------------")
            
            lexer = Lexer(test_file)
            tokens = lexer.make_tokens()
            for token in tokens:
                print(token)
                
        except FileNotFoundError:
            print(f"Arquivo {filename} não foi encontrado no diretório de testes.")
            
        except Exception as e:
            print(e)
