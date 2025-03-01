import os
from pathlib import Path
from collections import defaultdict

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

def process_category(category_path):
    """Process all PDFs in a category folder and return accuracy stats."""
    pdf_files = list(Path(category_path).glob("*.pdf"))
    category_stats = {
        'total_files': len(pdf_files),
        'successful_extractions': 0,
        'failed_extractions': 0,
        'accuracies': [],
        'average_accuracy': 0.0
    }
    
    for pdf_file in pdf_files:
        extracted_text, accuracy = extract_text_from_pdf(pdf_file)
        
        if extracted_text:
            category_stats['successful_extractions'] += 1
            category_stats['accuracies'].append(accuracy)
        else:
            category_stats['failed_extractions'] += 1
    
    if category_stats['accuracies']:
        category_stats['average_accuracy'] = sum(category_stats['accuracies']) / len(category_stats['accuracies'])
    
    return category_stats

def analyze_resume_categories(data_path):
    """Analyze all categories in the dataset."""
    results = {}
    
    # Process each category folder
    for category_folder in Path(data_path).iterdir():
        if category_folder.is_dir():
            category_name = category_folder.name
            print(f"\nProcessing category: {category_name}")
            print("-" * 50)
            
            results[category_name] = process_category(category_folder)
            
            # Print category summary
            stats = results[category_name]
            print(f"Files processed: {stats['total_files']}")
            print(f"Successful extractions: {stats['successful_extractions']}")
            print(f"Failed extractions: {stats['failed_extractions']}")
            print(f"Average accuracy: {stats['average_accuracy']:.2f}%")
    
    return results

def print_overall_summary(results):
    """Print overall summary of all categories."""
    print("\n=== OVERALL SUMMARY ===")
    print("-" * 50)
    
    # Calculate overall statistics
    total_files = sum(cat['total_files'] for cat in results.values())
    total_successful = sum(cat['successful_extractions'] for cat in results.values())
    total_failed = sum(cat['failed_extractions'] for cat in results.values())
    
    # Sort categories by average accuracy
    sorted_categories = sorted(
        results.items(),
        key=lambda x: x[1]['average_accuracy'],
        reverse=True
    )
    
    # Print overall stats
    print(f"Total files processed: {total_files}")
    print(f"Total successful extractions: {total_successful}")
    print(f"Total failed extractions: {total_failed}")
    
    print("\nCategory Rankings by Accuracy:")
    print("-" * 50)
    for category, stats in sorted_categories:
        print(f"{category}: {stats['average_accuracy']:.2f}%")

if __name__ == "__main__":
    data_path = "data"  # Path to the categories folder
    results = analyze_resume_categories(data_path)
    print_overall_summary(results)
