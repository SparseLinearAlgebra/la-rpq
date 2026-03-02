# Databases

This directory contains competitor graph databases and query engines used in the experiments, together with benchmarking scripts and dataset-conversion utilities specific to each system.

## Competitors

| Directory | System | Notes |
|-----------|--------|-------|
| `MillenniumDB/` | [MillenniumDB](https://github.com/MillenniumDB/MillenniumDB) (current) | State-of-the-art graph database; may cache data in RAM. Patched for URI-prefix handling. |
| `MillenniumDB-old/` | [MillenniumDB](https://github.com/MillenniumDB/MillenniumDB/tree/path_query_challenge) (path-query-challenge version) | Older version used because it supports different query semantics. Uses its own non-RDF data model. |
| `RPQ-matrix/` | [rpq-matrix](https://github.com/adriangbrandon/rpq-matrix) | Linear algebra-based RPQ evaluation using a custom sparse matrix implementation. |
| `RPQ-matrixGB/` | [rpq-matrix-GrB](https://github.com/suvorovrain/rpq-matrix/tree/gbmod) | rpq-matrix modified to use [SuiteSparse:GraphBLAS](https://github.com/DrTimothyAldenDavis/GraphBLAS) as the sparse matrix backend. |

Each subdirectory contains:

* A **submodule** with the system's source code.
* A `README.md` with build prerequisites, dataset-preparation steps, and benchmarking commands.
* A `bench` script that runs the timed experiments and collects results.
* A `requirements.txt` with Python dependencies where needed.
* Dataset-conversion scripts specific to that system's input format.

## General workflow

For each competitor the workflow is:

1. **Prepare the dataset** — convert the shared `.nt` file into the system-specific format (see each `README.md`).
2. **Build the system** — follow the instructions in the system's own `README.md` inside its submodule directory.
3. **Run the benchmark** — execute the `bench` script with the appropriate arguments.
