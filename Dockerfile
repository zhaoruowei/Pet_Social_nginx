FROM python:3.9
WORKDIR /pet_social
COPY . /pet_social
RUN pip install -r requirements.txt
RUN chmod +x /pet_social/run.sh
CMD ["/pet_social/run.sh"]
EXPOSE 8000
