# Night Sky Planner

Night Sky Planner coordinates telescope windows, weather holds, and alert routing.

## Readiness review

The `readiness-pass` branch is staged for the next scheduling exercise.

### 🔭 Scheduling Readiness Queue

- [ ] `ops/telemetry.py:2` | WATCH | redact station credentials from diagnostic events
- [ ] `scheduler/alerts.py:3` | LATER | route weather holds to the overnight operator
- [ ] `scheduler/windows.py:2` | WATCH | reject windows ending before they begin
- [ ] `scheduler/windows.py:4` | LATER | collapse adjacent windows for the same instrument
- [ ] `tests/test_windows.py:2` | WATCH | cover a reservation spanning midnight UTC

## Review procedure

Run the scheduler tests and inspect the queue before authorizing an observing night.
