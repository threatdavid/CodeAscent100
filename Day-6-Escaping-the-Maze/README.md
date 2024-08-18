# Reeborg's World: Lost in the Maze Solution

Reeborg was exploring a dark maze when the battery in its flashlight ran out. The objective is to guide Reeborg to the exit using an efficient strategy.

### Key Details

- **Functions Used**: `move()`, `turn_left()`

- **Conditions**: `front_is_clear()`, `right_is_clear()`, `is_facing_north`, `at_goal()`

- **Loop and Control Structures**: `while` loop, `if/elif/else` statements

- **Important Note**: Reeborg should follow the right edge of the maze, turning right whenever possible, moving straight if it can't turn right, and turning left as a last resort.

## Solution Strategy
This solution builds upon the standard right-hand rule, with enhancements to handle specific edge cases:

 1. **Downward Positioning**: If Reeborg is at the bottom of the maze and needs to move upward, it checks if the right side is clear and if it is facing north to determine the correct movement.
 2. **Central Positioning**: If Reeborg is in the middle of the maze with no walls on any side, the solution still ensures that Reeborg finds its way to the exit.

### Pseudocode Outline

 1. **Check if Reeborg is at the goal**: If yes, stop. 
 2. **Straight Movement**: If the path straight ahead is clear, move forward. Then, check if the right side is clear: - If yes, turn right. - If Reeborg is not facing north after turning right, turn left to correct its direction. 
 3. **Right Turn**: If the path ahead is not clear but the right side is, turn right. 
 4. **Left Turn**: If neither front nor right is clear, turn left.
 5. **Loop**: Continue this process until Reeborg reaches the goal.

## Code Implementation
```python 
def turn_right(): 
	turn_left() 
	turn_left() 
	turn_left() 

while not at_goal(): 
	if front_is_clear(): 
		move() 
		if right_is_clear(): 
			turn_right() 
			if not is_facing_north(): 
				turn_left() 
	elif right_is_clear(): 
		turn_right() 
	else: 
		turn_left()
```

## Explanation

![enter image description here](https://res.cloudinary.com/dqkuzohnx/image/upload/v1724025098/Lost-in-the-Maze_awryyq.png)

- **`turn_right()`**: Defined as three consecutive `turn_left()` calls to make Reeborg turn 90 degrees to the right.

- **`while not at_goal():`** Reeborg will continue to execute the instructions inside this loop until it reaches the goal.

- **`front_is_clear():`** Reeborg moves forward if the path is clear. After moving, it checks if the right side is clear: If yes, Reeborg turns right and checks if it is facing north. If not, it turns left to correct its direction.

- **`right_is_clear():`** If the path ahead is blocked but the right side is clear, Reeborg turns right.

- **`else:`** If neither front nor right is clear, Reeborg turns left.

## Handling Edge Cases

1. **Bottom of the Maze:**
   - When Reeborg is at the bottom and needs to move upward, it checks the right side and its direction. If the right is clear but Reeborg is not facing north, it adjusts its direction accordingly.

2. **Center of the Maze:**
   - When Reeborg is in the middle of the maze without walls on any side, this solution ensures that Reeborg doesn't get stuck and eventually finds the exit by carefully checking each direction.

## Conclusion

This enhanced solution ensures that Reeborg can navigate more complex mazes, handling specific scenarios that could cause issues in a simpler approach. By considering the bot's orientation and surroundings, this approach provides a robust method to ensure Reeborg reaches the goal.
