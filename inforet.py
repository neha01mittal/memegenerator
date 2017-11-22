from google.cloud import vision
from google.cloud.vision import types
import csv

def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    print 'uri', uri
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts: ')
    try:
        newtext = texts[0].description.split('quickmeme.com')[0].split('CHUCK TESTA')[0].split('uickmeme.com')[0].split('HISTORY.COM')[0]
        print('\n{}'.format(newtext))
        return newtext
    except:
        print 'Error'
        return 'Error parsing text'

with open('names.csv', 'w') as csvf:
    fieldnames = ['caption']
    writer = csv.DictWriter(csvf, fieldnames=fieldnames)
    writer.writeheader()
    with open('memes_total_time.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            newtext = detect_text_uri('http://i.qkme.me/'+ row[0].split('\t')[0] + '.jpg')
            writer.writerow({'caption': newtext})