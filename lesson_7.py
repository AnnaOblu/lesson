import datetime
import csv
import json

from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage


def get_context(auto, power, year):
    return {
        'auto': auto,
        'power': power,
        'year': year,
    }


def from_template(auto, power, year, template, signature):
    template = DocxTemplate(template)
    context = get_context(auto, power, year)

    img_size = Cm(15)
    foto = InlineImage(template, signature, img_size)

    context['foto'] = foto
    template.render(context)

    template.save(auto + '_' + str(datetime.datetime.now().date()) + '_new.docx')


def generate_report(auto, power, year):
    template = 'doc_auto.docx'
    signature = 'foto.jpg'
    document = from_template(auto, power, year, template, signature)


generate_report('Subaru Baja', '177', '2002')

list_1 = [['auto', 'power', 'year'],['Subaru Baja', '177', '2002']]

with open('auto.csv', 'w') as f:
    writer = csv.writer(f, delimiter = '*')
    writer.writerows(list_1)

with open('auto.csv') as m:
    reader = csv.reader(m, delimiter = '*')
    for row in reader:
        print(row)

dict = {'auto': 'Subaru Baja', 'power': '177', 'year': '2002'}

with open('dict_to_json.txt', 'w') as f:
    json.dump(dict, f)

with open('dict_to_json.txt') as f:
    data = json.load(f)
    print(data)