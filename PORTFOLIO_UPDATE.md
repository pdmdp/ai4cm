# Portfolio update — 15 November 2026

The three studies were developed for the course submission. The repository publication and the checks described here happened later, on 15 November 2026.

The published notebooks use the final submitted notebooks as their source. The changes are:

- Data and output paths now resolve from the repository root.
- The segmentation CSV loader accepts tab or semicolon delimiters and a UTF-8 byte-order mark.
- Parallel training in the customer-value notebook is limited to one worker.
- Notes about generalization, independence and campaign effects have been narrowed to what the experiments support.
- An update note and valid cell identifiers were added; notebook widget metadata and local path displays were removed.

The modeling choices, parameter grids and saved result figures are retained. The slides are byte-for-byte copies of the submitted PDFs. Input checksums, execution checks and the README figures were added during publication.

All three packaged notebooks were executed locally from start to finish. [Reproduction results](results/reproduction-check.json) record the observed values; [source comparison](results/source-comparison.json) records original file hashes and changed source cells. These checks reuse the course data and splits and are not independent validation experiments.

The repository was forked from [sbesby/ai4cm](https://github.com/sbesby/ai4cm). The inherited `setup/`, `quick-guide/`, editor configuration and `AGENTS.md` remain course scaffolding. The 15 November publication does not change that upstream repository or establish when the original coursework was written.

## Environment scope

The notebooks use paths relative to the repository root and the `ai4cm-env` kernel. Part 3 uses one training worker to limit memory consumption. The environment file describes the local analysis environment; a fresh environment solve has not been verified on every platform. Saved coursework figures remain the source for the README illustrations.
