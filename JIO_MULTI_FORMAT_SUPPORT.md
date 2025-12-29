# Jio Reply Multi-Format Support

## Overview
The Jio Reply Analyzer now supports both `.7z` and `.zip` file formats for processing Jio reply files.

## Supported Formats

### 1. **7z Format** (Original)
- Compressed archive format using 7-Zip
- Typically used for larger reply files
- Requires `py7zr` library for extraction

### 2. **ZIP Format** (New)
- Standard ZIP archive format
- More universally compatible
- Uses built-in `zipfile` library for extraction

## File Structure

Both formats should contain CSV files with the following structure:

```
Archive (.7z or .zip)
├── File1.csv
├── File2.csv
└── File3.csv
```

### CSV Format
Each CSV file contains Jio IPDR (IP Detail Record) data with columns including:
- Name of Person/Organization
- Address
- Contact No.
- Source IP Address
- IMSI
- PGW IP address
- Session Duration
- Data Volume Up Link/Down Link
- And more...

## How It Works

1. **Upload**: Upload either a `.7z` or `.zip` file containing Jio reply data
2. **Auto-Detection**: The system automatically detects the file format based on extension
3. **Extraction**: 
   - For `.7z` files: Uses `py7zr` library
   - For `.zip` files: Uses Python's built-in `zipfile` library
4. **Processing**: Extracts all CSV files and combines them into a single dataset
5. **Analysis**: Displays results with pagination for large datasets

## Usage

### In the Streamlit App:

1. Navigate to the **Reply Parsing Tool** tab
2. Go to the **Jio Reply Analysis** column
3. Click "Upload Jio .7z or .zip"
4. Select your file (either `.7z` or `.zip` format)
5. Click "🔍 Analyze Jio"

### Results:

The analyzer will:
- Extract all CSV files from the archive
- Combine them into a single DataFrame
- Display summary statistics
- Provide paginated view for large datasets (>10,000 rows)
- Allow download of:
  - Individual CSV files
  - Combined Excel file with all data

## Technical Details

### Backend Changes (`backend.py`)

The `process_jio_reply()` function now:
1. Detects file extension using `os.path.splitext()`
2. Routes to appropriate extraction method:
   - `.7z` → `py7zr.SevenZipFile`
   - `.zip` → `zipfile.ZipFile`
3. Processes extracted CSV files identically regardless of source format

### Frontend Changes (`app.py`)

1. File uploader accepts both formats: `type=['7z', 'zip']`
2. Temporary file preserves original extension
3. Updated UI text to reflect multi-format support

## Example Files

### Sample .7z File:
```
temp_jio.7z
```

### Sample .zip File:
```
20099773_0_30310288_IPV6_IPDR_2409_40e3_5_a865_20251014090143_20251014091143_DL.zip
```

Both contain the same type of CSV data and will be processed identically.

## Error Handling

The system provides clear error messages for:
- Unsupported file formats
- Extraction failures
- Corrupted archives
- Empty or invalid CSV files

## Performance

- Both formats are processed efficiently
- Memory-optimized for large datasets
- Pagination prevents browser crashes with large result sets
- Automatic garbage collection after processing

## Dependencies

- **For .7z files**: `py7zr` library
- **For .zip files**: Built-in `zipfile` module (no additional dependency)

## Migration Notes

- Existing `.7z` workflows remain unchanged
- No breaking changes to API or functionality
- Backward compatible with all existing features
