# Utils for benchmarking MillenniumDB

These are the utils we've used to benchmark [MillenniumDB](https://github.com/MillenniumDB/MillenniumDB).

## Prerequisites

This dependencies are needed in order for everything to work.

* A few extra Python dependencies. We'd recommend to set up a [virtual env](https://docs.python.org/3/library/venv.html).

```bash
# Set up a virtual env in .venv directory.
python -m venv ./.venv && source ./.venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

**Note**: by default MillenniumDB prevents using URIs without prefixes. It might be patched as follows.

```bash
cd MillenniumDB
git apply ../mdb-allow-unprefixed.patch
cd ..
```

## Running and benchmarking

After building MillenniumDB running and benchmarking can be summarized as follows.

```bash
# Assume MillenniumDB is built inside ./build dir
./MillenniumDB/build/bin/mdb-import <dataset-nt> <database dir>

# Run the benches.
./bench <path to dir with MillenniumDB binaries> <database> <query file>
```
