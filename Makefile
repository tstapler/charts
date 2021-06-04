CHARTS=$(shell find . -maxdepth 1 -type d | xargs -I{} sh -c '[ $$(find {} -name Chart.yaml | wc -l) -gt 0 ] && echo {}')
apply:
	helmfile apply --concurrency 1

lint:
	helm lint $(CHARTS)

docs: deps
	helm-docs

deps:
	@if ! hash helm-docs; then GO111MODULE=on go get github.com/norwoodj/helm-docs/cmd/helm-docs; fi
