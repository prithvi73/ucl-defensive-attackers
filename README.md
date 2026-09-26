# Champions League Defensive Attackers Analysis ⚽📊

An end-to-end Python data science project analyzing UEFA Champions League player data to identify the most defensively active forwards. 

## The Objective
Modern football requires attackers to press high, disrupt build-up play, and win the ball back. This project processes raw UCL dataset files to isolate forwards and evaluates their defensive work rate using a custom mathematical metric.

## The Metric: Total Defensive Impact
Relying solely on "Tackle Success %" is flawed because it artificially rewards players with very low defensive volume (e.g., 1 tackle attempted, 1 won = 100%). To accurately measure high-work-rate attackers, this project combines direct tackling with spatial awareness:

**Total Defensive Impact = Tackles Won + Balls Recovered**

## Key Findings
* **The Top Performer:** Dan Ndoye took the #1 spot with a Total Defensive Impact of 20.0 and a solid 66.6% tackle success rate.
* **The Pressing Anomaly:** Julián Alvarez ranked in the top 10 despite having a 0.0% tackle success rate. His high placement is entirely driven by recovering loose balls, validating the decision to track recoveries alongside traditional tackles to measure true defensive work rate.

## Tech Stack
* **Language:** Python
* **Data Processing:** Pandas (dataset merging, Boolean filtering, handling NaN values, custom metric calculation)
* **Visualization:** Matplotlib (side-by-side subplot dashboard comparing tackle efficiency and overall impact)
* **Version Control:** Git & GitHub

## How to Run Locally
1. Clone the repository: `git clone https://github.com/prithvi73/ucl-defensive-attackers.git`
2. Install dependencies: `pip install pandas matplotlib`
3. Execute the analysis: `python main.py`