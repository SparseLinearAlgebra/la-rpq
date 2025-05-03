# Linear Algebra-based Regular Path Queries

This is a repository with utils that can be used to reproduce experiments described in [Single-Source Regular Path Querying in Terms of Linear Algebra paper](https://arxiv.org/abs/2412.10287). The paper is about evaluating graph Regular Path Queries using linear algebra over sparse adjacency matrices implemented using [SuiteSparse:GraphBLAS](https://github.com/DrTimothyAldenDavis/GraphBLAS).

## Datasets

Currently, we use the following datasets for the experiments information on which is available within the `Datasets` directory.

* [Wikidata snapshot from MillenniumDB path-query-challenge](https://github.com/MillenniumDB/path-query-challenge) this is a snapshot of a real-world [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page) graph and 660 queries taken from the [query log](https://iccl.inf.tu-dresden.de/web/Wikidata_SPARQL_Logs/en).
* [Yago-2S knowledge base](https://yago-knowledge.org/downloads/yago-2s) is a large knowledge base evaluated with 7 complex RPQ queries taken from [academic papers](https://openproceedings.org/2017/conf/edbt/paper-302.pdf).

## Reproducing experiments

For running the experiments in a specific environment refer to `Databases` folder with information on evaluating the experiments. These are the competitors.

* [rpq-matrix](https://github.com/adriangbrandon/rpq-matrix) is another linear algebra-based algorithm for evaluating RPQs using their own implementation of sparse matrices.
* [MillenniumDB](https://github.com/MillenniumDB/MillenniumDB) is a graph database demonstrating state-of-the-art performance among other competitors and that might cache the data to execute queries out of the RAM.
* [FalkorDB (ex. RedisGraph)](https://github.com/FalkorDB/FalkorDB) is an in-memory graph database employing [SuiteSparse:GraphBLAS](https://github.com/DrTimothyAldenDavis/GraphBLAS) sparse matrix approaches for query evaluation.
* [Memgraph](https://github.com/memgraph/memgraph) is quite advanced in-memory graph database.

## Authors

* [Semyon Grigorev](https://github.com/gsvgit) (mail: [s.v.grigoriev@mail.spbu.ru](mailto://s.v.grigoriev@mail.spbu.ru)).
* [Georgiy Belyanin](https://github.com/georgiy-belyanin) (mail: [belyaningeorge@ya.ru](mailto://belyaningeorge@ya.ru)).
* [Rodion Suvorov](https://github.com/suvorovrain) (mail: [rodion.suvorov.94@mail.ru](mailto://rodion.suvorov.94@mail.ru)).

## Acknowledgments & copyright notices

LA-RPQ is licensed under [GPL-2.0 license](https://www.gnu.org/licenses) and acknowledges the following projects and modifications made to them.

* [MillenniumDB](https://github.com/MillenniumDB/MillenniumDB) licensed under GPL-2.0 used in two different versions with modifications to the RDF prefix handling. For more information see the `./Databases/MillenniumDB` directory.
* [rpq-matrix](https://github.com/MillenniumDB/MillenniumDB) licensed under GPL-3.0 used both w/o modifications and with modifications to work with GraphBLAS.
* [Blazegraph](https://github.com/blazegraph/database) licensed under GPL-2.0 used without modifications but with custom benchmarking scripts that uses procedures from the unlicensed [MillenniumDB WDBench](https://github.com/MillenniumDB/WDBench) but configured for different datasets and only for the Blazegraph database.

We also appreciate [Vladimir Kutuev](https://github.com/vkutuev)(mail: [vladimir.kutuev@gmail.com](mailto://vladimir.kutuev@gmail.com)) for consulting us on the proper engineering approaches to use.

Thank you for you interest in the la-rpq project.
