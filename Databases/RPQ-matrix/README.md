# Utils for benchmarking rpq-matrix

These are the utils we've used to benchmark [rpq-matrix](https://github.com/adriangbrandon/rpq-matrix).

## Prerequisites

This dependencies are needed in order for everything to work.

* A few extra Python dependencies. We'd recommend to set up a [virtual env](https://docs.python.org/3/library/venv.html).

```bash
# Set up a virtual env in .venv directory.
python -m venv ./.venv && source ./.venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Extra dataset preparements.

At first you need to use rpq-matrix-specific converter to convert the dataset into the desired format.

```bash
./nt-to-rpqm-txts <dataset.nt> <output dir> <output name>
```

**Note** this would also print you a parameters of the graph. You will need them later. Make sure to write them down somehow.

```
Successfully converted ./dataset.nt
Triples: 1000, vertices: 100, predicates: 5
```

Then you might follow README instructions in rpq-matrix to prepare the dataset.

## Running and benchmarking

After preparing the dataset it might be run as follows.

```bash
./bench <rpq-matrix build dir> <dataset dir>/<dataset name.dat> <queries> <predicate count> <triples count>
```
