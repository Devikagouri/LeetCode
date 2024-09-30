class Solution {
    char[] arr;int top=-1;
    public void push(char ch)
    {
        top+=1;
        arr[top]=ch;
    }
    
    public char pop()
    {
        if(top==-1)
            return '%';
        else
        {
            char ch = arr[top];
            top--;
            return ch;
        }
    }
    
    public boolean isValid(String s) {
        int l = s.length();
        arr = new char[l];
        for(int i=0;i<l;i++)
        {
            char ch = s.charAt(i);
            if(ch=='('||ch=='{'||ch=='[')
                push(ch);
            else if(ch==')'||ch=='}'||ch==']')
            {
                char x = pop();
                if(x=='%')
                    return false;
                else
                {
                    if(x=='(')
                    {
                        if(ch==')')
                            continue;
                        else
                            return false;
                    }
                    
                    else if(x=='{')
                    {
                        if(ch=='}')
                            continue;
                        else
                            return false;
                    } 
                    
                    else if(x=='[')
                    {
                        if(ch==']')
                            continue;
                        else
                            return false;
                    }
                   
                }
            }
        }
        char x = pop();
        if(x=='%')
            return true;
        else
            return false;
    }
}