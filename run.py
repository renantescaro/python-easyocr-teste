import easyocr

reader = easyocr.Reader(['en'])
plate_text = reader.readtext('assets/placas_antigas/1.png', detail=0)

print(f'plate_text:{plate_text}')
