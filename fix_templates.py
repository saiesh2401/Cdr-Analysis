from docx import Document

def replace_text(doc_path, old_text, new_text):
    doc = Document(doc_path)
    count = 0
    for p in doc.paragraphs:
        if old_text in p.text:
            p.text = p.text.replace(old_text, new_text)
            count += 1
    doc.save(doc_path)
    print(f"Replaced {count} occurrences in {doc_path}")

print("--- Fixing Templates ---")
replace_text("JIO Template.docx", "Airtel", "Reliance Jio Infocomm Ltd.")
replace_text("VI Template.docx", "Airtel", "Vodafone Idea Ltd.")
