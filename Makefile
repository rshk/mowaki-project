TARGETS = requirements.txt requirements-dev.txt

all: $(TARGETS)

requirements.txt: pyproject.toml
	poetry export --without-hashes > $@

requirements-dev.txt: pyproject.toml
	poetry export --without-hashes --with dev > $@

clean:
	rm -f $(TARGETS)
