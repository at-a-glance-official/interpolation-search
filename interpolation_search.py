def interpolation_search(arr,element):
    low = 0
    high = len(arr) - 1

    while low <= high:
        interpolation = low + (((high-low)*(element-arr[low]))//(arr[high]-arr[low]))
        if interpolation >= low and interpolation <= high:
            if arr[interpolation] == element:
                return f'Element found at index {interpolation}'
            elif arr[interpolation] > element:
                high = interpolation - 1
            elif arr[interpolation] < element:
                low = interpolation + 1
        else:
            return 'Element Not Found!'
    return 'Element Not Found!'

arr = [10,20,54,100,1000,5400]
print(interpolation_search(arr,878451659))