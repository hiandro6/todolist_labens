#imagem base (slim = versão leve)
FROM python:3.11-slim

#pasta principal dentro do container
WORKDIR /app

# evita gerar .pyc
ENV PYTHONDONTWRITEBYTECODE=1

#logs aparecem direto no terminal
ENV PYTHONUNBUFFERED=1

#copia dependencias primeiro(cache)
COPY requirements.txt .

#--no-cache-dir evita cache desnecessário e reduz o tamanho da imagem
RUN pip install --no-cache-dir -r requirements.txt

#copia apenas arquivos necessários
COPY manage.py .
COPY tasks ./tasks
COPY todolist_labens/ ./todolist_labens

#porta usada pela aplicação
EXPOSE 8000

#comando inicial do container
CMD [ "python", "manage.py", "runserver", "0.0.0:8000" ]
