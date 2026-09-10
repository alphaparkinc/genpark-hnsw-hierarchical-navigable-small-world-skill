# genpark-hnsw-hierarchical-navigable-small-world-skill

[![CI](https://github.com/alphaparkinc/genpark-hnsw-hierarchical-navigable-small-world-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/alphaparkinc/genpark-hnsw-hierarchical-navigable-small-world-skill/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> Hierarchical Navigable Small World (HNSW) vector search graph engine with skip-list layered routing, greedy nearest neighbor search, and cosine distance.

## Architecture

```mermaid
flowchart TD
    Client[AI Agent / Spatial Query] -->|Coordinates / Vector| Engine[genpark-hnsw-hierarchical-navigable-small-world-skill]
    Engine --> SpatialIndex[Spatial Index / Hyperplane Graph]
    SpatialIndex --> Neighbors[(Nearest Neighbors / MBR Matches)]
```

## Features
- Pure standard library Python implementation with strictly zero pip dependencies.
- Sub-linear multi-dimensional spatial and vector indexing algorithms.
- Native Model Context Protocol (MCP) server support for AI agent spatial intelligence.

## Installation

```bash
git clone https://github.com/alphaparkinc/genpark-hnsw-hierarchical-navigable-small-world-skill.git
cd genpark-hnsw-hierarchical-navigable-small-world-skill
```

## Quickstart

```bash
python example_usage.py
```
