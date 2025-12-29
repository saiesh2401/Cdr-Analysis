# Quick Start Guide: Jio Reply Multi-Format Support

## 🚀 How to Use

### Step 1: Navigate to Reply Parsing Tool
1. Open the Streamlit application
2. Click on the **"Reply Parsing Tool"** tab
3. Look for the **"🔵 Jio Reply Analysis"** section (middle column)

### Step 2: Upload Your File
You can now upload **either** format:

#### Option A: Upload .7z file
```
✅ Supported: file.7z
Example: jio_reply_data.7z
```

#### Option B: Upload .zip file (NEW!)
```
✅ Supported: file.zip
Example: 20099773_0_30310288_IPV6_IPDR_2409_40e3_5_a865_20251014090143_20251014091143_DL.zip
```

### Step 3: Analyze
1. Click the **"🔍 Analyze Jio"** button
2. Wait for extraction and processing
3. View results!

---

## 📊 What You'll See

### Processing Status
```
🔄 Extracting and Analyzing Jio Data...
```

### Success Message
```
✅ Analysis Complete!

Valid Hits: 350
Empty/Skipped Files: 0
```

### Results Display
- **Summary Statistics**: Total records found
- **Paginated Data View**: For large datasets (>10,000 rows)
- **Raw Evidence Files**: Individual CSV downloads
- **Combined Excel**: All data in one file

---

## 📥 Download Options

### Individual CSV Files
Each extracted CSV file is available for download:
```
📥 Download 20099336_0_30309851_IPV6_IPDR_2409_40d0_101d_f40b_20250827205147_20250827210147_DL.csv
📥 Download 20099337_0_30309852_IPV6_IPDR_2409_40d0_101d_f40b_20250827205148_20250827210148_DL.csv
...
```

### Combined Excel File
All data combined into a single Excel file:
```
📥 Download Combined Jio Excel
File: Jio_Hits_Combined.xlsx
```

---

## 🔍 Data Preview

### Sample Columns
- Source IP Address
- Landline/MSISDN/MDN/Leased Circuit ID
- IMSI
- PGW IP address
- Start Date/Time of Public IP allocation
- End Date/Time of Public IP allocation
- Session Duration
- Data Volume (Up/Down Link)
- CELL ID
- And 20+ more columns...

### Sample Data View
```
Source IP Address                      | MSISDN        | IMSI            | Start Date
2409:40e3:0042:9d41:8000:0000:0000:0000 | 918376998009 | 405871171119461 | 2025-07-17
2409:40d0:101d:f40b:8000:0000:0000:0000 | 918376998009 | 405871171119461 | 2025-08-27
```

---

## ⚙️ Advanced Features

### Pagination (for large datasets)
If your data has more than 10,000 rows:
- Automatic pagination is enabled
- Navigate between pages using controls
- Each page shows 10,000 rows
- Total count displayed

### Memory Management
- Automatic garbage collection after processing
- Efficient handling of large files
- No browser crashes

### Reset Function
Click **"🔄 Reset"** to:
- Clear current analysis
- Free up memory
- Start fresh analysis

---

## 💡 Tips & Best Practices

### File Preparation
✅ **Do:**
- Use original files from Jio
- Ensure files are not corrupted
- Check file size is reasonable

❌ **Don't:**
- Modify CSV files before upload
- Upload empty archives
- Upload non-Jio data files

### Performance Tips
- For files > 100MB, expect longer processing times
- Close other browser tabs for better performance
- Use the pagination feature for large datasets

### Troubleshooting

**Problem**: "Failed to extract zip"
- **Solution**: Ensure file is not corrupted, try re-downloading

**Problem**: "No valid data rows found"
- **Solution**: Check if CSV files inside archive are empty

**Problem**: "Unsupported file format"
- **Solution**: Only .7z and .zip are supported, convert other formats

---

## 📋 Supported File Structures

### ZIP Archive Structure
```
your_file.zip
├── file1.csv
├── file2.csv
├── file3.csv
└── ...
```

### 7Z Archive Structure
```
your_file.7z
├── file1.csv
├── file2.csv
├── file3.csv
└── ...
```

Both structures are processed identically!

---

## 🎯 Common Use Cases

### Use Case 1: Single IP Investigation
1. Upload Jio reply (ZIP or 7Z)
2. Analyze data
3. Search for specific IP address
4. Download filtered results

### Use Case 2: Bulk Data Analysis
1. Upload large archive (1000+ CSVs)
2. Let system process all files
3. Use pagination to browse results
4. Download combined Excel for offline analysis

### Use Case 3: Evidence Collection
1. Upload reply file
2. Download individual CSV files as evidence
3. Download combined Excel for court submission
4. Keep original archive as backup

---

## ✅ Checklist

Before uploading:
- [ ] File is in .7z or .zip format
- [ ] File contains Jio IPDR CSV data
- [ ] File is not password protected (or password is known)
- [ ] File size is reasonable for your system

After processing:
- [ ] Check total records count
- [ ] Review sample data
- [ ] Download required files
- [ ] Clear session if processing another file

---

## 🆘 Need Help?

### Documentation
- Full technical docs: `JIO_MULTI_FORMAT_SUPPORT.md`
- Format comparison: `JIO_FORMAT_COMPARISON.md`
- Implementation details: `JIO_MULTIFORMAT_UPDATE.md`

### Testing
Run the test script to verify your setup:
```bash
python3 test_jio_multiformat.py
```

---

## 🎉 You're Ready!

The Jio Reply Analyzer now supports both .7z and .zip formats.
Upload your file and start analyzing!
