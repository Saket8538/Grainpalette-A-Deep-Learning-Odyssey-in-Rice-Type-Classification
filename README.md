# 🌾 GrainPalette - Rice Type Classification

An advanced AI-powered rice classification system built with Streamlit and TensorFlow. This application helps farmers, agricultural scientists, and rice enthusiasts identify different varieties of rice grains using computer vision and deep learning.

![Rice Classification Demo](https://img.shields.io/badge/Model-TensorFlow-orange) ![Framework](https://img.shields.io/badge/Framework-Streamlit-red) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 Features

- **Multi-class Classification**: Identify 5 different rice varieties (Arborio, Basmati, Ipsala, Jasmine, Karacadag)
- **High Accuracy**: 95%+ accuracy using MobileNetV2 transfer learning
- **Interactive Web Interface**: User-friendly Streamlit app with multiple pages
- **Real-time Predictions**: Fast inference with confidence scores
- **Detailed Analytics**: Performance metrics and visualization
- **Educational Content**: Learn about different rice varieties
- **Multiple Interfaces**: Streamlit web app and Flask API

## 🚀 Quick Start

### Option 1: Streamlit App (Recommended)
```bash
# Clone the repository
git clone https://github.com/yourusername/SBIgrainpallate.git
cd SBIgrainpallate

# Install dependencies
pip install -r requirements.txt

# Run the main Streamlit app
python -m streamlit run app.py
```

### Option 2: Simple Streamlit App
```bash
# Run the simplified version
python -m streamlit run app_simple.py
```

### Option 3: Flask Web App
```bash
# Run the Flask version
python main.py
```

## 🌐 Live Demo

- **Main App**: Open `http://localhost:8501` after running the Streamlit app
- **Simple App**: Open `http://localhost:8501` for the simplified version  
- **Flask App**: Open `http://localhost:5000` for the Flask interface

## 📋 System Requirements

- Python 3.8 or higher
- 4GB+ RAM recommended
- Internet connection (for initial TensorFlow Hub download)

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **ML Framework**: TensorFlow/Keras
- **Computer Vision**: MobileNetV2 (Transfer Learning)
- **Data Processing**: NumPy, Pandas, PIL
- **Visualization**: Plotly, Matplotlib, Seaborn
- **Image Processing**: OpenCV

## 📁 Project Structure

```
grainpaletteSBL/
├── app.py                 # Main Streamlit application
├── rice.keras            # Trained model file
├── requirements.txt      # Python dependencies
├── start_app.py         # Application launcher
├── test_system.py       # System testing script
├── evaluate_model.py    # Model evaluation script
├── predict.py          # Prediction utilities
├── main.py             # Flask app (alternative)
├── team_images/        # Team member photos
├── test_data/          # Test dataset
│   ├── Arborio/
│   ├── Basmati/
│   ├── Ipsala/
│   ├── Jasmine/
│   └── Karacadag/
└── README.md
```

## 🌾 Supported Rice Varieties

1. **Arborio** - Italian short-grain rice, perfect for risotto
2. **Basmati** - Aromatic long-grain rice from India/Pakistan
3. **Ipsala** - Turkish rice variety with medium grains
4. **Jasmine** - Fragrant long-grain rice from Thailand
5. **Karacadag** - Ancient Turkish rice variety from volcanic soil

## 🧪 Testing

Run system tests to verify everything is working:

```bash
python test_system.py
```

Evaluate model performance:

```bash
python evaluate_model.py
```

## 📊 Model Performance

- **Accuracy**: 95%+ on test dataset
- **Model Size**: ~2.3M parameters
- **Input Size**: 224×224×3 RGB images
- **Inference Time**: ~2 seconds per image

## 🎨 App Features

### 1. Rice Classification
- Upload rice grain images
- Get instant predictions with confidence scores
- View detailed rice variety information
- Interactive confidence visualization

### 2. About the Project
- Comprehensive project overview
- Technology stack details
- Use cases and applications

### 3. Model Performance
- Real-time performance metrics
- Confusion matrix visualization
- Per-class accuracy breakdown

### 4. Meet the Team
- Team member profiles
- Project roles and contributions

## 🔧 Usage Tips

1. **Image Quality**: Use clear, well-lit images of rice grains
2. **File Formats**: Supports JPG, JPEG, and PNG formats
3. **Image Size**: Any size (automatically resized to 224×224)
4. **Multiple Grains**: Works best with images showing multiple rice grains

## 📈 Future Enhancements

- [ ] Support for more rice varieties
- [ ] Batch processing capabilities
- [ ] Mobile app version
- [ ] API endpoints for integration
- [ ] Multi-language support
- [ ] Advanced analytics dashboard

## 👥 Team

**🎓 Aditya College of Engineering Madanapalle, JNTUA - Computer Science & Engineering**

- **Saket Kumar** - Team Leader & Project Developer (B.Tech 3rd Year)
- **Shaik Kalesha** - Team Member (B.Tech 3rd Year)  
- **Shaik Asfiya Anjum** - Team Member (B.Tech 3rd Year)
- **Shaik Thasmiya** - Team Member (B.Tech 3rd Year)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- TensorFlow team for the excellent ML framework
- Streamlit for the amazing web app framework
- MobileNetV2 team for the pre-trained model
- Agricultural research community for inspiration
- Aditya College of Engineering Madanapalle for support

## 📞 Support

If you encounter any issues or have questions:

1. Check the [troubleshooting section](#-troubleshooting) below
2. Run `python test_system.py` to diagnose problems
3. Open an issue on GitHub
4. Contact: [Your GitHub Profile]

## 🔧 Troubleshooting

### Common Issues

**Model Loading Error**
```bash
# Solution: Ensure rice.keras file is in the project root
# Check if file exists and is not corrupted
python -c "import os; print('Model exists:', os.path.exists('rice.keras'))"
```

**Package Installation Error**
```bash
# Solution: Upgrade pip and try again
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Streamlit Not Found**
```bash
# Solution: Use python -m streamlit instead
python -m streamlit run app.py
```

**Memory Error**
```bash
# Solution: Close other applications to free up RAM
# The model requires at least 2GB available memory
```

**Port Already in Use**
```bash
# Solution: Use a different port
python -m streamlit run app.py --server.port 8502
```

---

**🌾 Made with ❤️ by Saket Kumar & Team | © 2025**
