<!-- ABN-BADGES -->
# StageRAG Production Automation Pack

<p align="center">
  <a href="https://3km-collab.github.io/stagerag-production-automation-pack-11/"><img alt="Live Demo" src="https://img.shields.io/badge/Live%20Demo-View%20Site-6366f1?style=for-the-badge"></a>
  <a href="#"><img alt="Download Package" src="https://img.shields.io/badge/Download%20Package-Get%20Now-22d3ee?style=for-the-badge"></a>
  <img alt="Made by RAGForge" src="https://img.shields.io/badge/by-RAGForge-10b981?style=for-the-badge">
</p>

[**Live Demo**](https://3km-collab.github.io/stagerag-production-automation-pack-11/) · [**Download the package**](#)

---

# StageRAG Production Automation Pack

A production-ready Python package by **RAGForge** (automation_kits). Ships with a
FastAPI service, a deterministic synthetic-data generator, a pytest suite,
Docker, Postman, automation presets, and 1,000+ sample records.

## Features
- Modular FastAPI service (app/) with logging and error handling
- Deterministic generator (seedable) — privacy-safe synthetic data
- pytest suite that actually runs
- Docker + docker-compose, Makefile, .env.example
- Ready sample data: CSV, JSON, SQL schema (1,000+ records)
- Postman collection for instant API testing
- Importable presets/ for automation

## Structure
```
stagerag_production_automation_pack/
  main.py  models.py  generator.py  config.py  logging_conf.py
tests/test_main.py
presets/  sample_data/  scripts/
Dockerfile  docker-compose.yml  Makefile  requirements.txt  QUICKSTART.md
```

## Install
```bash
pip install -r requirements.txt
make run
```

See `QUICKSTART.md` for the 3-step setup.
