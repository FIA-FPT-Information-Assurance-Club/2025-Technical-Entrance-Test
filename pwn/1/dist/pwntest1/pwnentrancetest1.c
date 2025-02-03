#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#define VIDEO_PRICE 500
//--------------------------------file reading (ignore this)-------------------------------
void ignore_me_init_buffering() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void kill_on_timeout(int sig) {
    if (sig == SIGALRM) {
        printf("[!] Anti DoS Signal. Patch me out for testing.");
        _exit(0);
    }
}

void ignore_me_init_signal() {
    signal(SIGALRM, kill_on_timeout);
    alarm(60);
}

void readFile(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error opening the file!! Contact the workshop personnel");
        return;
    }

    // Seek to the end of the file to determine its size
    fseek(file, 0, SEEK_END);
    long fileSize = ftell(file);
    rewind(file);

    // Allocate memory to hold the file contents
    char *buffer = (char *)malloc(fileSize + 1);
    if (buffer == NULL) {
        perror("Memory allocation error. Contact the workshop personnel");
        fclose(file);
        return;
    }

    // Read the file into the buffer
    size_t bytesRead = fread(buffer, 1, fileSize, file);
    buffer[bytesRead] = '\0'; // Null-terminate the string

    // Print the file contents
    printf("%s\n", buffer);

    // Clean up
    free(buffer);
    fclose(file);
}
//-----------------------------file reading----------------------------------

//------------------------------main--------------------------------------------------------
int get_int() {
    char *buffer = (char *)malloc(64 * sizeof(char));
    if (buffer == NULL) {
        fprintf(stderr, "Memory allocation failed. Contact the workshop personnel\n");
        exit(1);
    }
    if (fgets(buffer, 64, stdin) == NULL) {
        fprintf(stderr, "Error reading input. Contact the workshop personnel\n");
        free(buffer);
        exit(1);
    }
    int result = atoi(buffer);
    free(buffer);
    return result;
}

int buy_JV(int moneyAccount){
	printf("Here we have some JV codes each costs 500k VND:\nPRO-192\nOSG-202\nDBI-202\nCSD-201\nIAM-302\nSWT-301\nCPV-301\nSWP-391\nCRY-303c\n");
	printf("You have %dk VND. How many codes do you want to buy> ", moneyAccount);
    fflush(stdout);

	int buyQuantities= get_int();
	if(buyQuantities ==0){
		printf("Don't find anything interesting :(((. Try to visit again!!");
        fflush(stdout);
		exit(0);
	}
	if(buyQuantities >0){
		int totalCost= buyQuantities * VIDEO_PRICE;
		if(totalCost <= moneyAccount){
			moneyAccount -= totalCost;
		printf("Proceeding....... You have %dk VND left\n", moneyAccount);
        fflush(stdout);
		printf("We have one special gift for you: ");
        fflush(stdout);
		readFile("flag");
		return 0;
		}
		printf("Stop it you know that you don't have enough cash!! :))");
        fflush(stdout);
		return 0;
	}
	printf("It seems like you have entered negative quantities?! What's wrong with you huh?");
}

void menu_choice(int choice, int moneyAccount){
	switch(choice){
		case 1: buy_JV(moneyAccount); break;
		case 2: printf("Thank you for visiting!!"); break;
		default: printf("It seems you have entered something not.... right!!"); break;
	}
    fflush(stdout);
}

void menu_print(){
	printf("Welcome to the Automatic Japanese Video (JV) Vending Machine");
	printf("\n----------------------u53rr007------------------------------\n");
	printf("How can I help you?\n");
	printf("1: Buy some JV\n");
	printf("2: Quit\n");
	printf("Your choice> ");
    fflush(stdout);
}

int main(){
    ignore_me_init_buffering();
	ignore_me_init_signal();
	int moneyAccount= 100;
	menu_print();
	int choice= get_int();
	menu_choice(choice, moneyAccount);
	return 0;
}
