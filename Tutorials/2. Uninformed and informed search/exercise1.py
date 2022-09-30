import time
from eightpuzzle import eightpuzzle

class node:
    def __init__(self, s, parent=None, g=0, h=0, action=None):
        self.s = s
        self.parent = parent
        self.g = g
        self.f = g+h
        self.action = action
    
    def heuristic(s, goal):
        h = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                h += 1
        return h

puzzle = eightpuzzle(mode='medium')
init_state = puzzle.reset()


if __name__ == "__main__":
    start_time = time.time()
    goal_state = puzzle.goal()
    root_node = node(s=init_state, parent=None, g=0, h=node.heuristic(s=init_state, goal=goal_state))
    fringe = [root_node]

    solution_node = None
    while len(fringe) > 0:
        current_node = fringe.pop(0)
        current_state = current_node.s
        if current_state == goal_state:
            solution_node = current_node
            break
        else:
            available_actions = puzzle.actions(s=current_state)
            for a in available_actions:
                next_state = puzzle.step(s=current_state, a=a)
                new_node = node(s=next_state, parent=current_node, g=current_node.g+1, h=node.heuristic(s=next_state, goal=goal_state), action=a)
                fringe.append(new_node)
            fringe.sort(key=lambda x: x.f)
    
    if solution_node is None:
        print("Solution not found!")
    else:
        action_sequence = []

        next_node = solution_node
        while True:
            if next_node == root_node:
                break

            action_sequence.append(next_node.action)
            next_node = next_node.parent
        action_sequence.reverse()
        print("Number of moves: %d" % solution_node.g)

    # The following commented code is what GitHub Copilot suggested
    """ goal = puzzle.goal()
    start = node(init_state, None, 0, node.heuristic(init_state, goal), None)
    frontier = [start]
    explored = []
    while frontier:
        frontier.sort(key=lambda x: x.f)
        current = frontier.pop(0)
        explored.append(current)
        if current.s == goal:
            print('Goal found!')
            break
        for action in puzzle.actions(current.s):
            child = node(puzzle.step(current.s, action), current, current.g+1, node.heuristic(puzzle.step(current.s, action), goal), action)
            if child not in explored and child not in frontier:
                frontier.append(child)
    action_sequence = []
    while current.parent:
        action_sequence.append(current.action)
        current = current.parent
    action_sequence.reverse()
    print(action_sequence) """

    elapsed_time = time.time() - start_time
    print("Elapsed time: %.2f seconds" % elapsed_time)
    

    puzzle.show(s=init_state, a=action_sequence)