all:
	gcc -fPIC -shared -O2 -o tmontage/wumanber/wumanber.so tmontage/wumanber/wumanber_impl.c

clean:
	rm -rf tmontage/wumanber/wumanber.so
