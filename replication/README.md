# Replication README

## Environment

- Python 3.10+
- Dependencies in `requirements.txt`

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## Verify

```bash
python3 -m pytest examples/mini-economics/tests
python3 examples/mini-economics/src/analysis.py
```

## Expected Output

The analysis script prints a small synthetic Phillips-curve regression summary.

## Known Limitations

The bundled example uses synthetic data for teaching only. Do not interpret it as
an empirical result.
