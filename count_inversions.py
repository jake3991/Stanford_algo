def count_inversions(input):
    #define a single element list to keep track of inversions
    count=[0]
    
    def merge(left,right):
        #init some varibles
        output=[]
        i,j=0,0

        #loop while the indexes i and j are less than the length of left and right
        while i < len(left) and j < len(right):
            #if the left is bigger than the right append the left an increase the step i by 1
            if left[i] <= right[j]:
                output.append(left[i])
                i+=1
            #else the right must be smaller, append the right and increase the step j by 1
            else:
                output.append(right[j])
                j+=1
                count[0]+=(len(left)-i)

        #lists are exausted so add the rest to the ouput
        output += left[i:]
        output += right[j:]

        #return the output
        return output

    def merge_sort(input):

        #if the len of the input is less than 2 just return the input
        if len(input) < 2:
            return input

        #find the middle of the input
        middle = int(len(input) / 2)

        #make recursive calls
        left = merge_sort(input[:middle])
        right = merge_sort(input[middle:])

        #merge 
        D=merge(left, right)

        return D
    
    #call the merge_sort on the input
    merge_sort(input)
    
    #return the count
    return count[0]