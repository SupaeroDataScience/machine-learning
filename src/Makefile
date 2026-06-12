# SDD course site — Machine Learning (FSD311)
# Deployment is standardised across all SDD course repos: see DEPLOYING.md.
# Requires: pip install mkdocs mkdocs-material pymdown-extensions

serve:   ## Live-preview the site locally at http://localhost:8000
	mkdocs serve

build:   ## Build the static site into site/
	mkdocs build

deploy:  ## Build and publish the site to the gh-pages branch on origin
	mkdocs gh-deploy

clean:
	rm -rf site

# Copy docs/*.md out to the per-topic folder READMEs (repo-specific helper).
sync:
	bash sync.sh

.PHONY: serve build deploy clean sync
