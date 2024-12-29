def get_file_category(filename):
    ext = filename.split('.')[-1].lower()
    if ext in ['mp3']:
        return 'Audio'
    elif ext in ['mp4']:
        return 'Video'
    elif ext in ['jpeg', 'png', 'gif']:
        return 'Image'
    return None