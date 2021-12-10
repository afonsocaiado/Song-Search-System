chmod +x startup.sh

docker build . -t pri-g72

docker run --name music_lyrics -p 8983:8983 -v ${PWD}/data:/data --rm pri-g72