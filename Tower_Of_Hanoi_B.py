#Write a program to solve Tower of Hanoi puzzle
def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)

# Input the number of disks
num_disks = int(input("Enter the number of disks: "))

# Call the tower_of_hanoi function
tower_of_hanoi(num_disks, 'A', 'B', 'C')
