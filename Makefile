all:
	gcc -fPIC -shared -O2 -o rmontage/wumanber/wumanber.so rmontage/wumanber/wumanber_impl.c

clean:
	rm -rf rmontage/wumanber/wumanber.so
