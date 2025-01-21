# ocr_egyptian_ID
A Python-based application that detects and processes Egyptian ID cards using YOLO and EasyOCR. This system also identifies fraudulent IDs by verifying elements such as the picture, first name, and last name.

## Features

- **ID Card Detection**: Automatically detects and crops the ID card from an image.
- **Field Detection**: Identifies key fields including name, address, and national ID number.
- **Text Extraction**: Extracts text in both Arabic and English.
- **ID Decoding**: Decodes the national ID to extract:
  - Birth Date
  - Governorate
  - Gender
  - Birth Place
  - Location
  - Nationality
- **Fraud Detection**: Recognizes fake IDs by validating the authenticity of the picture and personal information.
- **Web Interface**: User-friendly interface built with Streamlit.

## Installation

1. **Clone the repository**:
   ```bash
   git clone (https://github.com/SondosSaad14/ocr_egyptian_ID)
   ```
2. **Navigate to the project directory**:
   ```bash
   cd ocr_egyptian_ID
   ```
3. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:
   ```bash
   streamlit run deployment.py
   ```
2. **Upload an Image**: Use the web interface to upload an image of an Egyptian ID card.
3. **View Results**: The application will display the detected ID card, extracted fields, and decoded information.

## Model Training

- **YOLO Model**: Trained for ID card detection.
- **EasyOCR**: Utilized for text extraction in Arabic and English.

  
## Acknowledgments

- [YOLO]      (https://github.com/ultralytics/yolov5) for object detection.
- [EasyOCR]   (https://github.com/JaidedAI/EasyOCR) for optical character recognition.
- [Streamlit] (https://streamlit.io/) for the web interface.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.


## Contact

For questions or feedback, feel free to open an issue or reach out to [sondos](https://github.com/SondosSaad14).

Email: bakeer.sondos@gmail.com

LinkedIn: [LinkedIn](www.linkedin.com/in/sondos-bakeer-5718a4310)
