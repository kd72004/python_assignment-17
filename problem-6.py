# with the help of add function we are not able to
# add unhashable value in set list is mutable
# and all mutable values are unhashable
s={'java','python','cpp'}
l=['c','django']
s.update(l)
print(s)
