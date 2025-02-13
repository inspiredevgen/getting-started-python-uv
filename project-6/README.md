# DuckDB with Python

```bash
# Initialize a Project with uv
uv init project-6

# change dir
cd project-6

# Creating a virtual env. with Python3.12
uv venv python3.12

# Activate Virtual env

source .venv/bin/activate

# Install duckdb
uv add duckdb

## Output ...
Resolved 2 packages in 242ms
Prepared 1 package in 4.06s
Installed 1 package in 6ms
 + duckdb==1.2.0
```

uv run app.py
┌────────┬───────────────┬──────────┬───────┬───────────┬─────────┐
│ car_id │ brand │ model │ year │ city │ state │
│ int32 │ varchar │ varchar │ int32 │ varchar │ varchar │
├────────┼───────────────┼──────────┼───────┼───────────┼─────────┤
│ 1 │ Tesla │ Model Y │ 2024 │ Toronto │ ON │
│ 2 │ Mercedes-Benz │ GLE │ 2022 │ Montreal │ QC │
│ 3 │ Nissan │ Murano │ 2019 │ Vancouver │ BC │
│ 4 │ Toyota │ Rav4 │ 2015 │ Calgary │ AB │
│ 5 │ Ford │ Explorer │ 2022 │ Oakville │ ON │
└────────┴───────────────┴──────────┴───────┴───────────┴─────────┘
