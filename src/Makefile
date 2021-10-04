
all:
	mkdocs build

sync:
	bash sync.sh

deploy:
	git checkout main
	mkdocs gh-deploy
	git checkout gh-pages
	git add ../slides
	git commit -m 'reveal update'
	git push origin gh-pages
	git checkout main

clean:
	rm -rf site
	rm -rf ../slides
