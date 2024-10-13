FROM nikolaik/python-nodejs:python3.10-nodejs19

RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/
RUN pip3 install yt-dlp https://github.com/coletdjnz/yt-dlp-youtube-oauth2/archive/refs/heads/master.zip
RUN python3 -m pip install --upgrade pip setuptools
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
RUN yt-dlp --username oauth2 --password '' -F https://www.youtube.com/watch?v=nVjsGKrE6E8 && echo "Authentication complete. Continuing build..."
CMD python3 -m YukkiMusic
