

CHARTS=$(shell find . -maxdepth 1 -type d | xargs -I{} sh -c '[ $$(find {} -name Chart.yaml | wc -l) -gt 0 ] && echo {}')

lint:
	helm lint $(CHARTS)
