import os
from PyPDF2 import PdfReader, PdfWriter


def ren(fol):
   n=0
   for file in fol:
    tup=os.path.splitext(file)
    ex=tup[1]
    
    try:
    
        if ex==".pdf":
            os.rename(f"{fol}/{file}",f"{fol}/{n}{ex}")
            n+=1
    except FileExistsError:
        n=n+1


while True:
  print("welcome to PDF Merger".center(150))

  fol=input("Enter the name or path of the folder :".capitalize())
  output_fol=input("Write the name of output PDF")

  if  os.path.exists(fol):
      
      folder=os.listdir(fol)
    #   ren wil rename the pdf files in the folder number wise
      ren(fol)
    # adding pdfs
      pdf_writer = PdfWriter()
      for pdf_file in folder:
        reader =  PdfReader(open(f"{fol}/{pdf_file}", "rb"))
        for page in reader.pages:
            pdf_writer.add_page(page)
    # making mergered pdf
      with open(f'output/{output_fol}.pdf', 'wb') as output_file:
        pdf_writer.write(output_file)
      print("TASK COMPLETED SUCCESFULL")


  else:
    print("Folder does not exists")
    break

