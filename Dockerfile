#Cogemos una imagen ubuntu
FROM ubuntu:lunar

#Copiamos el codigo fuente
COPY . /IAOSProject

# Ejecutamos pip y la version más actualizada del mismo
#RUN apt-get update 
#RUN apt-get install -y python3.10 python3-pip
#RUN python3.10 -m pip install --upgrade pip

RUN apt-get update 
RUN apt-get update && apt-get install -y curl
RUN apt-get install -y python3.10 python3.10-distutils
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10

#Definimos carpeta de trabajo
WORKDIR /IAOSProject

RUN pip install poetry
RUN poetry install