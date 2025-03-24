# Wikidata graph

Basically, the provided dataset is based on th [MillenniumDB regular path query challenge](https://github.com/MillenniumDB/path-query-challenge). We truncate this dataset from properties and convert it into matrix-market adjacency matrices for linear algebra-based algorithms and into CSVs for Memgraph and FalkorDB.

## Processing the dataset

The original dataset in the [N-triples](https://www.w3.org/TR/n-triples/) format can be downloaded from [Figshare](https://figshare.com/s/50b7544ad6b1f51de060). The following transformations has been applied.

```bash
# The downloaded dataset is wikidata.nt

# Create a Python venv and install requirements
python -m venv ./.venv && source ./.venv/bin/activate
pip install -r requirements.txt

# Remove the properties & the prefixes from the dataset.
./truncate wikidata.nt | ./deprefix-nt > wikidata-trunc.nt

# LA-RPQ (our-algorithm). Convert the truncated dataset to a set of matrix-market files.
./nt-to-mm wikidata-trunc.nt wikidata-mm

# FalkorDB, Memgraph. Convert the truncated dataset to a few CSV files.
./nt-to-csv wikidata-trunc.nt wikidata-csv

# For preparing the dataset for RPQ-matrix and MillenniumDB see the corresponding Databases dir.

# Remove prefixes from the original queries.
./deprefix-sparql ./sparql-queries.txt > ./sparql-queries-trunc.txt
# Convert queries to a set of Matrix-Market files.
./sparql-to-fa ./sparql-queries-trunc.txt ./wikidata-mm ./wikidata-queries
```

