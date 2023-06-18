#include "names.h"

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define GOAL_SCORE 100

// Initializing the Pig
typedef enum { JOWLER, RAZORBACK, TROTTER, SNOUTER, SIDE } pig_position;

// Pig Probabilities
const pig_position pig[7] = {
    SIDE,
    SIDE,
    RAZORBACK,
    TROTTER,
    SNOUTER,
    JOWLER,
    JOWLER,
};

// function prototypes
int roll_pig(void);
void play_game(int num_players, unsigned int seed);

int main(void) {
    int num_players = 2;
    unsigned seed = 2023;

    printf("Number of players (2 to 10)? ");
    int scanf_result = scanf("%d", &num_players);

    if (scanf_result < 1 || num_players < 2 || num_players > 10) {
        fprintf(stderr, "Invalid number of players. Using 2 instead.\n");
        num_players = 2;
    }

    printf("Random-number seed? ");
    int num_assignments = scanf("%u", &seed);

    if (num_assignments < 1) {
        fprintf(stderr, "Invalid seed. Using 2023 instead.\n");
        seed = 2023;
    }

    play_game(num_players, seed);

    return 0;
}

int roll_pig(void) {
    int roll = rand() % 7;
    return pig[roll];
}

void play_game(int num_players, unsigned int seed) {
    int scores[MAX_PLAYERS] = { 0 };
    int current_player = 0;
    int winner = -1;
    int jval, rval, tval, sval, val;
    int turn = 1;

    srand(seed);

    while (winner == -1) {

        printf("%s\n", player_name[current_player]);
        turn = 1;

        while (turn == 1) {

            int position = roll_pig();

            switch (position) {
            case JOWLER:
                jval = 5;
                scores[current_player] += jval;
                printf(" rolls %d, has %d\n", jval, scores[current_player]);
                break;

            case RAZORBACK:
                rval = 10;
                scores[current_player] += rval;
                printf(" rolls %d, has %d\n", rval, scores[current_player]);
                break;

            case TROTTER:
                tval = 10;
                scores[current_player] += tval;
                printf(" rolls %d, has %d\n", tval, scores[current_player]);
                break;

            case SNOUTER:
                sval = 15;
                scores[current_player] += sval;
                printf(" rolls %d, has %d\n", sval, scores[current_player]);
                break;

            case SIDE:
                val = 0;
                scores[current_player] += val;
                printf(" rolls %d, has %d\n", val, scores[current_player]);
                turn = 0;
                break;
            }

            if (scores[current_player] >= GOAL_SCORE) {
                // check for winner
                winner = current_player;
                printf("%s won!\n", player_name[winner]);
                break;
            }
        }
        current_player = (current_player + 1) % num_players;
    }
}

