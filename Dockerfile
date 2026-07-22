#Use Version
FROM python:3.12
#Create a Working Directory
WORKDIR /app
#Copy your Source Code/Project Files
COPY . /app
#UpgradePIP
RUN python -m pip install --upgrade pip
#Install Dependencies
RUN pip install -r requirements.txt
#Expose Port
EXPOSE 5000
#Running the Application
CMD ["python", "QR_code_generator.py"]