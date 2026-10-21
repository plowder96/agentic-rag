# Agentic RAG

A basic agentic Retrieval-Augmented Generation (RAG) project built in Python.

The project is intended as a learning environment for understanding how document indexing, retrieval, and an LLM-powered agent can work together to answer questions using a controlled set of source documents.

## Overview

The system currently follows a simple RAG workflow:

1. Load source documents.
2. Split the documents into searchable chunks.
3. Generate embeddings for the chunks.
4. Store the indexed data for retrieval.
5. Accept a user question.
6. Retrieve relevant document chunks.
7. Provide the retrieved context to an agent.
8. Generate an answer based on the retrieved information.

The project is being structured so that **indexing** and **agent runtime** are separate processes.

```text
Documents
    |
    v
Indexing Pipeline
    |
    v
Vector Store / Index
    |
    v
Retriever
    |
    v
Agent
    |
    v
Answer
```

## Project Structure

```text
.
├── config.py
├── indexing.py
├── init_agent.py
├── retriever.py
└── agentic_rag.py
```

### `config.py`

Contains shared configuration used by the application.

### `indexing.py`

Responsible for preparing source documents for retrieval, including document loading, chunking, embedding, and index creation.

### `retriever.py`

Defines the retrieval interface used to search the indexed documents for relevant context.

### `init_agent.py`

Responsible for configuring and creating the agent and registering the tools available to it.

### `agentic_rag.py`

Application entry point. Handles the runtime flow between the user, agent, and retrieval system.

## Design Goals

The project currently focuses on:

- understanding the basic architecture of RAG systems
- separating indexing from query-time execution
- keeping retrieval logic independent from agent logic
- experimenting with tool-using agents
- learning how retrieved context is passed to an LLM
- gradually adding more agentic behavior without hiding the underlying mechanics

## Current Status

This project is under active development.

The current refactor is focused on separating two major concerns:

**Indexing**

```text
documents -> chunks -> embeddings -> stored index
```

**Runtime**

```text
question -> agent -> retriever -> relevant context -> answer
```

The goal is for indexing to run only when the document collection changes, while the agent runtime can repeatedly query the existing index.

## Purpose

This repository is primarily a learning project rather than a production-ready RAG framework.

The emphasis is on building the individual pieces explicitly and understanding how they interact before introducing more abstraction.
