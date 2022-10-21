from models.Writer import Writer
from models.Pen import Pen

writer = Writer('Little John')
pen = Pen('Bic')

print(f'Writer Name: {writer.name}')
print(f'Pen Brand: {pen.brand}')

writer.tool = pen
writer.tool.write()
