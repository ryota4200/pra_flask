FROM python3.9

WORKDIR /app

COPY pra_flask /app/

RUN pip install  --no-chache-dir -r requirements.txt

CMD [ "python", app2.py ]
