#include <stdio.h>
#include <string.h>

int checkRegistrationKey(char name[22], char key[22]);

int main(int argc, char const *argv[]) {
	char name[22];
	char key[22];

	puts("Enter username: ");
	fgets(name, sizeof(name), stdin);

	puts("Enter your registration key: ");
	fgets(key, sizeof(key), stdin);
	
	if(checkRegistrationKey(name, key) == 1) {
		puts("Try again...");
	} else {
		puts("Well done!!");
	}
}

int checkRegistrationKey(char name[22], char key[22]) {
	
	if((strlen(name) != strlen(key)) || ((int)name[0] == 10 || (int)key[0] == 10)) {
		return 1;
	}
	for(int i = 0; (int)name[i] != 10; i++) {
		if((int)name[i] % 10 != (key[i] - '0')) {
			return 1;
		} else {
			continue;
		}
	}
	return 0;
}