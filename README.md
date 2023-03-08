# IA-OS
In this project our objective is to obtain data of 10 pdfs, in particular we want: A list of the urls that each pdf contains
         A graphic with each pdf and the number of images and pictures they have
         An image generated with relevant words of all pdf files (Keyword)

To perform all these actions we will execute a Python Script. 
Moreover, to analyze and treat, as well as convert to XML each pdf we are going to use a web service called "grobid". 

## 
#### Author: Eduardo Marquina García
#### Contact: eduardo.marquina.garcia@alumnos.upm.es
#### Year: 2023

## Pre- Requirements
You must have installed "Docker" which is a software container platform that enables consistent application deployment across any environment. 
Depending on your Operating System you could do it in Linux through your terminal or in Windows installing "Docker Desktop".

Also we need to have installed "Poetry", we can do it by using this command: (if you are using Linux) or by pip install poetry (if you are using Windows).


## Instructions for use
### Step 1: 
First of all you may clone this repository with command:  
***git clone https://github.com/edumg180032/IA-OS

### Step 2:
After this you have to be located on directory "IAOSProject" and execute: 
***docker network create <network_name>

### Step 3:
You have to run the grobid service who is on port 8070 using this command:
***docker run --name grobid --network <network_name> -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2

We can check if grobid it's running properly by entering on the internet:  
***http://localhost:8070

### Step 4:
Open a new terminal, because the last one will be running grobid. 
In this point we have to run:
***docker run -it --rm --network="networkIA2" -v "<pdf_path>:<path_new_content>" mi_imagen

<pdf_path> is the path in which you have located all the pdf files in your local computer.
<path_new_content> is the path in which it will upload the pdf files as well as the results of running the script

¡CAUTION!
Depending on your operating system the <pdf_path> could have different formats:
In Linux: /home/<username>/.../
In Windows: "//d/.../"
       
