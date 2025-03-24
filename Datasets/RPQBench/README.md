# RPQbench

The provided dataset is based on [RPQBench](https://github.com/Mamenglu/LD-RPQB). We truncate this dataset from properties and convert it into matrix-market adjacency matrices for linear algebra-based algorithms and into CSVs for Memgraph and FalkorDB.

## Processing the dataset

The original dataset in the [N-triples](https://www.w3.org/TR/n-triples/) format and can be generated using `./RPQBench/LD-RPQB/bin/rpqbench_gen`.

```bash
cd RPQBench/rpqbench/bin && ./rpqbench_gen -t <triple_count> && cd ../../..
cp RPQBench/rpqbench/bin/rpqbench.n3 .

# Create a Python venv and install requirements
python -m venv ./.venv && source ./.venv/bin/activate
pip install -r requirements.txt

# Remove the properties & the prefixes from the dataset.
./truncate rpqbench.n3 | ./deprefix-nt > rpqbench-trunc.nt

# LA-RPQ (our-algorithm). Convert the truncated dataset to a set of matrix-market files.
./nt-to-mm rpqbench-trunc.nt rpqbench-mm

# FalkorDB, Memgraph. Convert the truncated dataset to a few CSV files.
./nt-to-csv rpqbench-trunc.nt rpqbench-csv

# For preparing the dataset for RPQ-matrix and MillenniumDB see the corresponding Databases dir.
```

Queries are all paths. For evaluating single-source/single destination benchmarks you need to explicitly specify the sources.

```
# Remove prefixes from the original queries.
./deprefix-sparql ./sparql-queries.txt > ./sparql-queries-trunc.txt
# Convert queries to a set of Matrix-Market files.
./sparql-to-fa ./sparql-queries-trunc.txt ./rpqbench-mm ./rpqbench-queries
```
