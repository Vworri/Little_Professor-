from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from memory_profiler import profile

class extract_text(object):
    def __init__(self):
        text = self.convert("AHistoryOfTheUnitedStatesVol2.pdf")
        with open("testFile.txt", "w+") as f:
            f.write(text)
    def convert(self,fname, pages=None):
        text = ""
        ifp = open(fname, 'rb')
        parser = PDFParser(ifp)
        doc = PDFDocument()
        parser.set_document(doc)
        doc.set_parser(parser)
        doc.initialize('')
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # Process each page contained in the document.
        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for lt_obj in layout:
                if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                    text += lt_obj.get_text()
        return text

if "__main__"==__name__:
    extract_text()