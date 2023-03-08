# IA-OS
In this project our objective is to obtain data of 10 pdfs, in particular we want: 
         A list of the urls that each pdf contains
         A graphic with each pdf and the number of images and pictures they have
         An image generated with relevant words of all pdf files (Keyword)

To perform all these actions we will execute a Python Script. 
Also, to analyze and treat, as well as convert to XML each pdf we are going to use a web service called "grobid". 
Moreover, we are going to use Poetry which is a Python package and dependency manager that simplifies the packaging, publishing, and installation of Python projects.


## 
#### Author: Eduardo Marquina García
#### Contact: eduardo.marquina.garcia@alumnos.upm.es
#### Year: 2023

## Pre- Requirements
You must have installed "Docker" which is a software container platform that enables consistent application deployment across any environment. 
Depending on your Operating System you could do it in Linux through your terminal or in Windows installing "Docker Desktop". For this action you can use this url: https://www.docker.com/products/docker-desktop/ or to install it in Linux you can use: https://grobid.readthedocs.io/en/latest/Grobid-docker/#crf-only-image 

Also we need to pull the grobid image, so we have to execute:
> docker pull lfoppiano/grobid:${latest_grobid_version}


## Instructions for use
### Step 1: 
First of all you may clone this repository with command:  
> git clone https://github.com/edumg180032/IA-OS 

### Step 2:
After this you have to be located on directory "IAOSProject" and execute: 
> docker network create <network_name>

### Step 3:
You have to run the grobid service who is on port 8070 using this command:
> docker run --name grobid --network <network_name> -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2 

We can check if grobid it's running properly by entering on the internet:  
> https://localhost:8070 


### Step 4:
We have to generate the image while being in IAOSProject directory by putting this command:
> docker build -t <image_name> .

### Step 5:
Open a new terminal, because the last one will be running grobid. 
In this point we have to run:
> docker run -it --rm --network="<network_name>" -v "<pdf_path>:<project_path>" <image_name> 

<pdf_path> is the path in which you have located all the pdf files in your local computer.
<project_path> is the path in which it will upload the pdf files as well as the results of running the script

¡CAUTION!
Depending on your operating system the <pdf_path> could have different formats:
In Linux: /home/<username>/.../
In Windows: "//d/.../"

### Step 6:
To activate the poetry shell we run:
> poetry shell

### Step 7:
To finish we move to "iaosproject" directory and execute 
> poetry run python3.10 __init\_\_.py  


After this we may see this in our terminal (you should have other pdf names): 
         
         
![](https://github.com/edumg180032/IAOSProject/blob/main/captura.png)

         
         
         
         
         
         
### Aditional Step:
To prove everything is running correctly move to "tests" directory and execute again:
> poetry run python3.10 __init\_\_.py  
