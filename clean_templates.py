from docx import Document

def clean_doc(path):
    doc = Document(path)
    header_text = "OFFICE OF THE CYBER CRIME UNIT"
    
    # 1. Find the element where the 2nd letter starts
    second_header_element = None
    count = 0
    
    for p in doc.paragraphs:
        if header_text in p.text:
            count += 1
            if count == 2:
                second_header_element = p._element
                break
    
    if not second_header_element:
        print(f"Skipping {path}: Less than 2 headers found.")
        return

    # 2. Iterate and Remove
    body = doc.element.body
    children = list(body) # Snapshot
    start_deleting = False
    
    deleted_count = 0
    for child in children:
        if child == second_header_element:
            start_deleting = True
        
        if start_deleting:
            body.remove(child)
            deleted_count += 1
            
    doc.save(path)
    print(f"Cleaned {path}: Removed {deleted_count} elements (pages 2+).")

files = ["JIO Template.docx", "Airtel Template.docx", "VI Template.docx"]
print("--- Truncating Templates ---")
for f in files:
    try:
        clean_doc(f)
    except Exception as e:
        print(f"Error cleaning {f}: {e}")
