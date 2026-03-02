# Datasets

This directory contains datasets used in the experiments and scripts to download and prepare them.

Each dataset subdirectory provides:

* A `README.md` with download instructions and a step-by-step guide for converting the raw data into the formats required by the different systems.
* Conversion scripts shared across the pipeline.
* A `requirements.txt` with Python dependencies for those scripts.

## Available datasets

| Directory | Dataset | Description |
|-----------|---------|-------------|
| `Wikidata/` | [Wikidata snapshot](https://github.com/MillenniumDB/path-query-challenge) | Real-world Wikidata graph with 660 SPARQL queries from the Wikidata query log. |
| `Yago-2S/` | [Yago-2S knowledge base](https://yago-knowledge.org/downloads/yago-2s) | Large knowledge base evaluated with 7 complex RPQ queries. |
| `RPQBench/` | [LD-RPQB (ex. RPQBench)](https://github.com/Mamenglu/LD-RPQB) | Synthetic benchmark with a configurable number of triples and generated queries. |

## Common conversion scripts

All dataset directories share the following scripts (see `Scripts/` in the repository root for the canonical versions):

| Script | Description |
|--------|-------------|
| `truncate` | Filters N-Triples triples by subject/predicate/object using regex patterns. Removes non-URI literals, keeping only object-to-object edges. |
| `deprefix-nt` | Strips URI prefixes from N-Triples files, leaving only the local name of each URI. |
| `deprefix-sparql` | Strips URI prefixes from SPARQL query files. |
| `remove-dups` | Removes duplicate triples from an N-Triples file. |
| `nt-to-mm` | Converts an N-Triples file into a set of [Matrix-Market](https://math.nist.gov/MatrixMarket/formats.html) adjacency matrix files (one per predicate). Used as input for the LA-RPQ algorithm. |
| `nt-to-csv` | Converts an N-Triples file into CSV adjacency files. Used as input for Memgraph and FalkorDB bulk loaders. |
| `sparql-to-fa` | Converts SPARQL regular path queries into NFA adjacency matrices in Matrix-Market format. Requires the graph prepared by `nt-to-mm`. |

## Typical preprocessing pipeline

```
raw dataset (.nt)
    │
    ├─ ./truncate | ./deprefix-nt → dataset-trunc.nt
    │
    ├─ ./nt-to-mm  → dataset-mm/       (LA-RPQ, RPQ-matrix)
    ├─ ./nt-to-csv → dataset-csv/      (Memgraph, FalkorDB)
    │
    └─ ./sparql-to-fa queries.txt dataset-mm/ → dataset-queries/
```

For RPQ-matrix and MillenniumDB, additional steps are needed — see the corresponding directories under `Databases/`.
