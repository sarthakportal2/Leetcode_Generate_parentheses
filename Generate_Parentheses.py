class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # T(C(N)=O(1)) 
        #new_approach
        #min runtime (35 ms) S(C(N)=O(N)) as it reuqires non coniguous memory allocation wihout iterating level wise 
        #using BST'dfs(depth First Search) Traversal approach
        def dfs(l,r,s):#dfs funct declare
            if len(s)==n*2:#appending the stack in output
                out.append(s);return
            if l<n:dfs(l+1,r,s+'(')#appending '(' to the stack's left child at most to its length 
            if r<l:dfs(l,r+1,s+')')#appending ')' to the stack's right child at most to its left child 

        out=[]#output list initilize
        dfs(0,0,'')#dfs funct declare
        return out#printing the output list 
        
        #old_apporaches
        # def rec(l,r,stack,cand):
        #     if l==r==0:out.append(cand);return
        #     elif l>0:rec(l-1,r,stack+1,cand+"(")
        #     elif r<0 and stack>0:rec(l,r-1,stack-1,cand+")")

        # rec(n,n,0,"")

        # return out
        
