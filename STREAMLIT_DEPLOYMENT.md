# Deploying CDR Analyzer to Streamlit Cloud

## Prerequisites
✅ GitHub repository: https://github.com/saiesh2401/Cdr-Analysis  
✅ Streamlit account (free): https://streamlit.io/cloud

## Step-by-Step Deployment

### 1. Create `.streamlit/config.toml` (Optional but Recommended)

This configures your app's appearance and settings.

```toml
[theme]
primaryColor = "#00f5ff"
backgroundColor = "#0a0e27"
secondaryBackgroundColor = "#1a1a2e"
textColor = "#ffffff"

[server]
maxUploadSize = 500
enableCORS = false
```

### 2. Ensure `requirements_cdr.txt` is Complete

Your file should include all dependencies:

```
streamlit
pandas
plotly
folium
streamlit-folium
networkx
requests
openpyxl
```

### 3. Create `.gitignore` (if not exists)

```
.venv/
__pycache__/
*.pyc
.DS_Store
cell_tower_cache.json
CDR/*.csv
*.pages
```

### 4. Commit and Push Configuration Files

```bash
git add .streamlit/config.toml .gitignore
git commit -m "Add Streamlit Cloud configuration"
git push origin main
```

### 5. Deploy on Streamlit Cloud

#### Option A: Via Web Interface (Recommended)

1. **Go to**: https://share.streamlit.io/
2. **Sign in** with GitHub
3. **Click**: "New app"
4. **Fill in**:
   - Repository: `saiesh2401/Cdr-Analysis`
   - Branch: `main`
   - Main file path: `cdr_app.py`
5. **Click**: "Deploy!"

#### Option B: Via Direct URL

Visit: https://share.streamlit.io/deploy?repository=saiesh2401/Cdr-Analysis&branch=main&mainModule=cdr_app.py

### 6. Advanced Settings (Optional)

In the deployment settings, you can:
- Set Python version (3.9, 3.10, 3.11)
- Add secrets (for API keys)
- Configure resource limits

### 7. Add Secrets (for Cell Tower APIs)

If you want to use OpenCelliD or Unwired Labs:

1. Go to your app settings
2. Click "Secrets"
3. Add:
```toml
OPENCELLID_API_KEY = "your_key_here"
UNWIRED_API_KEY = "your_key_here"
```

## Important Notes

### File Upload Limits
- Default: 200MB
- Configured: 500MB (in config.toml)
- For larger files, consider using cloud storage

### CDR Files
- Users will need to upload their own CDR files
- Sample files should NOT be committed to GitHub (privacy)
- Add `CDR/*.csv` to `.gitignore`

### Performance
- Free tier has resource limits
- For heavy usage, consider Streamlit Cloud Pro

## Post-Deployment

### Your App URL
After deployment, you'll get a URL like:
```
https://saiesh2401-cdr-analysis-cdr-app-xxxxx.streamlit.app
```

### Custom Domain (Optional)
You can configure a custom domain in app settings.

### Monitoring
- View logs in Streamlit Cloud dashboard
- Monitor resource usage
- Check for errors

## Troubleshooting

### Common Issues

**1. Module Not Found**
- Ensure all imports are in `requirements_cdr.txt`
- Check spelling and versions

**2. File Not Found**
- Verify file paths are relative
- Check case sensitivity

**3. Memory Errors**
- Optimize data processing
- Use chunking for large files
- Consider upgrading to Pro

**4. Slow Loading**
- Add `@st.cache_data` decorators
- Optimize visualizations
- Reduce initial data processing

## Security Considerations

### DO NOT Commit:
- ❌ Actual CDR files (sensitive data)
- ❌ API keys (use Secrets instead)
- ❌ Personal information
- ❌ Database credentials

### DO Commit:
- ✅ Application code
- ✅ Requirements file
- ✅ Configuration files
- ✅ Documentation
- ✅ Sample/dummy data (if needed)

## Next Steps

1. Create `.streamlit/config.toml`
2. Update `.gitignore`
3. Commit and push
4. Deploy on Streamlit Cloud
5. Test with sample CDR file
6. Share the URL!

Your futuristic CDR analyzer will be live and accessible to anyone with the link! 🚀
