#Program of function to separate even and odd elements of a list

def eve_odd():
    li = []
    li_even = []
    e = 0
    li_odd = []
    o = 0

    limit = int(input("Enter number of elements: "))

    for i in range(0,limit):
        li.append(int(input(f"Enter element {i}: ")))
        if(li[i]%2==0):
            li_even.append(li[i])
            e = e+1
        else:
            li_odd.append(li[i])
            o = o+1

    print(f"List of even numbers is: {li_even}")
    print(f"List of odd numbers is: {li_odd}")

eve_odd()