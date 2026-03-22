import os
from PIL import Image, ImageDraw

def GerarGabarito(testID):
    ##Variaveis pro desenho
    width, height = 800, 1131
    color = "white"

    ##Imagem A4 em branco
    img = Image.new("RGB", (width, height), color)
    draw = ImageDraw.Draw(img)

    ##Desenha linha
    draw.line([(40, 50), (760, 50)], fill="Black")


    ##Salvar a img
    path = f"../examples/{testID}.png"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    img.save(path, format="PNG")
    print(f"Gabarito salvo em: {path}")

    return path
