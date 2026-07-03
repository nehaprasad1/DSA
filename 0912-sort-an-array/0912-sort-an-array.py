class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,l,m,h):
            a=[]
            left,right = l,m+1
            while left<=m and right <=h:
                if arr[left] <= arr[right]:
                    a.append(arr[left])
                    left+=1
                else:
                    a.append(arr[right])
                    right+=1
            while left<=m:
                a.append(arr[left])
                left+=1
            while right<=h:
                a.append(arr[right])
                right+=1
            for i in range(len(a)):
                arr[l + i] = a[i]



        def mergeSort(arr, l , h):
            if l >= h:
                return 
            m = (l+h) //2
            mergeSort(arr , l,m)
            mergeSort(arr,m+1,h)
            merge(arr,l,m,h)
        mergeSort(nums,0,len(nums)-1)
        return  nums
        