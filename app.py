import os
from flask import Flask, render_template, request, flash, redirect, url_for
from PIL import Image
import numpy as np
from collections import Counter
import io
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'  # Change this for production
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def extract_colors(image, num_colors=10):
    """
    Extracts the most common colors from an image using Pillow/Numpy.
    """
    # Resize image to speed up processing
    image.thumbnail((150, 150))
    
    # Quantize to reduce number of colors and find dominant ones
    # method=2 (FASTOCTREE) is usually good
    quantized_image = image.quantize(colors=num_colors, method=2)
    
    # Get the palette
    palette = quantized_image.getpalette()
    
    # The palette is a list of [r, g, b, r, g, b, ...]
    # We need to chunk it into tuples
    color_counts = quantized_image.getcolors()
    
    # color_counts is a list of (count, index)
    # We need to map index to RGB from palette
    
    colors = []
    if color_counts:
        # Sort by count descending
        color_counts.sort(reverse=True)
        
        for count, index in color_counts[:num_colors]:
            # Get RGB values
            r = palette[index * 3]
            g = palette[index * 3 + 1]
            b = palette[index * 3 + 2]
            
            hex_code = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            colors.append({'rgb': (r, g, b), 'hex': hex_code, 'count': count})
            
    return colors

@app.route('/', methods=['GET', 'POST'])
def index():
    colors = None
    image_data = None
    
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
            
        if file:
            try:
                # Open image using Pillow
                img = Image.open(file.stream)
                
                # Convert to RGB if it's RGBA or P
                if img.mode != 'RGB':
                    img = img.convert('RGB')

                # Extract colors
                colors = extract_colors(img.copy())
                
                # Save image to a bytes buffer to display it without saving to disk
                buffered = io.BytesIO()
                img.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                image_data = f"data:image/jpeg;base64,{img_str}"
                
            except Exception as e:
                flash(f'Error processing image: {e}')
                
    return render_template('index.html', colors=colors, image_data=image_data)

if __name__ == '__main__':
    app.run(debug=True)
