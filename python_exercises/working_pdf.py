from PyPDF2 import PdfFileReader, PdfWriter, PdfMerger
from pathlib import Path

# pdf_path = (
#         Path.home() /
#         "Fluent-Python.pdf"
# )

# pdf = PdfFileReader(str(pdf_path))
# output_path = Path.home() / "Fluent-Python.txt"
# with output_path.open(mode='w') as output_file:
#     output_file.write(
#         f"{pdf.documentInfo.title}\n"
#         f"Number of pages: {pdf.getNumPages()}\n\n"
#     )
#
#     for page in pdf.pages:
#         text = page.extractText()
#          output_file.write(text)

# print(pdf.getNumPages())
# print(pdf.documentInfo.title)
#
# first_page = pdf.getPage(3)
# print(first_page.extractText())

# Creat a new PDF file page

# pdf_writer = PdfWriter()
# pagez = pdf_writer.addBlankPage(width=72, height=72)
#
# with Path("blank.pdf").open(mode="wb") as outfile:
#     pdf_writer.write(outfile)

# Extracting a page from PDF File

# pdfpath = (
#     Path.home()/
#     "Fluent-Python.pdf"
# )
# input_pdf = PdfFileReader(str(pdfpath))
# f_page = input_pdf.getPage(10)
# pdfwritez = PdfWriter()
# pdfwritez.addPage(f_page)
# with Path("FirstPage.pdf").open(mode="wb") as out_file:
#     pdfwritez.write(out_file)

# Extracting from multiple pages
#
# pdfpath = (
#         Path.home() /
#         "Fluent-Python.pdf"
# )
#
# inputN = PdfFileReader(str(pdfpath))
# pdfWri = PdfWriter()
# for n in range(20, 31):
#     # using slice notation
#     # for n in inputN.pages[20 : 31]:
#     pagee = inputN.getPage(n)
#     pdfWri.addPage(pagee)
#
# print(pdfWri.getNumPages())
#
# with Path("Fluent-Python-Part.pfd").open(mode="wb") as output_filee:
#     pdfWri.write(output_filee)

# merge two or more files together

# pdf_merge = PdfMerger()
# report_dir = Path(
#     Path.home()/
#     "report"
# )
#
# for path in report_dir.glob("*.pdf"):
#     print(path.name)
# ordered_report = list(report_dir.glob("*.pdf"))
# ordered_report.sort()
#
# for path in ordered_report:
#     pdf_merge.append(str(path))
#
# with Path("data-structures.pdf").open(mode="wb") as fiilee:
#     pdf_merge.write(fiilee)

# encrypt a PDF file

pdf_path = Path.home() / "Fluent-Python.pdf"


# pdf_read = PdfFileReader(str(pdf_path))
# pdf_write = PdfWriter()
# pdf_write.appendPagesFromReader(pdf_read)
# pdf_write.encrypt(user_pwd="AsaFiles", owner_pwd="WeCanNowEdit")
#
# outPut_path = Path.home() / "Fluent-Python-Protected.pdf"
#
# with outPut_path.open(mode="wb") as output_file:
#     pdf_write.write(output_file)

# decrypting
pdf_path2 = Path.home() / "Fluent-Python-Protected.pdf"
pdf_reader = PdfFileReader(str(pdf_path2))
print(pdf_reader.decrypt("AsaFiles"))
print(pdf_reader.getPage(0))

from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
html_page = urlopen(url)
html_text = html_page.read().decode("utf-8")
print(html_text)