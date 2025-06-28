# 🚀 GrainPalette Deployment Guide

This guide provides comprehensive instructions for deploying and running the GrainPalette Rice Classification system.

## 📋 Prerequisites

- Python 3.8 or higher
- 4GB+ RAM (recommended)
- Internet connection (for initial setup)
- Web browser (Chrome, Firefox, Safari, Edge)

## 🔧 Installation Methods

### Method 1: Quick Start (Recommended)

1. **Navigate to Project Directory**
   ```bash
   cd grainpaletteSBL
   ```

2. **Run the Launcher**
   ```bash
   python start_app.py
   ```
   This will automatically:
   - Install required dependencies
   - Run system tests
   - Start the Streamlit app

### Method 2: Manual Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   streamlit run app.py
   ```

### Method 3: Virtual Environment (Production)

1. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```

2. **Activate Environment**
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Application**
   ```bash
   streamlit run app.py
   ```

## 🌐 Accessing the Application

Once running, the app will be available at:
- **Local**: http://localhost:8501
- **Network**: http://[your-ip]:8501

The app will automatically open in your default browser.

## 📱 Application Features

### Main Pages

1. **Rice Classification**
   - Upload rice grain images
   - Get instant AI predictions
   - View confidence scores
   - Interactive result visualization

2. **About the Project**
   - Technology overview
   - Supported rice varieties
   - Use cases and applications

3. **Model Performance**
   - Accuracy metrics
   - Confusion matrix
   - Performance visualization

4. **Meet the Team**
   - Developer profiles
   - Project contributions

## 🎯 Usage Instructions

### Uploading Images

1. **Supported Formats**: JPG, JPEG, PNG
2. **Recommended Size**: Any size (auto-resized)
3. **Image Quality**: Clear, well-lit photos work best
4. **Content**: Multiple rice grains preferred

### Getting Predictions

1. Upload an image using the file uploader
2. Click "🎯 Predict Rice Type"
3. View the prediction result and confidence
4. Explore the detailed confidence chart
5. Read about the predicted rice variety

## 🔧 Troubleshooting

### Common Issues

**App Won't Start**
```bash
# Check Python version
python --version

# Reinstall dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

**Model Loading Error**
- Ensure `rice.keras` file is in the project root
- Check available memory (model requires 2GB+)
- Try restarting the application

**Port Already in Use**
```bash
# Use a different port
streamlit run app.py --server.port 8502
```

**Memory Issues**
- Close other applications
- Use a machine with more RAM
- Try running with fewer background processes

### Testing the System

Run comprehensive tests:
```bash
python test_system.py
```

Run demo:
```bash
python demo.py
```

## 🎨 Customization

### Changing Theme Colors

Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#4CAF50"  # Change this color
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F5F5F5"
```

### Adding New Rice Varieties

1. Update `class_names` in `model_utils.py`
2. Add descriptions in `rice_descriptions` in `app.py`
3. Retrain the model with new data

### Modifying UI

Edit `app.py`:
- Update CSS styles in the markdown section
- Modify layout and components
- Add new pages or features

## 🚀 Production Deployment

### Local Production Server

```bash
streamlit run app.py --server.port 80 --server.address 0.0.0.0
```

### Docker Deployment

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
```

Build and run:
```bash
docker build -t grainpalette .
docker run -p 8501:8501 grainpalette
```

### Cloud Deployment

**Streamlit Cloud**
1. Push code to GitHub
2. Connect to Streamlit Cloud
3. Deploy with one click

**Heroku**
1. Create `Procfile`: `web: streamlit run app.py --server.port=$PORT`
2. Deploy via Heroku CLI

**AWS/Azure/GCP**
- Use container services
- Deploy via CI/CD pipelines

## 📊 Performance Optimization

### Model Optimization

- Use model caching with `@st.cache_resource`
- Load model once at startup
- Optimize image preprocessing

### Memory Management

- Clear cache periodically
- Optimize image sizes
- Use efficient data structures

### Speed Improvements

- Use GPU acceleration if available
- Optimize TensorFlow settings
- Enable model quantization

## 🔒 Security Considerations

### File Upload Security

- Validate file types and sizes
- Scan uploaded files
- Implement rate limiting

### Production Security

- Use HTTPS in production
- Implement authentication if needed
- Monitor resource usage

## 📈 Monitoring and Analytics

### Built-in Metrics

- Model prediction accuracy
- Response times
- Error rates

### Custom Analytics

- User interaction tracking
- Usage patterns
- Performance metrics

## 🛠️ Development Tools

### Useful Commands

```bash
# Run with debugging
streamlit run app.py --logger.level=debug

# Clear cache
streamlit cache clear

# Check configuration
streamlit config show
```

### Development Mode

```bash
# Auto-reload on changes
streamlit run app.py --server.runOnSave=true
```

## 📞 Support and Maintenance

### Getting Help

1. Check this deployment guide
2. Run diagnostic tests: `python test_system.py`
3. Check logs for error messages
4. Consult the troubleshooting section

### Regular Maintenance

- Update dependencies monthly
- Monitor disk space
- Backup model files
- Review performance metrics

## 🔄 Updates and Upgrades

### Updating the Application

1. Backup current installation
2. Pull latest changes
3. Update dependencies: `pip install -r requirements.txt --upgrade`
4. Test the updated system: `python test_system.py`
5. Restart the application

### Model Updates

1. Replace `rice.keras` with new model
2. Update class names if changed
3. Test predictions
4. Update documentation

---

**Made with ❤️ by the GrainPalette Team**

For additional support, please refer to the main README.md or contact the development team.
