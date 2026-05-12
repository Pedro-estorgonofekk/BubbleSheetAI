import os, time, qrcode, json 
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
    boxHeight = (totalQuestions * spaceYPerQuestion) + (35 + spaceYPerQuestion)

    x0 = x1 - boxWidth
    y1 = y0 + boxHeight

    return x0, y0, x1, y1


##Desenho do cabeçalho:
def DrawHeader(draw):
    draw.text([margin, 36], "Nome:", fill="black")
    draw.line([(margin + 55, 50), (width - margin, 50)], fill="black")


##Desenhar a caixa delimitadora:
def DrawBox(draw, x0, y0, x1, y1):

    draw.rectangle([(x0, y0), (x1, y1)], outline="black", width=2)

    return draw


##Desenhar as ancoras
def DrawAnchor(draw, x0, y0, x1, y1):

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
        draw.text([x0 + 15, startY + (q * spacingY) + 2], f"{q+1:02d}:", fill="black")
        for a in range(altsPerQuestion):
            x = startX + a * spacingX
            y = startY + q * spacingY
            draw.ellipse([(x, y), (x + bubbleSize, y + bubbleSize)],outline="black", width=2)


def WriteId(draw, testId):
    startY = height - 60
    draw.text([width / 2, startY], f"Prova: {testId}", fill="black", anchor="mm")


def DrawQRCode(img, testID, totalQuestions, altsPerQuestion, y0):
    data = {
        "testID": testID,
        "totalQuestions": totalQuestions,
        "altsPerQuestion": altsPerQuestion
    }
    
    json_string = json.dumps(data)

    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(json_string)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    qr_img = qr_img.resize((200, 200))

    pos_x = margin
    pos_y = y0
    
    img.paste(qr_img, (pos_x, pos_y))

##Gerar a imagem final
def SheetGeneration(testID, totalQuestions, altsPerQuestion):
    print(totalQuestions, altsPerQuestion)
    time.sleep(2)
    if totalQuestions <= 25 and altsPerQuestion <= 6:
        img = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(img)

        DrawHeader(draw)

        x0, y0, x1, y1 = CalculateBox(totalQuestions, altsPerQuestion)

        DrawBox(draw, x0, y0, x1, y1)
        DrawAnchor(draw, x0, y0, x1, y1)
        DrawAlternatives(draw, x0, y0, totalQuestions, altsPerQuestion)
        WriteId(draw, testID)
        DrawQRCode(img, testID, totalQuestions, altsPerQuestion, y0)

        path = f"../examples/{testID}.pdf"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        img.save(path, format="PDF")
        print(f"Gabarito salvo em: {path}")
        
        img.show()
        return path
    else:
        return "valores muito grande"