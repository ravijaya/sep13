#!/usr/bin/env python
import subprocess
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from pprint import pprint as pp


def disk_report():
    p = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
    return p.stdout.readlines()


def create_pdf(input, output="disk_report.pdf"):
    now = datetime.datetime.today()
    date = now.strftime("%h %d %Y %H:%M:%S")
    c = canvas.Canvas(output)
    textobject = c.beginText()
    textobject.setTextOrigin(inch, 11 * inch)

    textobject.textLines('''Disk Capacity Report: {}'''.format(date))

    for line in input:
        textobject.textLine(line.strip())

    c.drawText(textobject)
    c.showPage()
    c.save()


if __name__ == '__main__':
    report = disk_report()
    # pp(report)
    create_pdf(report)
