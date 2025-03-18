import os
import exifread
import PyPDF2
from PIL import Image
from PIL.ExifTags import TAGS
import piexif
import chardet
from datetime import datetime

def extract_metadata(file_path):
    """Extract metadata from a file based on its type (image, PDF, or text)."""
    file_metadata = {
        'file_name': os.path.basename(file_path),
        'file_size': os.path.getsize(file_path),
        'file_type': get_file_type(file_path),
        'last_modified': get_last_modified(file_path)
    }

    # Image files (JPEG, PNG, TIFF)
    if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff')):
        file_metadata.update(extract_image_metadata(file_path))
    
    # PDF files
    elif file_path.lower().endswith('.pdf'):
        file_metadata.update(extract_pdf_metadata(file_path))
    
    # Text files
    elif file_path.lower().endswith(('.txt', '.md')):
        file_metadata.update(extract_text_metadata(file_path))

    return file_metadata

def get_file_type(file_path):
    """Return the MIME type of the file."""
    import magic  # You might need to install `python-magic`
    mime = magic.Magic(mime=True)
    return mime.from_file(file_path)

def get_last_modified(file_path):
    """Return the last modified timestamp of the file."""
    try:
        return datetime.utcfromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        print(f"Error fetching last modified date: {e}")
        return 'Unknown'

def extract_image_metadata(file_path):
    """Extract EXIF and other metadata from an image file (JPEG, PNG, TIFF)."""
    metadata = {}
    try:
        with Image.open(file_path) as img:
            metadata['image_format'] = img.format
            metadata['image_mode'] = img.mode
            metadata['image_size'] = img.size
            metadata['image_resolution'] = img.info.get('dpi', 'Unknown')
            
            # Extract EXIF data for supported formats (JPEG, TIFF)
            exif_data = img._getexif() if hasattr(img, '_getexif') else None
            if exif_data:
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    metadata[tag_name] = value

            # Additional metadata extraction: color profile, ICC profile, and thumbnail
            if 'icc_profile' in img.info:
                metadata['icc_profile'] = img.info['icc_profile']

            if 'thumbnail' in img.info:
                metadata['thumbnail'] = img.info['thumbnail']
            
            # Get image orientation from EXIF tag if available
            if exif_data and 274 in exif_data:
                metadata['image_orientation'] = exif_data.get(274)  # Orientation tag (274)

            # ICC profile and color space
            metadata['color_space'] = img.info.get('icc_profile', 'Unknown')

            # Extract detailed GPS data if available
            if exif_data and 34853 in exif_data:  # GPS info tag
                gps_data = exif_data.get(34853)
                if gps_data:
                    metadata['gps'] = gps_data

            # Extract additional image properties (like DPI)
            metadata['dpi'] = img.info.get('dpi', 'Unknown')

    except Exception as e:
        print(f"Error extracting image metadata: {e}")
    
    return metadata

def extract_pdf_metadata(file_path):
    """Extract metadata from a PDF file."""
    metadata = {}
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            doc_info = reader.getDocumentInfo()
            metadata['author'] = doc_info.author
            metadata['producer'] = doc_info.producer
            metadata['title'] = doc_info.title
            metadata['subject'] = doc_info.subject
            metadata['creator'] = doc_info.creator
            metadata['keywords'] = doc_info.get('/Keywords', 'Unknown')
            metadata['creation_date'] = doc_info.get('/CreationDate', 'Unknown')
            metadata['modification_date'] = doc_info.get('/ModDate', 'Unknown')
            metadata['page_count'] = reader.getNumPages()
    except Exception as e:
        print(f"Error extracting PDF metadata: {e}")
    return metadata

def extract_text_metadata(file_path):
    """Extract simple metadata from a text file."""
    metadata = {}
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            # Detect file encoding
            result = chardet.detect(content)
            metadata['encoding'] = result.get('encoding', 'Unknown')
            
            # Get word count and line count
            content_str = content.decode(metadata['encoding'], errors='ignore')
            metadata['word_count'] = len(content_str.split())
            metadata['line_count'] = len(content_str.splitlines())

            # Get the last modified date
            metadata['last_modified'] = get_last_modified(file_path)

    except Exception as e:
        print(f"Error extracting text metadata: {e}")
    return metadata
