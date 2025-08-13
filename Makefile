
# Minimal Makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

.PHONY: help clean html

help:
	@echo "Makefile for Sphinx documentation"
	@echo
	@echo "Usage:"
	@echo "  make html      to build the HTML documentation"
	@echo "  make clean     to clean the built docs"

html:
	$(SPHINXBUILD) -b html $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

clean:
	rm -rf $(BUILDDIR)/*
