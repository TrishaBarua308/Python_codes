# write function overrides existing text
with open('name.txt','w') as f:
    f.write("I am a programmer.\n")
    f.write("I love to do code everyday.")

# append to write over text
with open('name.txt', 'a') as f:
    f.write("\nC++")
    f.write("\nPython")
    f.write("\nJava")
    f.write("\nC")

line = ['\nTrisha Barua\n', 'BSc in CSE\n','Learner\n']

with open('name.txt','a') as f:
    f.writelines(line)