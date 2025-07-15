#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define the maximum size of the stack
#define MAX 100

// Structure to represent a packet
typedef struct {
    int id;                // Packet ID
    char source[50];       // Source IP
    char destination[50];  // Destination IP
    char action[10];       // Action: ALLOW or BLOCK
} Packet;

// Stack structure
typedef struct {
    Packet packets[MAX];
    int top;
} Stack;

// Initialize the stack
void initStack(Stack *stack) {
    stack->top = -1;
}

// Check if the stack is full
int isFull(Stack *stack) {
    return stack->top == MAX - 1;
}

// Check if the stack is empty
int isEmpty(Stack *stack) {
    return stack->top == -1;
}

// Push a packet onto the stack
void push(Stack *stack, Packet packet) {
    if (isFull(stack)) {
        printf("Error: Stack is full. Cannot add more packets.\n");
        return;
    }
    stack->packets[++stack->top] = packet;
    printf("Packet ID %d pushed to stack.\n", packet.id);
}

// Pop a packet from the stack
Packet pop(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Error: Stack is empty. No packets to process.\n");
        Packet empty = {-1, "", "", ""}; // Return an empty packet
        return empty;
    }
    return stack->packets[stack->top--];
}

// Peek at the top packet of the stack
Packet peek(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Error: Stack is empty.\n");
        Packet empty = {-1, "", "", ""}; // Return an empty packet
        return empty;
    }
    return stack->packets[stack->top];
}

// Simulate packet processing in a firewall
void processPackets(Stack *stack) {
    while (!isEmpty(stack)) {
        Packet packet = pop(stack);
        printf("Processing Packet ID: %d\n", packet.id);
        printf("Source: %s\n", packet.source);
        printf("Destination: %s\n", packet.destination);
        printf("Action: %s\n", packet.action);
        printf("----------------------------\n");
    }
}

int main() {
    Stack firewallStack;
    initStack(&firewallStack);

    // Simulate adding packets to the firewall stack
 Packet packet1 = {1, "192.168.1.1", "192.168.1.2", "ALLOW"};
Packet packet2 = {2, "192.168.1.2", "192.168.1.3", "BLOCK"};
Packet packet3 = {3, "192.168.1.3", "192.168.1.4", "ALLOW"};

    push(&firewallStack, packet1);
    push(&firewallStack, packet2);
    push(&firewallStack, packet3);

    // Peek at the top packet
    Packet topPacket = peek(&firewallStack);
    printf("Top Packet ID: %d (Action: %s)\n", topPacket.id, topPacket.action);
    printf("============================\n");

    // Process packets in LIFO order
    processPackets(&firewallStack);

    return 0;
}