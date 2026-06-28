# DO NOT MOVE OR DELETE `CNAME`

The `CNAME` file in this directory is **load-bearing infrastructure**, not a
normal file. GitHub Pages reads it on every build and rewrites the repo's
custom-domain setting to match it.

- It must live **at the repo root** (Pages serves this site from `main` `/`).
- Its only content is the custom domain: `www.quay-cncpts.com`.

If `CNAME` is moved out of the served folder, deleted, or rapidly
deleted-then-recreated, GitHub Pages **drops the custom domain** and can leave
it in a stuck "claimed but unattached" state that requires unpublishing and
republishing the Pages site to recover.

## Rules for any future restructuring

- Never relocate `CNAME` when moving the site folder. If the served path
  changes, the `CNAME` goes wherever Pages serves from and nothing else.
- Never delete `CNAME` "to clean up." It controls the live domain.
- A change scoped to design (favicon, CSS, copy) must not touch this file.
