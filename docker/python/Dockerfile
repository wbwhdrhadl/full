# Step1 : Base Images
FROM python:3.9

# Step2 : Package Install
RUN apt -y update && apt -y upgrade && apt -y install git net-tools vim

# Step3 : Specify a working directory
WORKDIR /app

# Step4 : Copy file copy
COPY .bashrc .
COPY .exec .
COPY hello.py . 
RUN pip install bottle

# Step 5 : Open port
EXPOSE 3000

# Step 6 : Excute command
CMD ["python","hello.py"]



