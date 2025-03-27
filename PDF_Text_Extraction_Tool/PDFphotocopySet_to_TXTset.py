import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import os

custom_config = r'--oem 1 --psm 6'


def extract_text_from_image_pdf(pdf_path, output_txt_path):
    try:
        doc = fitz.open(pdf_path)
        extracted_text = ""

        for page_num in range(len(doc)):
            # Render page to an image
            page = doc[page_num]
            pix = page.get_pixmap(dpi=300)
            img = Image.open(io.BytesIO(pix.tobytes("png")))
            img = img.convert("L")

            # Use Tesseract OCR to extract text from the image
            text = pytesseract.image_to_string(img, lang="eng", config=custom_config)
            extracted_text += f"\n--- Page {page_num + 1} ---\n{text}"

        # Save the text to a file
        with open(output_txt_path, "w", encoding="utf-8") as text_file:
            text_file.write(extracted_text)

        print(f"Text extracted and saved to {output_txt_path}")
    except Exception as e:
        print(f"An error occurred with {pdf_path}: {e}")

def process_pdf_directory(input_dir, output_dir):
    try:
        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)
        dirLen = str(len(os.listdir(input_dir)))
        # Process each PDF in the input directory
        for fileNum, file_name in enumerate(os.listdir(input_dir)):
            if file_name.endswith(".pdf"):
                pdf_path = os.path.join(input_dir, file_name)
                output_txt_path = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}.txt")
                #Process file if not already processed
                if not os.path.exists(output_txt_path):
                    print(f"Processing: {file_name} ({str(fileNum + 1)} of {dirLen})")
                    extract_text_from_image_pdf(pdf_path, output_txt_path)
                else:
                    print(f"{file_name} allready processed...Moving on")

        print("All PDFs have been processed.")
    except Exception as e:
        print(f"An error occurred while processing the directory: {e}")

# Example usage
input_directory = os.path.join(os.getcwd(), "pdfs")  # Replace with your input folder path
output_directory = os.path.join(os.getcwd(), "output")  # Replace with your output folder path
process_pdf_directory(input_directory, output_directory)
