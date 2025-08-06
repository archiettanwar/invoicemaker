from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

filepaths=glob.glob('invoices/*.xlsx')
for i in filepaths:
    df=pd.read_excel(i,sheet_name="Sheet 1")

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
    pdf.cell(w=0,h=20,txt="Date - "+files[1],border=0,align="L",ln=2)

    df=pd.read_excel(i,sheet_name="Sheet 1")
    col=df.columns
    col=[(i.replace("_"," ")).title() for i in col]
    pdf.set_font(family="Times", style="B", size=10)
    pdf.cell(w=30, h=8, txt=col[0], border=1)
    pdf.cell(w=70, h=8, txt=col[1], border=1)
    pdf.cell(w=40, h=8, txt=col[2], border=1)
    pdf.cell(w=30, h=8, txt=col[3], border=1)
    pdf.cell(w=30, h=8, txt=col[4], border=1, ln=1)

    for index,rows in df.iterrows():
        pdf.set_font(family="Times", style="B", size=10)
        pdf.cell(w=30, h=8, txt=str(rows["product_id"]),border=1)
        pdf.cell(w=70, h=8, txt=str(rows["product_name"]), border=1)
        pdf.cell(w=40, h=8, txt=str(rows["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(rows["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(rows["total_price"]), border=1,ln=1)

    total_sum=df["total_price"].sum()
    pdf.set_font(family="Times", style="B", size=10)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=40, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=f"{total_sum}", border=1, ln=1)

    pdf.set_font(family="Times", style="B", size=10)
    pdf.cell(w=0,h=8,txt=f"The total sum is {total_sum}",ln=1)

    pdf.set_font(family="Times", style="B", size=15)
    pdf.cell(w=30,h=8,txt="Python How",border=0)
    pdf.image("pythonhow.png",w=10)



    pdf.output(f"pdfs/{files[0]}.pdf")