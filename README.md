# Sign Language to Text Conversion 🤟➡️📝

A mini-project developed for converting American Sign Language (ASL) gestures into readable text using machine learning and computer vision techniques. This solution helps bridge the communication gap between the hearing-impaired and the general population.

  ![image](https://github.com/user-attachments/assets/bff88ac7-211a-4fcc-8a1e-c5c7f6290c1a)


---

## 📁 Project Structure

```
Sign-Language-To-Text-Conversion/
├── Application.py                  # Main GUI application using OpenCV
├── FoldersCreation.py             # Script to create necessary folders for dataset
├── TestingDataCollection.py       # Script to collect test data for each sign
├── TrainingDataCollection.py      # Script to collect training data
├── trainmodel.ipynb               # Notebook to train the model
├── Models/                        # Contains trained model and checkpoint
├── Logs/                          # Training logs (optional)
├── dataSet/                       # Contains collected gesture images
├── temp.py                        # Temporary or test script
├── README.md                      # Project documentation
├── CSE_MINI_PROJECT_Report_Template.docx
├── PROJECT PRESENTATION - SIGN LANGUAGE TO TEXT CONVERSION.pptx
├── Synopsis.docx
├── DocScanner.pdf                 # Scanned document
└── .ipynb_checkpoints/            # Jupyter notebook checkpoints
```

---

## 💡 Features

- Real-time gesture detection using webcam
- Custom dataset creation for Indian Sign Language
- Machine Learning model for gesture classification
- Easy-to-use Python GUI (OpenCV-based)
- SHA-256 checksum verification (OpenSSL integration optional)

---

## 🛠️ Technologies Used

- Python 
- OpenCV
- TensorFlow / Keras
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook

---

## 🚀 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/anshul-79/ASL-Sign-To-Text.git
   cd ASL-Sign-To-Text
   ```

2. **Collect Data**
   - Run `FoldersCreation.py` to initialize dataset folders
   - Run `TrainingDataCollection.py` to capture gesture images for each class

3. **Train the Model**
   - Open `trainmodel.ipynb` in Jupyter and train your CNN model
   - Save the trained model to the `Models/` directory

4. **Run the Application**
   ```bash
   python Application.py
   ```

---

## 📷 Example Output
Collect Data:

![Screenshot 2025-01-11 105923](https://github.com/user-attachments/assets/5c757025-8589-4705-85ca-162e8ba10f28)

Application:

![Screenshot 2025-01-08 150216](https://github.com/user-attachments/assets/7da3f9c5-ec6d-4724-80e1-1705b99bb130)

---

## ## 📄 Project Documents

- 📘 [CSE_MINI_PROJECT_Report_Template.docx](./CSE_MINI_PROJECT_Report_Template.docx)
- 📝 [Synopsis.docx](./Synopsis.docx)
- 📊 [PROJECT PRESENTATION - SIGN LANGUAGE TO TEXT CONVERSION.pptx](./PROJECT%20PRESENTATION%20-%20SIGN%20LANGUAGE%20TO%20TEXT%20CONVERSION.pptx)
- 📄 [DocScanner.pdf](./DocScanner%2011-Jan-2025%2010-52%20am.pdf)


---

## 📌 Future Enhancements

- Expand gesture dataset for full ASL alphabet
- Add Text-to-Speech conversion for output
- Optimize model for mobile deployment
- Integrate with web/desktop GUI (Tkinter, React, etc.)

---
