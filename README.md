# relestatedb — Neo4j geographic/property-data prototype

A small Python experiment for ingesting **GeoJSON feature data into Neo4j**. The original project goal was to enrich housing-related graph data with additional open datasets. This repository currently contains `ingest.py` and this README, not a published dataset or fully configured database.

## What `ingest.py` does

The script imports `neo4j.GraphDatabase` and defines a `GeoJSONImporter` class with `import_geojson`, `create_node`, and a transaction helper. It is an **ingestion/writing tool**. No pinned dependencies, migration plan, schema guarantees, or isolated test suite are supplied.

## Safe reproduction

- Obtain open GeoJSON with verified license, source, dates, geometry validity, and a declared coordinate reference system.
- Use a disposable Neo4j database and synthetic features. Inspect the `main()` connection settings, paths, credentials, and transaction behavior before running.
- Validate unique identifiers, duplicates/idempotency, geometry properties, missing values, and graph constraints before importing into any existing graph.
- Do not ingest private property-owner records, personal addresses, access tokens, or unreleased GIS datasets into public graphs or model traces.

Build out spatial indexing, lineage, update policy, reproducible fixtures, a source attribution table, and explicit query examples before treating this as an analytics database.

**Status:** source-level documentation only. No Neo4j connection, data import, or test execution performed.
