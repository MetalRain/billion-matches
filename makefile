.PHONY : generate run build

generate: |
	@docker build ./data \
		-t billion-matches-data:latest
	@docker run \
		--volume=$(shell pwd)/data/data:/app/data \
		billion-matches-data:latest

build: |
	@docker build ./solutions/$(solution) -t billion-matches-solution:s-$(solution)

run: |
	@echo 'Running solution: $(solution)'
	@time docker run \
		--cpus=1 \
		--memory=512m \
		--volume=$(shell pwd)/solutions/$(solution)/output:/app/output:rw \
		--volume=$(shell pwd)/data/data:/app/data:ro \
		billion-matches-solution:s-$(solution)