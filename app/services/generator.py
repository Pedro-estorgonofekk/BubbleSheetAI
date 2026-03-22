import os
from PIL import Image, ImageDraw

##Geração da Imagem inicial
def Img():
    ##Variaveis pro desenho
    width, height = 800, 1131
    color = "white"

    ##Imagem A4 em branco
    img = Image.new("RGB", (width, height), color)
    draw = ImageDraw.Draw(img)

    return draw, img

##Calculo da altura entre as caixas 
def BoxHeight():
    print("Calcular altura entre caixas")

##Desenhar as caixas
def DrawBox():
    draw, img = Img()
    
    ##Desenha a caixa para a facilitação do reconhecimento
    ##Caixa superior esquerda
    draw.rectangle([50, 50, 80, 80], fill="Black")

    ##Caixa superior direita
    draw.rectangle([720, 50, 750, 80], fill="Black")

    ##Caixa inferior esquerda
    draw.rectangle([50, 1051, 80, 1081], fill="Black")

    ##Caixa inferior direita
    draw.rectangle([720, 1051, 750, 1081], fill="Black")

    img.show()
    
    ##Exportar a img
    return img

##Salvar a imagem
def SaveImg(testID):
    ##Importar Imagem
    finalImg = DrawBox()
    path = f"../examples/{testID}.png"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    finalImg.save(path, format="PNG")
    print(f"Gabarito salvo em: {path}")
    return path

##Gerar a imagem final
def SheetGeneration(totalQuestions,testID):
    SaveImg(testID)
