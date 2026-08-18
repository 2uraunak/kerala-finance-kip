import os

# Create dummy PDFs so the pipeline doesn't crash if the user doesn't provide real ones
# We'll just create a text file for now, since installing PDF libraries might fail
# But wait, pdfplumber will crash on invalid PDFs. Let's create a minimal valid PDF manually.

def create_minimal_pdf(filename, text):
    content = f"""%PDF-1.1
%¥±ë
1 0 obj
  << /Type /Catalog
     /Pages 2 0 R
  >>
endobj
2 0 obj
  << /Type /Pages
     /Kids [3 0 R]
     /Count 1
     /MediaBox [0 0 595.28 841.89]
  >>
endobj
3 0 obj
  <<  /Type /Page
      /Parent 2 0 R
      /Resources
       << /Font
           << /F1
               << /Type /Font
                  /Subtype /Type1
                  /BaseFont /Helvetica
               >>
           >>
       >>
      /Contents 4 0 R
  >>
endobj
4 0 obj
  << /Length 55 >>
stream
  BT
    /F1 18 Tf
    0 800 Td
    ({text}) Tj
  ET
endstream
endobj
xref
0 5
0000000000 65535 f 
0000000018 00000 n 
0000000077 00000 n 
0000000178 00000 n 
0000000457 00000 n 
trailer
  <<  /Root 1 0 R
      /Size 5
  >>
startxref
565
%%EOF
"""
    with open(filename, 'wb') as f:
        f.write(content.encode('utf-8'))

os.makedirs('data/sample_documents', exist_ok=True)
create_minimal_pdf('data/sample_documents/GO_Ms_No_45_2023.pdf', 'Government Order 45/2023: Dearness Allowance Revision')
create_minimal_pdf('data/sample_documents/GO_Ms_No_45_2023_SUPERSEDED.pdf', 'Government Order 45/2023 (SUPERSEDED): Dearness Allowance')
create_minimal_pdf('data/sample_documents/GST_Circular_2024.pdf', 'GST Circular 2024: Compliance Measures')
create_minimal_pdf('data/sample_documents/Budget_2024_25.pdf', 'Kerala State Budget 2024-25')

print("Minimal PDFs created successfully.")
