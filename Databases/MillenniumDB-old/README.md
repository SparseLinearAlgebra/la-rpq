# Utils for benchmarking MillenniumDB old version

These are the utils we've used to benchmark [old version of MillenniumDB used in path query challenge](https://github.com/MillenniumDB/MillenniumDB/tree/path_query_challenge). It's used due to the fact it's one of a few competitors that support different query semantics.

## Prerequisites

This dependencies are needed in order for everything to work.

* A few extra Python dependencies. We'd recommend to set up a [virtual env](https://docs.python.org/3/library/venv.html).

```bash
# Set up a virtual env in .venv directory.
python -m venv ./.venv && source ./.venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

You will also need to download boost to build MillenniumDB. Check the README in the MillenniumDB repository for more information on this.

## Preparing dataset

Old versions of MillenniumDB doesn't support RDF data model (i.e. SPARQL queries and N-Triples formats). To work with it we need to convert the dataset into the MillenniumDB-specific format.

```bash
./nt-to-mdb <dataset.nt> <dataset.mdb>
```

## Running and benchmarking

After building MillenniumDB running and benchmarking can be summarized as follows.

```bash
# Assume MillenniumDB is built inside ./build dir
./MillenniumDB/build/bin/create_db <dataset.mdb> <database dir> 

# Run the benches.
# Note there are quite a few flags allowing to change semantics.
# See them all by running `./bench --help`
# By default MillenniumDB seeks for any paths, using BFS and caches.
./bench <path to dir with MillenniumDB binaries> <database> <query file>
```
