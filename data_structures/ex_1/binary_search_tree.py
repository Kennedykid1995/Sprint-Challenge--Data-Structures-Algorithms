class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    #create an empty stack
    stack=[self]
    #append the self to the stack
    while stack:
      #create a object that holds the values within stack
      current = stack.pop()
      #find out whether the right or left side has any values, if so then append the current.value right or left.
      if current.right:
        stack.append(current.right)
      if current.left:
        stack.append(current.left)
      #invoke the callback function
      cb(current.value)

  def breadth_first_for_each(self, cb):
    #create a object called queue and add the root to it
    queue = [self]
    #loop through the queue to find the values within the branches
    while queue:
        leaf = queue.pop(0)
        #if there is a leaf on the left then add to the queue
        if leaf.left:
            queue.append(leaf.left)
        #if there is a leaf on the right add to the queue
        if leaf.right:
            queue.append(leaf.right)
        #invoke the callback function
        cb(leaf.value)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
