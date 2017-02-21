from copy import deepcopy

class SearchNode:
    def __init__(self, assignments):
        self.assignments = assignments
        
    def successors(self, explore_idxs, delta):
        succs = []
        for i in explore_idxs:
            pos_delta_assignments = deepcopy(self.assignments)
            pos_delta_assignments[i] += delta
            succs.append(SearchNode(pos_delta_assignments))
            neg_delta_assignments = deepcopy(self.assignments)
            neg_delta_assignments[i] -= delta
            succs.append(SearchNode(neg_delta_assignments))
        return succs
    
    def __repr__(self):
        return "{" + str(self.assignments) + "}"
    
if __name__ == '__main__':
    root = SearchNode([0, 0, 0, 0])
    print root.successors([0, 2], 1)