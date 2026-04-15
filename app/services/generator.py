import os
from PIL import Image, ImageDraw

##Altura e largura
width, height = 800, 1131
margin = 40

##Calculo da altura entre as caixas
def CalculateBox(totalQuestions, altsPerQuestion):
    spaceYPerQuestion = 35
    spaceXPerQuestion = 40
    spaceTextLeft = 60

    x1 = width - margin
    y0 = 150

    boxWidth = spaceTextLeft + (altsPerQuestion * spaceXPerQuestion)
    boxHeight = totalQuestions * spaceYPerQuestion

    x0 = x1 - boxWidth
    y1 = y0 + boxHeight

    return x0, x1, y0, y1


##Desenho do cabeçalho:
def DrawHeader(draw):
    draw.line([(margin, 50), (width - margin, 50)], fill="black")
    draw.text([margin, 60], "Nome:", fill="black")


##Desenhar a caixa delimitadora:
def DrawBox(draw, x0, x1, y0, y1):

    draw.rectangle([(x0, y0), (x1, y1)], outline="black", width=2)

    return draw


##Desenhar as ancoras
def DrawAnchor(draw, x0, x1, y0, y1):

    ##Variaveis para o desenho (q era pra faciliar)
    size = 30

    ##Desenha a caixa para a facilitação do reconhecimento
    ##Caixa superior esquerda
    draw.rectangle([(x0, y0), (x0 + size, y0 + size)], fill="black")

    ##Caixa superior direita, será fixa
    draw.rectangle([(x1 - size, y0), (x1, y0 + size)], fill="black")

    ##Caixa inferior esquerda
    draw.rectangle([(x0, y1 - size), (x0 + size, y1)], fill="black")

    ##Caixa inferior direita
    draw.rectangle([(x1 - size, y1 - size), (x1, y1)], fill="black")


##Desenha as bolhas das alternativas
def DrawAlternatives(draw, x0, y0, totalQuestions, altsPerQuestion):
    startX, startY = x0 + 60, y0 + 35 
    spacingX, spacingY = 40, 35
    bubbleSize = 20  

    for q in range(totalQuestions):
        for a in range(altsPerQuestion):
            x = startX + a * spacingX
            y = startY + q * spacingY
            draw.ellipse([(x, y), (x + bubbleSize, y + bubbleSize)],outline="black", width=2)


def WriteId(draw, testId):
    startY = height - 60
    draw.text([width / 2, startY], f"Prova: {testId}", fill="black", anchor="mm")


##Salvar a imagem


##Gerar a imagem final
def SheetGeneration(testID, totalQuestions, altsPerQuestion):
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    # 2. Desenha o cabeçalho
    DrawHeader(draw)

    # 3. Calcula a matemática da caixa (A mágica da responsividade)
    x0, y0, x1, y1 = CalculateBox(totalQuestions, altsPerQuestion)

    # 4. Manda os operários desenharem passando as coordenadas
    DrawBox(draw, x0, y0, x1, y1)
    DrawAnchor(draw, x0, y0, x1, y1)
    DrawAlternatives(draw, x0, y0, totalQuestions, altsPerQuestion)
    WriteId(draw, testID)

    # 5. Salva a imagem
    path = f"../examples/{testID}.png"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, format="PNG")
    print(f"Gabarito salvo em: {path}")
    
    img.show()
    return path