# Bryte Eval Use Cases — R105

## Project Overview
A static data visualization report for Bryte AI (R105) containing 28 eval use cases across 6 scorecards covering every scorecard criterion. Includes sections for Common Checks, Simple Q&A, Multi-step, Emotional, Error & Recovery, Agent Handoffs, and Session & Memory.

## Tech Stack
- Pure HTML5 + CSS3 (single file: `eval-use-cases-review.html`)
- Python `http.server` for local serving via `serve.py`

## Project Structure
- `eval-use-cases-review.html` — Main report file (all content, styles, and visualizations)
- `serve.py` — Simple Python HTTP server that redirects `/` to the HTML report on port 5000
- `replit.md` — This file

## Running Locally
The "Start application" workflow runs `python3 serve.py`, serving the report on port 5000.

## Deployment
Configured as a static deployment with the root directory (`.`) as the public directory.

## GitHub Integration
Connected to `UKG-Sandbox/kq-CIRT-usecases` via the Replit GitHub integration for pulling updates.
