FROM python:3.8-slim-buster

WORKDIR /flask-loan-app

RUN python3 -m pip install --upgrade pip 

COPY artefacts/reqiurements.txt  reqiurements.txt

RUN pip3 install -r reqiurements.txt

COPY . .

CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0"]

# Access key
# AKIAX3G4BDFZWWFNLGFY
	

# Secret access key    
# ECvw4Wegx/ZvtUa5d0fIlMCyoEYOxK3alG8YPyPj  