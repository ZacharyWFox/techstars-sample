FROM python
COPY app.py /
COPY requirements.txt /
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0"]
