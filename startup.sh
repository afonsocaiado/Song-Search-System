#!/bin/bash

precreate-core music

# Start Solr in background mode so we can use the API to upload the schema
solr start

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary @schema.json \
    http://localhost:8983/solr/music/schema

# Populate collection
bin/post -c courses /data/music_lyrics.csv

# Restart in foreground mode so we can access the interface
solr restart -f
