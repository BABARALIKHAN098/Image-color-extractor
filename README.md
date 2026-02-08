# 🎨 Color Extractor using Numpy

**Color Extractor** is a powerful and efficient web application designed to automatically identify and extract the most dominant colors from any image. Built with **Python**, **Flask**, and **Numpy**, this tool provides designers, developers, and artists with an instant color palette generation solution.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)
![Numpy](https://img.shields.io/badge/Numpy-Latest-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🚀 Key Features

*   **Instant Color Extraction**: Upload any image and instantly retrieve its top 10 dominant colors.
*   **High-Performance Processing**: Utilizes **Numpy** and **Pillow (PIL)** for fast and accurate image quantization and color analysis.
*   **Interactive UI**:
    *   Visual representation of the extracted color palette.
    *   One-click **Hex Code Copy** functionality for easy integration into your projects.
    *   Real-time image preview.
*   **Responsive Design**: A clean, modern interface that works seamlessly on desktop and mobile devices.
*   **Secure Uploads**: Handled via Flask with file type validation.

## 🛠️ Technologies Used

*   **Backend**: [Python](https://www.python.org/), [Flask](https://flask.palletsprojects.com/)
*   **Data Processing**: [Numpy](https://numpy.org/), [Pillow (PIL)](https://python-pillow.org/)
*   **Frontend**: HTML5, CSS3, JavaScript, [FontAwesome](https://fontawesome.com/)

## 📦 Installation & Setup

Follow these steps to set up the project locally.

### Prerequisites

Ensure you have **Python 3.x** installed on your system.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/color-extractor-numpy.git
cd color-extractor-numpy
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Start the Flask development server:

```bash
python app.py
```

### 5. Access the App

Open your web browser and navigate to:

```
http://127.0.0.1:5000/
```

## 🖥️ Usage Guide

1.  **Launch the App**: Open the application in your browser.
2.  **Upload Image**: Click on the **"Choose Image"** button and select an image functionality (JPEG, PNG, etc.) from your device.
3.  **View Results**: The app will display your uploaded image alongside a generated palette of the 10 most prominent colors.
4.  **Copy Hex Codes**: Click on any color card or hex code to copy the value to your clipboard.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

*Keywords: Color Extractor, Image Palette Generator, Python, Flask, Numpy, Image Processing, Color Picker, Web App, HEX Code Finder, Dominant Colors*
