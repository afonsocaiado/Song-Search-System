#!/bin/bash

echo "--- precreate-core music"
precreate-core music

# Start Solr in background mode so we can use the API to upload the schema
echo "--- solr start"
solr start

echo "--- sleep 5"
sleep 5

# Schema definition via API
echo "--- curl schema"
curl -X POST -H 'Content-type:application/json' --data-binary @/data/schema.json http://localhost:8983/solr/music/schema

# Adding stopwords for stopword filter
echo "--- stopwords"
curl -X PUT -H 'Content-type:application/json' --data-binary '["songs"]' "http://localhost:8983/solr/music/schema/analysis/stopwords/english"
curl -X PUT -H 'Content-type:application/json' --data-binary '["song"]' "http://localhost:8983/solr/music/schema/analysis/stopwords/english"

# Populate collection
echo -e "\n--- curl music_lyrics data"
curl -X POST -H 'Content-type:application/csv' --data-binary @/data/music_lyrics.csv "http://localhost:8983/solr/music/update?commit=true"


# Restart in foreground mode so we can access the interface
echo -e "\n--- solr restart -f"
solr restart -f
