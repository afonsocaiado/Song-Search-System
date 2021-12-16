# Installation and use

1. Tornar o ficheiro executável `chmod +x startup.sh`
2. `docker build . -t pri-g72`
3. `docker run --name music_lyrics -p 8983:8983 -v ${PWD}/data:/data --rm pri-g72`

==> http://localhost:8983/solr/#/