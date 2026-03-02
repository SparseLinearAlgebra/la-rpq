# Scripts

Shared utility scripts for preprocessing graph datasets in [N-Triples](https://www.w3.org/TR/n-triples/) format.

These scripts are used by both the `Datasets/` pipeline (converting raw graph data for LA-RPQ, Memgraph and FalkorDB) and some `Databases/` pipelines (converting data for rpq-matrix and MillenniumDB). Each dataset directory includes its own copies of the scripts it needs; the authoritative versions live here.

## Prerequisites

```bash
python -m venv ./.venv && source ./.venv/bin/activate
pip install -r requirements.txt
```

## Scripts reference

### `truncate`

Filters triples from an N-Triples file, keeping only triples whose subject, predicate, and object match given regex patterns. By default retains only URI-to-URI edges (drops literal objects and blank nodes).

```
Usage: truncate [input] [--s REGEX] [--p REGEX] [--o REGEX]

  input       Input .nt file (reads from stdin if omitted)
  --s REGEX   Regex for subject   (default: "^<")
  --p REGEX   Regex for predicate (default: "^<")
  --o REGEX   Regex for object    (default: "^<")
```

Example:
```bash
./truncate wikidata.nt > wikidata-trunc.nt
# or as a filter
cat wikidata.nt | ./truncate > wikidata-trunc.nt
```

---

### `deprefix-nt`

Strips URI prefixes from an N-Triples file, replacing each full URI with only its local name.

```
Usage: deprefix-nt [input]

  input   Input .nt file (reads from stdin if omitted)
```

Example:
```bash
./deprefix-nt wikidata-trunc.nt > wikidata-deprefixed.nt
# or as a filter in a pipeline
./truncate wikidata.nt | ./deprefix-nt > wikidata-processed.nt
```

---

### `deprefix-sparql`

Strips URI prefixes from SPARQL regular path query files, rewriting URIs to their local names so they match the output of `deprefix-nt`.

```
Usage: deprefix-sparql [input]

  input   Input SPARQL queries file (reads from stdin if omitted)
```

Example:
```bash
./deprefix-sparql sparql-queries.txt > sparql-queries-trunc.txt
```

---

### `remove-dups`

Removes duplicate triples from an N-Triples file.

```
Usage: remove-dups [input]

  input   Input .nt file (reads from stdin if omitted)
```

Example:
```bash
./remove-dups dataset.nt > dataset-no-dups.nt
```

---

### `nt-to-mm`

Converts an N-Triples file into a directory of [Matrix-Market](https://math.nist.gov/MatrixMarket/formats.html) adjacency matrix files — one `.txt` file per predicate.  Used as graph input for the LA-RPQ algorithm and rpq-matrix-GrB.

```
Usage: nt-to-mm <input> <output-dir>

  input       Input .nt file
  output-dir  Directory to create (must not exist)
```

Output structure:
```
<output-dir>/
  <predicate-number>.txt   # Boolean adjacency matrix in Matrix-Market format
  vertices.txt             # Mapping from URI to vertex number
  edges.txt                # Mapping from URI to predicate number
```

Example:
```bash
./nt-to-mm wikidata-trunc.nt wikidata-mm
```

---

### `nt-to-csv`

Converts an N-Triples file into a directory of CSV adjacency files for bulk import into Memgraph and FalkorDB.

```
Usage: nt-to-csv <input> <output-dir>

  input       Input .nt file
  output-dir  Directory to create (must not exist)
```

Output structure:
```
<output-dir>/
  Vertex.csv        # Vertex id list
  _vertices.txt     # URI → vertex-id mapping
  <predicate>.csv   # Edge list (src,dest) per predicate
```

Example:
```bash
./nt-to-csv wikidata-trunc.nt wikidata-csv
```

---

### `sparql-to-fa`

Converts a file of SPARQL regular path queries into per-query NFA adjacency matrix directories in Matrix-Market format.  Requires the graph to have been prepared with `nt-to-mm` first.

Input query file format (one query per line):
```
<number>,<source-URI or ?var> <regex-pattern> <target-URI or ?var>
```

Example:
```
1,<Q10281806> (<P131>)* ?x1
2,<Q11193> (<P279>)* ?x1
```

```
Usage: sparql-to-fa <queries> <graph-dir> <output-dir>

  queries     Input SPARQL queries file (after deprefix-sparql)
  graph-dir   Graph directory produced by nt-to-mm
  output-dir  Directory to create for query NFA files
```

Output structure (one subdirectory per query):
```
<output-dir>/
  <query-number>/
    meta.txt          # Source/target vertices, start/final NFA states, used labels
    raw.txt           # Original query line
    <label>.txt       # NFA transition matrix for that label in Matrix-Market format
```

Example:
```bash
./sparql-to-fa sparql-queries-trunc.txt wikidata-mm wikidata-queries
```
