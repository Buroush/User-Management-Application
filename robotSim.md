### Intuition
The problem requires us to simulate the movement of a robot on a grid, considering possible obstacles. The goal is to determine the maximum Euclidean distance from the origin that the robot can achieve during its movement.

### Approach
1. **Direction Handling**: The robot can face four possible directions: North, East, South, and West. These are handled using direction vectors.
2. **Command Execution**: The robot executes each command, where:
   - `-2` indicates a 90-degree left turn.
   - `-1` indicates a 90-degree right turn.
   - A positive integer `k` indicates moving `k` units in the current direction.
3. **Obstacle Handling**: We use a hash map to store obstacles and efficiently check if the robot encounters any obstacles during its movement.
4. **Distance Calculation**: After executing each command, the distance from the origin is calculated and the maximum distance squared is tracked.

### Complexity

- **Time Complexity**: 
  - Inserting obstacles into the hash map takes O(1) for each obstacle, so for `obstaclesSize` obstacles, it is O(obstaclesSize).
  - The robot processes each command sequentially. For each command of movement `k`, it checks up to `k` steps, each taking O(1) to check against obstacles. This gives a total time complexity of O(commandsSize * maxCommandLength).
  - Since each movement and obstacle check is O(1), and hash map operations (insert and lookup) are O(1), the overall time complexity is:
    - O(commandsSize + obstaclesSize)
  
- **Space Complexity**: 
  - The primary space usage is from the hash map storing the obstacles. The space complexity depends on the number of obstacles:
    *O(obstaclesSize)*
  - Additionally, we store the direction vectors and other variables, but these are constant space: *O(1)*
  
  Thus, the overall space complexity is:
    *O(obstaclesSize)*

### Code
The code you provided is well-structured and implements the approach effectively. Below is the same code with minor enhancements and comments:

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>

#define HASH_SIZE 100003

// Structure for a node in the hash map (for linked list collision handling)
typedef struct HashNode {
    int x, y;
    struct HashNode* next;
} HashNode;

HashNode* hashMap[HASH_SIZE];

// Hash function for obstacle coordinates
int hash(int x, int y) {
    return (abs(x * 30001 + y)) % HASH_SIZE;
}

// Insert an obstacle into the hash map
void insertObstacle(int x, int y) {
    int h = hash(x, y);
    HashNode* newNode = (HashNode*)malloc(sizeof(HashNode));
    newNode->x = x;
    newNode->y = y;
    newNode->next = hashMap[h];
    hashMap[h] = newNode;
}

// Check if a position is an obstacle
bool isObstacle(int x, int y) {
    int h = hash(x, y);
    HashNode* node = hashMap[h];
    while (node) {
        if (node->x == x && node->y == y) return true;
        node = node->next;
    }
    return false;
}

int robotSim(int* commands, int commandsSize, int** obstacles, int obstaclesSize, int* obstaclesColSize) {
    // Directions array: North, East, South, West
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};
    
    // Insert obstacles into hash map
    for (int i = 0; i < obstaclesSize; ++i) {
        insertObstacle(obstacles[i][0], obstacles[i][1]);
    }
    
    int x = 0, y = 0; // Robot's starting position
    int direction = 0; // Start facing North (index 0 in dx and dy)
    int maxDistSq = 0;
    
    for (int i = 0; i < commandsSize; ++i) {
        int command = commands[i];
        if (command == -2) {
            direction = (direction + 3) % 4; // Turn left 90 degrees
        } else if (command == -1) {
            direction = (direction + 1) % 4; // Turn right 90 degrees
        } else {
            // Move forward command steps
            for (int j = 0; j < command; ++j) {
                int newX = x + dx[direction];
                int newY = y + dy[direction];
                if (!isObstacle(newX, newY)) {
                    x = newX;
                    y = newY;
                    int distSq = x * x + y * y;
                    if (distSq > maxDistSq) {
                        maxDistSq = distSq;
                    }
                } else {
                    break; // Stop moving if an obstacle is encountered
                }
            }
        }
    }
    
    // Free the memory for the hash map
    for (int i = 0; i < HASH_SIZE; ++i) {
        HashNode* current = hashMap[i];
        while (current != NULL) {
            HashNode* temp = current;
            current = current->next;
            free(temp);
        }
        hashMap[i] = NULL;
    }
    
    return maxDistSq;
}
/*	Author   : Pankaj Mondal
	Date     : Wednesday, September 4, 2024, 4:20 PM
	LinkedIn : https://www.linkedin.com/in/buroush
	GitHub   : https://github.com/Buroush
	LeetCode : https://leetcode.com/Buroush        		*/
```
