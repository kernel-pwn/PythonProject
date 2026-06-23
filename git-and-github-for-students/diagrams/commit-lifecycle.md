# Commit lifecycle (Mermaid)

Shows Working directory → Staging → Local commit → Remote → Collaborators.

```mermaid
flowchart LR
  W[Working directory] --> S[Staging area (git add)]
  S --> L[Local repo (git commit)]
  L --> R[Remote (git push)]
  R --> C[Collaborators (git pull)]
```
