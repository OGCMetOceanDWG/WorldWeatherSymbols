
VERSION=`cat VERSION.txt`
BASENAME=WorldWeatherSymbols-$(VERSION)-png

clean:
	rm -fr png/ tmp/

zip: png
	mkdir -p tmp/$(BASENAME)
	cp -f png/*.png tmp/$(BASENAME)
	cp README.md tmp/$(BASENAME)
	cd tmp && zip $(BASENAME).zip $(BASENAME)/*.png $(BASENAME)/README.md

png:
	scripts/wws_manage.sh png
