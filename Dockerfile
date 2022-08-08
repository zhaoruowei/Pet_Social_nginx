FROM python:3.9
WORKDIR /Pet_Social
COPY . /Pet_Social
RUN pip install -r requirements.txt
RUN chmod +x /pet_social/run.sh
CMD ["/Pet_Social/run.sh"]
EXPOSE 8000
