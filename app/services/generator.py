import os
from PIL import Image, ImageDraw, ImageFont

##Altura e largura
width, height = 800, 1131


##Geração da Imagem inicial
def Img():

    ##Imagem A4 em branco
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    return draw, img


##Calculo da altura entre as caixas, ela sera definida com base no numero de questões
def BoxHeight(totalQuestions):
    alternativesSpace = 35 # pixels por linha
    upperPadding = 150

    boxHeight = upperPadding + (totalQuestions * alternativesSpace)

    return boxHeight


##Calculo da largura entre as caixas, ela sera definida com base no numero de alternativas
def BoxWidth():
    return

##Desenhar a linha
def DrawLine():
    draw, img, _, _  = Img()
    draw.line([(40, 50), (760, 50)], fill="Black")

    return draw, img


##Desenhar a caixa delimitadora:
def DrawBox():
    draw, img = DrawLine()

    ##Essas coords serão substituidas por variaveis igual à função abaixo, para poder ajudar na responsividade
    draw.rectangle([(50, 50), (750, 1081)], outline="black", width=2)

    return draw, img


##Desenhar as ancoras
def DrawAnchor():

    ##Variaveis para o desenho (q era pra faciliar)
    draw, img = DrawBox()
    _, _, width, height = Img() 
    padding = 40
    size = 30

    ##Desenha a caixa para a facilitação do reconhecimento
    ##Caixa superior esquerda
    draw.rectangle([(padding), (padding), (padding + size), (padding + size)], fill="black")

    ##Caixa superior direita, será fixa
    draw.rectangle([730, 80, 760, 110], fill="black")

    ##Caixa inferior esquerda
    draw.rectangle([(padding), (height - padding - size), (padding + size), (height - padding)], fill="black")

    ##Caixa inferior direita
    draw.rectangle([(width - padding - size), height - (padding + size), (width - padding), (height - padding)], fill="black")

    
    ##Exportar a img
    return draw, img


##Desenha as bolhas das alternativas
def DrawAlternatives(totalQuestions, altsPerQuestion):
    draw, img = DrawAnchor()

    startX, startY = 100, 200
    spacingX, spacingY = 40, 35
    bubbleSize = 20

    for q in range(totalQuestions):
        for a in range(altsPerQuestion):
            x = startX + a * spacingX
            y = startY + q * spacingY
            draw.ellipse([(x, y), (x + bubbleSize, y + bubbleSize)],outline="black", width=2)

    return draw, img



def WriteId(testId, altsPerQuestion, totalQuestions):
    draw, img = DrawAlternatives(totalQuestions, altsPerQuestion)
    
    font = ImageFont.truetype("arial.ttf", 14)
    bbox = draw.textbbox([0, 0], testId, font=font)
    txtWidth = bbox[2] - bbox[0]

    cordX = (800 - txtWidth) / 2
    cordY = (1131 - 40)


    draw.text([cordX, cordY], testId, font=font, fill="black",)

    return img


##Salvar a imagem
def SaveImg(testID, totalQuestions, altsPerQuestion):

    ##Importar Imagem
    finalImg = WriteId(testID, altsPerQuestion, totalQuestions)
    path = f"../examples/{testID}.png"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    finalImg.show()
    
    finalImg.save(path, format="PNG")
    print(f"Gabarito salvo em: {path}")
    return path


##Gerar a imagem final
def SheetGeneration(testID, totalQuestions, altsPerQuestion):
    path = SaveImg(testID, totalQuestions, altsPerQuestion)

    return path