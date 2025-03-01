import os
from pathlib import Path

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    try:
        # Open the PDF file
        doc = fitz.open(pdf_path)
        
        # Initialize text variable
        text = ""
        
        # Extract text from each page
        total_words = 0
        successfully_extracted_words = 0
        
        for page in doc:
            # Extract text from current page
            page_text = page.get_text()
            text += page_text
            
            # Count words for basic accuracy estimation
            words_in_page = len(page_text.split())
            total_words += words_in_page
            
            # Count successfully extracted words (non-empty)
            successfully_extracted_words += len([w for w in page_text.split() if w.strip()])
        
        # Calculate basic accuracy (rough estimation)
        accuracy = (successfully_extracted_words / total_words * 100) if total_words > 0 else 0
        
        return text, accuracy
        
    except Exception as e:
        print(f"Error processing {pdf_path}: {str(e)}")
        return None, 0
    finally:
        if 'doc' in locals():
            doc.close()

def process_resume_folder(folder_path):
    # Get all PDF files in the folder
    pdf_files = list(Path(folder_path).glob("*.pdf"))
    
    for pdf_file in pdf_files:
        print(f"\nProcessing: {pdf_file.name}")
        print("-" * 50)
        
        # Extract text and get accuracy
        extracted_text, accuracy = extract_text_from_pdf(pdf_file)
        
        if extracted_text:
            print(f"Extraction Accuracy: {accuracy:.2f}%")
            print("\nExtracted Text:")
            print("-" * 50)
            print(extracted_text)  # Print full text without truncation
        else:
            print("Failed to extract text from this file")

if __name__ == "__main__":
    # Use relative path for resume folder
    resume_folder = "resume"  # Folder containing PDF files
    process_resume_folder(resume_folder)