
VERSION=$(shell cat VERSION.txt)
BASENAME=WorldWeatherSymbols-$(VERSION)-png

clean:
	rm -fr png/ tmp/

dist: png
	mkdir -p tmp/$(BASENAME)
	cp -f symbols/png/*.png tmp/$(BASENAME)
	cp README.md tmp/$(BASENAME)
	cd tmp && zip $(BASENAME).zip $(BASENAME)/*.png $(BASENAME)/README.md

png:
	scripts/wws_manage.sh png
