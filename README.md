# Night Sky Planner

Night Sky Planner coordinates telescope windows, weather holds, and alert routing.

## Readiness review

The `readiness-pass` branch is staged for the next scheduling exercise.

### 🔭 Scheduling Readiness Queue

- [ ] `scheduler/legacy.py:7` | LATER | retire the old local-time parser
- [ ] `scheduler/windows.py:9` | WATCH | reject malformed reservations

## Review procedure

Run the scheduler tests and inspect the queue before authorizing an observing night.
