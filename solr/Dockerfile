FROM solr:8.10

#COPY music_lyrics.csv /data/music_lyrics.csv

#COPY schema.json /data/schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
