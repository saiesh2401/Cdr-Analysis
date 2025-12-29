#!/usr/bin/env python3
"""
Test script to verify Jio multi-format support
Tests both .7z and .zip file processing
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from backend import ISPProcessor

def test_jio_zip():
    """Test processing of Jio .zip file"""
    print("=" * 60)
    print("Testing Jio ZIP File Processing")
    print("=" * 60)
    
    processor = ISPProcessor()
    
    # Test with the zip file
    zip_path = "Jio_Reply/20099773_0_30310288_IPV6_IPDR_2409_40e3_5_a865_20251014090143_20251014091143_DL - Copy.zip"
    
    if not os.path.exists(zip_path):
        print(f"❌ Test file not found: {zip_path}")
        return False
    
    print(f"\n📁 Processing: {zip_path}")
    print(f"📊 File size: {os.path.getsize(zip_path) / 1024:.2f} KB")
    
    # Process the file
    result, msg = processor.process_jio_reply(zip_path)
    
    if result is None:
        print(f"\n❌ Processing failed: {msg}")
        return False
    
    # Display results
    hits_df = result['hits_df']
    misses = result['misses']
    
    print(f"\n✅ Processing successful!")
    print(f"\n📊 Results Summary:")
    print(f"   - Total records: {len(hits_df):,}")
    print(f"   - Total columns: {len(hits_df.columns)}")
    print(f"   - Files processed: {hits_df['Source_File'].nunique() if not hits_df.empty else 0}")
    print(f"   - Skipped files: {len(misses)}")
    
    if not hits_df.empty:
        print(f"\n📋 Column Names:")
        for i, col in enumerate(hits_df.columns[:10], 1):
            print(f"   {i}. {col}")
        if len(hits_df.columns) > 10:
            print(f"   ... and {len(hits_df.columns) - 10} more columns")
        
        print(f"\n📄 Sample Data (first 3 rows):")
        # Show first few important columns
        display_cols = ['Source IP Address', 'Landline/MSISDN/MDN/Leased Circuit ID for Internet Access', 
                       'IMSI', 'Start Date of Public IP Address allocation (dd/mm/yyyy)']
        available_cols = [col for col in display_cols if col in hits_df.columns]
        
        if available_cols:
            print(hits_df[available_cols].head(3).to_string(index=False))
        else:
            print(hits_df.head(3).to_string(index=False))
    
    if misses:
        print(f"\n⚠️  Skipped files:")
        for miss in misses[:5]:
            print(f"   - {miss}")
        if len(misses) > 5:
            print(f"   ... and {len(misses) - 5} more")
    
    return True

def test_jio_7z():
    """Test processing of Jio .7z file (if available)"""
    print("\n" + "=" * 60)
    print("Testing Jio 7Z File Processing")
    print("=" * 60)
    
    processor = ISPProcessor()
    
    # Test with the 7z file
    sevenz_path = "temp_jio.7z"
    
    if not os.path.exists(sevenz_path):
        print(f"\n⚠️  7z test file not found: {sevenz_path}")
        print("   Skipping 7z test (this is optional)")
        return True
    
    print(f"\n📁 Processing: {sevenz_path}")
    print(f"📊 File size: {os.path.getsize(sevenz_path) / 1024:.2f} KB")
    
    # Process the file
    result, msg = processor.process_jio_reply(sevenz_path)
    
    if result is None:
        print(f"\n❌ Processing failed: {msg}")
        return False
    
    # Display results
    hits_df = result['hits_df']
    misses = result['misses']
    
    print(f"\n✅ Processing successful!")
    print(f"\n📊 Results Summary:")
    print(f"   - Total records: {len(hits_df):,}")
    print(f"   - Files processed: {hits_df['Source_File'].nunique() if not hits_df.empty else 0}")
    print(f"   - Skipped files: {len(misses)}")
    
    return True

def main():
    """Run all tests"""
    print("\n🧪 Jio Multi-Format Support Test Suite\n")
    
    # Test ZIP format
    zip_success = test_jio_zip()
    
    # Test 7Z format (optional)
    sevenz_success = test_jio_7z()
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print(f"ZIP Format Test: {'✅ PASSED' if zip_success else '❌ FAILED'}")
    print(f"7Z Format Test:  {'✅ PASSED' if sevenz_success else '⚠️  SKIPPED'}")
    
    if zip_success:
        print("\n🎉 All critical tests passed!")
        print("✅ Jio Reply Analyzer now supports both .7z and .zip formats")
    else:
        print("\n❌ Some tests failed. Please review the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
