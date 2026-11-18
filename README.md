# Minecraft CI Learning Lab

A small educational project. It **does not** connect to Minecraft; it models tick-time samples so you can learn GitHub Issues, pull requests, reviews and Actions.

## Run tests

```bash
python -m unittest discover -v
```

The `.github/workflows/ci.yml` workflow automatically runs these tests on GitHub whenever a push or pull request occurs (provided Actions is enabled).

## Suggested practice

1. Create your own GitHub repository and upload this project, preserving the `.github/workflows/ci.yml` path.
2. Inspect the green Actions result.
3. Open an Issue titled `Add regression coverage near the 50 ms budget` to test that 50.0 ms is not overloaded but 50.1 ms is overloaded.
4. Create a feature branch `exercise/break-budget`, change `>` to `>=` in `overloaded`, commit and push it.
5. Open a pull request to `main`. Inspect the expected failed CI check.
6. Change `>=` back to `>`, and add a new unit test for `overloaded([50.1])` that expects True. Commit and push again; CI should turn green. The PR now contains a meaningful new test.
7. Review `Files changed`, explain that you temporarily introduced a regression to demonstrate CI, and merge only after checks pass.

Note: This is an intentionally simple numerical example, **not** an authoritative Minecraft performance metric. Averaging MSPT can hide tail latency; production performance testing should also report p95/p99 and use representative gameplay workloads.
