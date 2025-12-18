from backend import ISPProcessor
import os

def simulate_gui_run():
    print("--- Simulating GUI Run ---")
    processor = ISPProcessor()
    html_path = "bharatkumarumma.SubscriberInfo - Copy.html"
    
    print(f"User selected: {html_path}")
    print("Parsing HTML...")
    metadata, raw_data = processor.parse_html(html_path)
    
    suspect_name = metadata.get("name", "Unknown").replace(" ", "_")
    print(f"Suspect Identified: {suspect_name}")
    print(f"Records Found: {len(raw_data)}")
    
    print("Identifying ISPs (using cache)...")
    grouped_data = processor.process_data(raw_data) # Cache should be warm from previous run
    
    print(f"ISPs: {list(grouped_data.keys())}")
    
    print("Generating Documents...")
    if "JIO" in grouped_data:
        out_excel = f"{suspect_name}_JIO_Data.xlsx"
        out_word = f"{suspect_name}_JIO_Request_Letter.docx"
        processor.fill_jio_excel(grouped_data["JIO"], "JIO IP.xlsx", out_excel)
        processor.fill_word_letter(grouped_data["JIO"], "JIO", "IP Letter.docx", out_word)
        print(f"Generated: {out_excel}, {out_word}")

    if "AIRTEL" in grouped_data:
        out_excel = f"{suspect_name}_Airtel_Data.xlsx"
        out_word = f"{suspect_name}_AIRTEL_Request_Letter.docx"
        processor.fill_airtel_excel(grouped_data["AIRTEL"], "Airtel Format.xlsx", out_excel)
        processor.fill_word_letter(grouped_data["AIRTEL"], "AIRTEL", "IP Letter.docx", out_word)
        print(f"Generated: {out_excel}, {out_word}")

    if "VI" in grouped_data:
        out_word = f"{suspect_name}_VI_Request_Letter.docx"
        processor.fill_word_letter(grouped_data["VI"], "VI", "IP Letter.docx", out_word)
        print(f"Generated: {out_word}")

if __name__ == "__main__":
    simulate_gui_run()
