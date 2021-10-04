
all:
	mkdocs build

sync:
	bash sync.sh

deploy:
	git checkout main
	mkdocs gh-deploy
	git checkout gh-pages
	git commit -m 'website update'
	git push origin gh-pages
	git checkout main

clean:
	rm -rf site
	rm -rf ../slides
