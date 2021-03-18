FROM debien:latest
LABEL description="OS para instalação de dependencias do bot (requirements.txt)"
RUN sed 's/#.*//' my-requirements-file.txt | xargs sudo apt-get install

FROM nginx:latest
LABEL description="Servidor de execução chatbot" maintainer="Gabriel Ribeiro<gabriribeiro5@live.com>"

EXPOSE 9090