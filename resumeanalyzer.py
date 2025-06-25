import fitz  # PyMuPDF
import sys
import os

# Define important skill keywords
KEY_SKILLS = [
    "Python", "Java", "C++", "SQL", "Machine Learning", "Deep Learning",
    "NLP", "Pandas", "NumPy", "TensorFlow", "PyTorch", "Scikit-learn",
    "Data Analysis", "Data Visualization", "Excel", "Power BI", "Tableau"
]

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
    except Exception as e:
        print(f"❌ Error reading PDF: {e}")
    return text

def count_keywords(text, keywords):
    counts = {}
    for skill in keywords:
        count = text.lower().count(skill.lower())
        counts[skill] = count
    return counts

def suggest_improvements(counts):
    suggestions = [skill for skill, count in counts.items() if count == 0]
    if suggestions:
        print("\n🔍 Suggested Improvements (Missing Skills):")
        for skill in suggestions:
            print(f" - Consider adding: {skill}")
    else:
        print("\n✅ Great! All key skills are mentioned.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python resume_analyzer.py <your_resume.pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]

    if not os.path.isfile(pdf_path):
        print("❌ File does not exist.")
        sys.exit(1)

    print(f"📄 Analyzing: {pdf_path}")
    text = extract_text_from_pdf(pdf_path)

    if not text.strip():
        print("❌ No text extracted. Make sure your resume is not scanned or image-based.")
        sys.exit(1)

    print("\n🧠 Skill Mentions:")
    keyword_counts = count_keywords(text, KEY_SKILLS)
    for skill, count in keyword_counts.items():
        print(f" - {skill}: {count}")

    suggest_improvements(keyword_counts)

if __name__ == "__main__":
    main()
