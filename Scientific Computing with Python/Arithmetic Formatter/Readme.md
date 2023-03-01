Here is how you can use it:
```python
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
```
The first call to the function will print out the problems arranged vertically with no answers:
```diff
  32      3801      45      123    
+ 698    -    2    + 43    +  49    
-----    ------    ----    -----  
```
The second call to the function will print out the problems arranged vertically with the answers:
```diff
  32      3801      45      123    
+ 698    -    2    + 43    +  49    
-----    ------    ----    -----  
 730      3799      88      172    

```