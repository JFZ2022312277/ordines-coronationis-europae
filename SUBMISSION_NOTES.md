# Speculum Submission Notes

This folder is the lean public-review package for **Ordines Coronationis Europae**. It is separate from the working development folder and should be the folder uploaded to a public static host or archived for review.

## Recommended Live URL

After hosting this folder, use the URL of `index.html` as the live site URL, e.g.

`https://YOUR-USER.github.io/ordines-coronationis-europae/`

Recommended reviewer entry points:

- `#/map`
- `#/detail/OCF-XV`
- `#/detail/ECR-XIII`
- `iiif/viewer.html?manifest=ECR-XIII-LIBER-REGALIS`

## Recommended DOI/PURL Workflow

1. Upload this folder, or a zipped release of this folder, to Zenodo or an institutional repository.
2. Include `README.md`, `PROJECT.md`, `metadata.json`, and `CITATION.cff` in the archived release.
3. Use the issued DOI/PURL as the catalogued version requested by the Speculum form.
4. Use the public web-hosted URL as the live version requested by the form.

## What Was Excluded

Large scratch files, OCR working files, source PDFs, backups, and nonessential local image caches are excluded. The very large local `gcf-fr2813` image cache is omitted from this submission package to keep the public version lightweight. Core data, map layers, OpenAtlas-style JSON/CSV, OCF/HRE/ECR/PRG entities, and the Liber Regalis demonstration assets are retained.

## Lean package cleanup

This submission folder removes oversized or incomplete local facsimile experiments and keeps the core public review paths: the interactive site, OpenAtlas-style data, OCF-XV case-study data, ECR-XIII Liber Regalis data, and the Liber Regalis IIIF demonstration manifest. The original working project remains unchanged in its source folder.

