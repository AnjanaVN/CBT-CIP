from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_receipt(ereceipt, transaction_details):
    # PDF canvas creation here
    pdf = canvas.Canvas(ereceipt, pagesize=letter)
    pdf.setTitle("Transaction Receipt")

    # font setting
    pdf.setFont("Times-Roman-Bold", 16)
    pdf.drawString(200, 750, "Transaction Receipt")

    pdf.setFont("Times-Roman", 12)
    line = 700

    # details of transaction
    for key, value in transaction_details.items():
        pdf.drawString(50, line, f"{key}: {value}")
        line -= 20

    pdf.setFont("Helvetica-Oblique", 10)
    pdf.drawString(50, line - 20, "Thank you for your purchase!")

    # to save pdf
    pdf.save()
    print(f"Receipt saved as {ereceipt}")


# eg:transaction receipt
if __name__ == "__main__":
    transaction_details = {
        "Transaction ID": "67858556470",
        "Date": "2025-01-25",
        "Customer Name": "Shilpa S",
        "Amount": "$120.00",
        "Payment Method": "Debit Card",
        "Store Name": "Gadget Store",
        "Address": "Kochi,Kerala, India"
    }
    generate_receipt("transaction_receipt2.pdf", transaction_details)