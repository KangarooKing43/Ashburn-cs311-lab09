# CS311 Lab 10 The Priority Triage

**Instructor starter:** https://github.com/cwillpinto/cs311-lab10-priority-triage  
**Due:** Wednesday, November 4, 2026 at 11:59 PM Central  
**Task:** [Lab_10_The_Priority_Triage.md](Lab_10_The_Priority_Triage.md)

This repository is an intentionally incomplete student starter. Read the task and complete the TODOs. 

## Work in your own repository

Choose **Use this template** on the instructor repository and create a repository under your own GitHub account. Clone your repository, work there, and push to your `origin`. If you clone the instructor repository directly, create an empty repository in your account, then run:

```sh
git remote rename origin upstream
git remote add origin <your-repository-url>
git remote -v
git push -u origin <your-branch>
```

Check both URLs and your branch before pushing. Never push student work to the instructor starter.

## Check and submit

Run `python test_triage.py` from the repository root. The supplied starter must fail at unfinished TODOs; the success token is earned only after the implementation and harness pass. The token does not grade written reasoning.

Submit through Blackboard: `Lab10_Theory.pdf` (or `.md`), completed `test_triage.py`, and its Success Token. Include your own repository URL and exact commit SHA as evidence. Confirm the Blackboard item and due setting before submitting.


## Your repository and Blackboard evidence

Use **Use this template** on the instructor repository to create a copy under
your own GitHub account. Clone your copy and work there. Do not push completed
work to the instructor repository.

For direct cloning, create an empty repository under your own account first:

```sh
git clone https://github.com/cwillpinto/cs311-lab10-priority-triage
cd cs311-lab10-priority-triage
git remote rename origin upstream
git remote add origin <your-student-owned-repository-url>
git remote -v
git branch --show-current
git push -u origin main
```

Replace the placeholder with your repository URL. Before pushing, verify that
`origin` points to your account and `upstream` points to `cwillpinto`. Use your
actual branch name if it is not `main`. Submit your repository URL and the
output of `git rev-parse HEAD` in Blackboard, alongside the required files and
execution evidence. Blackboard remains the official submission location.
