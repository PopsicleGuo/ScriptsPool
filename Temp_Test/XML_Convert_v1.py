import os, sys
import xml.etree.ElementTree as ET
import pandas as pd
import xlsxwriter
from datetime import datetime


def initial_xmldata_pdformat(xml):
    xmlfile = xml
    if not os.path.exists(xmlfile):
        print("Error")
        return

    tree = ET.parse(xmlfile)
    root = tree.getroot()

    dic = {}

    # for child in root:
    #     for element in child:
    #         if not element.tag in dic.keys():
    #             dic[element.tag] = []
    #
    #         if element.tag == 'minDistance':
    #             dic[element.tag].append(float(element.text))
    #         else:
    #             dic[element.tag].append(element.text)

    # A Iterator which is using index to go through all elements
    for i in range(len(root)):
        for subindex in range(len(root[i])):
            if not root[i][subindex].tag in dic.keys():#Initial key's value as a list
                dic[root[i][subindex].tag] = []

            if root[i][subindex].tag == 'minDistance':
                dic[root[i][subindex].tag].append(float(root[i][subindex].text))
            elif subindex >= 3:
                dic[root[i][subindex].tag].append(int(root[i][subindex].text))
            else:
                dic[root[i][subindex].tag].append(root[i][subindex].text)

    return dic


def xmlwriter(xml, name):
    df = pd.DataFrame(initial_xmldata_pdformat(xml))
    exname = name + '_' + datetime.now().strftime("%Y%m%d%H%M%S") + '.xlsx'

    writer = pd.ExcelWriter(exname, engine='xlsxwriter')

    df.to_excel(writer, sheet_name='Sheet1')

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']


    header_format = workbook.add_format({
    'bold': True,
    'text_wrap': True,
    'valign': 'vcenter',
    'align': 'center',
    'fg_color': '#D7E4BC',
    'border': 1})


    for col_num, value in enumerate(df):
        worksheet.write(0, col_num+1, value, header_format)

    writer.save()


if __name__ == "__main__":
    xml = str(sys.argv[1])
    excel = str(sys.argv[2])

    xmlwriter(xml, excel)
    print('The file has been converted!!')
