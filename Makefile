clean:
	rm -fr png/ tmp/

zip: png
	mkdir -p tmp/WorldWeatherSymbols-png
	cp -f png/*.png tmp/WorldWeatherSymbols-png
	cd tmp && zip WorldWeatherSymbols-png.zip WorldWeatherSymbols-png/*.png

png:
	scripts/wws_manage.sh png
