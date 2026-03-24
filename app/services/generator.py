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

    return draw, img, width, height


##Calculo da altura entre as caixas 
def BoxHeight(totalQuestions):
    
    return totalQuestions


##Desenhar a linha
def DrawLine():
    draw, img, _, _  = Img()
    draw.line([(40, 50), (760, 50)], fill="Black")

    return draw, img


##Desenhar as caixas
def DrawBox():

    ##Variaveis para o desenho (q era pra faciliar)
    draw, img = DrawLine()
    _, _, width, height = Img() 
    padding = 50
    size = 30

    ##Desenha a caixa para a facilitação do reconhecimento
    ##Caixa superior esquerda
    draw.rectangle([(padding), (padding), (padding + size), (padding + size)], fill="black")

    ##Caixa superior direita
    draw.rectangle([(width - padding - size), (padding), (width - padding), (padding + size)], fill="black")

    ##Caixa inferior esquerda
    draw.rectangle([(padding), (height - padding - size), (padding + size), (height - padding)], fill="black")

    ##Caixa inferior direita
    draw.rectangle([(width - padding - size), height - (padding + size), (width - padding), (height - padding)], fill="black")

    img.show()
    
    ##Exportar a img
    return img


##Salvar a imagem
def SaveImg(testID, totalQuestions):

    ##Importar Imagem
    finalImg = DrawBox()
    path = f"../examples/{testID}.png"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    finalImg.save(path, format="PNG")
    print(f"Gabarito salvo em: {path}")
    return path


##Gerar a imagem final
def SheetGeneration(testID, totalQuestions):
    path = SaveImg(testID, totalQuestions)

    return path