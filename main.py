from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

filepaths=glob.glob('invoices/*.xlsx')
for i in filepaths:
    df=pd.read_excel(i,sheet_name="Sheet 1")
    print(df)
for i in filepaths:
    filename=Path(i).stem
    files=filename.split("-")
    df=pd.read_excel(i,sheet_name="Sheet 1")
    pdf=FPDF(orientation="L",
             unit="mm",
             format="A4")
    pdf.set_font(family="Times",style="B",size=25)
    pdf.add_page()
    pdf.cell(w=0,h=0,txt="Tax Invoice - "+files[0],border=0,align="L",ln=1)
    pdf.cell(w=0,h=20,txt="Date - "+files[1],border=0,align="L")



    pdf.output(f"pdfs/{files[0]}.pdf")