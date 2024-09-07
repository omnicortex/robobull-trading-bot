FROM python:3.9

RUN pip3 install playwright pytest pytest-playwright python-dotenv
RUN playwright install && playwright install-deps

WORKDIR /script

COPY ./createUser.py .

#RUN python3 -m pytest .
#RUN python3 tests/createUser.py 