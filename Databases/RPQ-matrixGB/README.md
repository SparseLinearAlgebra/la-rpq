
# Utils for benchmarking rpq-matrix

These are the utils we've used to benchmark [rpq-matrix-GraphBLAS](https://github.com/suvorovrain/rpq-matrix/tree/gbmod).

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

At first you need to remove duplicates from database.
```bash
python3 remove-dups dataset-with-dups.nt > dataset.nt
```

Then use rpq-matrix converter to convert the dataset into the matrix market format.

```bash
./nt-to-mm dataset.nt <output name>
```

**Note** this would also print you a parameters of the graph. You will need them later. Make sure to write them down somehow.

```
Successfully converted ./dataset-no-dups.nt
Triples: 1000, vertices: 100, predicates: 5
```

Then in output dir do following steps:
```bash
mv edges.txt dataset.dat.P; mv vertices.txt dataset.dat.SO
mkdir dataset.dat.baseline-64; mv *.txt dataset.dat.baseline-64
```
Now swap columns in SO and P files

```bash
../swap.sh dataset.dat.P
../swap.sh dataset.dat.SO
```
Convert files with predicate matrices
```bash
../txt-to-mat dataset.dat.baseline-64
```



## Running and benchmarking

After preparing the dataset change define macros at 10th line of `./rpq-matrixgb/include/solver` to your predicates number obtained on previous step. Then rebuild the library.

Then this it might be run as follows:
```bash
./bench <rpq-matrix build dir> <dataset dir>/<dataset name.dat> <queries> <predicate count> <triples count>
```