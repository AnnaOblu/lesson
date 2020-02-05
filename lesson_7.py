import datetime

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
