FROM python:3.10

ENV PYTHONUNBUFFERED 1

# RUN apt-get update

RUN useradd -ms /bin/bash hossam
ENV PATH="/home/hossam/.local/bin:${PATH}"

USER hossam
COPY --chown=hossam . /home/hossam/

RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r /home/hossam/requirements/requirements.txt
RUN chmod +x /home/hossam/entrypoint.sh

WORKDIR /home/hossam/


EXPOSE 8000


ENTRYPOINT ["/home/hossam/entrypoint.sh"]
# alias deploy-backend="cd /home/eprofile/ && git pull && docker compose up --build -d"
# alias deploy-frontend="cd /home/islam/frontend-admin/ && git pull && docker-compose up --build -d"