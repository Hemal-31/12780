# Notification Prioritization System

## Objective

The system fetches notifications from the API and displays the top 10 notifications based on priority and recency.


Redesign the system which will fetch the notifications from the API and it will displays only the top 10 notifications to the students so that they can get the get the most prioritied task first and they can complete it 
## Priority Rules

Priority order:

1. Placement ( This is considered to be the top priority because if we didn't        complete in time we will loose and opportunity)

2. Result ( This will goes to second place I know this is also important but considering to placement , placements is very important . We can see the Results everytime we want but Placements is not like that.)
3. Event ( This is last priorited task because comparing the above two this is not that much important .)

Notifications belonging to the same category are sorted using timestamp, with newer notifications appearing first.

## Approach

1. Fetch notifications from API.
2. Assign priority scores.
3. Convert timestamps into comparable values.
4. Sort notifications using:
   - Priority score (descending)
   - Timestamp (descending)
5. Return top 10 notifications.
6. Students can get most priorited task at top.

## Server used

Python

Notifications are stored in a list and sorted using Python's built-in sorting function.

Benefits:
- Faster updates
- Lower memory usage
- Efficient top 10 retrieval

