# Yago-2s graph

Basically, the provided dataset is based on the [Yago-2S knowledge base](https://yago-knowledge.org/downloads/yago-2s). We truncate this dataset from properties and convert it into matrix-market adjacency matrices for linear algebra-based algorithms and into CSVs for Memgraph and FalkorDB.

## Processing the dataset

The original dataset in the [N-triples](https://www.w3.org/TR/n-triples/) format can be downloaded from [the official website](https://yago-knowledge.org/downloads/yago-2s). The following transformations has been applied.

```bash
# The downloaded dataset is yago-2s.nt

# Create a Python venv and install requirements
python -m venv ./.venv && source ./.venv/bin/activate
pip install -r requirements.txt

# Remove the properties & the prefixes from the dataset.
./truncate yago-2s.nt | ./deprefix-nt > yago-2s-trunc.nt

# LA-RPQ (our-algorithm). Convert the truncated dataset to a set of matrix-market files.
./nt-to-mm yago-2s-trunc.nt yago-2s-mm

# FalkorDB, Memgraph. Convert the truncated dataset to a few CSV files.
./nt-to-csv yago-2s-trunc.nt yago-2s-csv

# For preparing the dataset for RPQ-matrix and MillenniumDB see the corresponding Databases dir.

# Remove prefixes from the original queries.
./deprefix-sparql ./sparql-queries.txt > ./sparql-queries-trunc.txt
# Convert queries to a set of Matrix-Market files.
./sparql-to-fa ./sparql-queries-trunc.txt ./yago-2s-mm ./yago-2s-queries
```


