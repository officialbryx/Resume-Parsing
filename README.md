# Resume PDF Extraction Analysis

This project analyzes the text extraction accuracy from PDF resumes across different job categories.

## Dataset Overview
- Total Resumes Processed: 2,484
- Successful Extractions: 2,483
- Failed Extractions: 1
- Overall Success Rate: 99.96%

## Category-wise Statistics

| Category | Files Processed | Success Rate | Avg. Accuracy |
|----------|----------------|--------------|---------------|
| Information Technology | 120 | 100% | 100% |
| Business Development | 120 | 99.17% | 100% |
| Accountant | 118 | 100% | 100% |
| Advocate | 118 | 100% | 100% |
| Engineering | 118 | 100% | 100% |
| Finance | 118 | 100% | 100% |
| Chef | 118 | 100% | 100% |
| Aviation | 117 | 100% | 100% |
| Fitness | 117 | 100% | 100% |
| Sales | 116 | 100% | 100% |
| Banking | 115 | 100% | 100% |
| Consultant | 115 | 100% | 100% |
| Healthcare | 115 | 100% | 100% |
| Construction | 112 | 100% | 100% |
| Public Relations | 111 | 100% | 100% |
| HR | 110 | 100% | 100% |
| Designer | 107 | 100% | 100% |
| Arts | 103 | 100% | 100% |
| Teacher | 102 | 100% | 100% |
| Apparel | 97 | 100% | 100% |
| Digital Media | 96 | 100% | 100% |
| Agriculture | 63 | 100% | 100% |
| Automobile | 36 | 100% | 100% |
| BPO | 22 | 100% | 100% |

## Key Findings
1. Nearly perfect extraction rate across all categories (99.96%)
2. Only 1 failed extraction out of 2,484 files (in Business Development category)
3. Consistent 100% accuracy in text extraction across all successful attempts
4. Largest categories (120 files each):
   - Information Technology
   - Business Development
5. Smallest categories:
   - BPO (22 files)
   - Automobile (36 files)

## Technical Details
- Used PyMuPDF (fitz) for PDF text extraction
- Accuracy measurement based on successful word extraction ratio
- Analysis includes 24 different job categories
