# Imports y bibliotecas que empleamos en el codigo
import os
import requests
import xml.etree.ElementTree as ET

#Para dibujar gráficas
import matplotlib.pyplot as plt

# Se usan para la obtención de palabras abstractas de los pdf
from collections import Counter
from wordcloud import WordCloud

# Elimina palabras poco relevantes/comunes (p.e determinantes)
#  para la obtencion del keyword 
import nltk
from nltk.corpus import stopwords

#importamos las bibliotecas relacionadas con tratamiento de
# expresiones regulares, como son el formato de las urls
import fitz
import re

# Unicamente es necesario ejecutar esta linea si es la 
# primera vez que ejecutas el programa y no tienes descargada
nltk.download('stopwords')

# En nuestro caso los pdf de los que obtenemos 
# el filtrado de palabras están en inglés
stop_words = set(stopwords.words('english'))
#####################################################################


# Directorio de PDFs
pdf_dir= '/IAOSProject/media/'

# Listas para almacenar los conteos de URLs, imágenes y palabras abtractas
pdf_names = []
imagenes_por_pdf = []
urls_por_pdf = []
abstracts = []

#Funcion para acceder a grobid
def send_grobid(path):
# URL de Grobid
    grobid_url = 'http://grobid:8070/api/processFulltextDocument'
    with open(path,'rb') as file:
        response = requests.post(grobid_url, files = {'input':file})
    return response.content.decode('utf-8')


# Función para crear la nube de palabras
def create_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    #plt.show()
    image_name= "Keyword.png"
    #plt.savefig(pdf_dir + 'Keyword')
    image_path = os.path.join(pdf_dir, image_name)
    plt.savefig(image_path)
    plt.close()
    
    return image_path

# Iterar sobre los archivos en el directorio
for filename in os.listdir(pdf_dir):
    if filename.endswith('.pdf'):
        # Leer el archivo PDF correspondiente
        print(f'Processing PDF: {filename}')
        path_complete = os.path.join(pdf_dir,filename)

        # Enviar la solicitud a Grobid
        xml_grob = send_grobid(path_complete)
        tree = ET.ElementTree(ET.fromstring(xml_grob))
        root = tree.getroot()

        # Conteo de imágenes
        images_count = len(root.findall(".//{http://www.tei-c.org/ns/1.0}figure"))
        #print(f'Número de imágenes: {images_count}')



        with fitz.open(path_complete) as doc:
            urls = []  # Crear la lista de URLs para este PDF
            for page in doc:
                text = page.get_text()
                # Buscar todas las cadenas de texto que parezcan URLs
                urls_encontradas = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
                urls.extend(urls_encontradas)
            urls_por_pdf.append(urls)  # Agregar la lista de URLs a la lista general
            if len(urls) > 0:
                print(f'URLs encontrados en {filename}:')
                for url in urls:
                    print(f'\t{url}')
            else:
                print(f'No se encontraron URLs en {filename}.')


        # Extraer el abstract del xml
        abstract = ''
        for ab in root.findall(".//{http://www.tei-c.org/ns/1.0}abstract"):
            for p in ab.findall(".//{http://www.tei-c.org/ns/1.0}p"):
                abstract += p.text.strip() + '\n'

        # Filtro de las stop words del texto del abstract. 
        abstract_clean = ' '.join([word for word in abstract.split() if word.lower() not in stop_words]) 
        abstracts.append(abstract_clean)

        pdf_names.append(filename)
        imagenes_por_pdf.append(images_count)

# Unir los abstracts en un solo string
all_abstracts = ' '.join(abstracts)

# Crear el conteo de palabras
word_freq = Counter(all_abstracts.split())

# Crear la nube de palabras
create_wordcloud(word_freq)

# Crear gráfico de barras para el número de imágenes
plt.bar(pdf_names, imagenes_por_pdf)
plt.xticks(rotation=90)
plt.ylim(0, max(imagenes_por_pdf) + 1)
plt.xlabel('PDFs')
plt.ylabel('Número de imágenes')
plt.title('Número de imágenes encontradas en cada PDF')
#plt.show()
image_name2= "conteoImagenes.png"
#plt.savefig(pdf_dir + 'conteo_Imagenes')
image_path2 = os.path.join(pdf_dir, image_name2)
plt.savefig(image_path2)
   
    # Cerrar figura
plt.close()
    
