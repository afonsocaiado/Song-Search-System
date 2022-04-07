# Song Information and Lyrics Search System - Information Processing and Retrieval Project

Documentation and description for this project can be found [here](https://github.com/afonsocaiado/Song-Search-System/blob/main/docs/milestone3/report-72.pdf). The file is a school report about the development of the project, written in English.

# Installation and use

1. In this directory, run `make`. The new dataset was created in the `/solr/data` directory.
2. Run `cd solr`
3. Make the file executable with: `chmod +x startup.sh`
4. `docker build . -t pri-g72`
5. `docker run --name music_lyrics -p 8983:8983 -v ${PWD}/data:/data --rm pri-g72`

==> http://localhost:8983/solr/#/