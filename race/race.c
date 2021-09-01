#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

int main(int argc, char **argv, char **envp) {
 	setreuid(0, 0); // needed to pass access()
	struct stat buf;
	lstat(argv[1], &buf);
	if (S_ISLNK(buf.st_mode)==0 && access(argv[1], R_OK) == 0 && strstr(argv[1], "flag") == 0) {
		long c =0;
		for (long i=0; i<100000000; i++) c++;
		sendfile(1, open(argv[1], 0), 0, 0x1000);
	} else {
		puts("Cannot access this!");
	}
}
