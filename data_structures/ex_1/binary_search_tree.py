class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    #create an empty stack
    stack=[]
    #append the self to the stack
    stack.append(self)
    if stack > 0:
      #create a object that holds the values within stack
      current = stack.pop()
      #give the callback function current.
      cb(current.value)
      #find out whether the right or left side has any values, if so then append the current.value right or left.
      if current.right is not None:
        stack.append(current.right)
      if current.left is not None:
        stack.append(current.left)

  def breadth_first_for_each(self, cb):
    
    pass

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
