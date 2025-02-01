---
tags: 
  - English
---
![[TOEFL REFORM]]
# Words
```dataview
LIST
FROM #English 
WHERE contains(file.path,"words")
SORT length(file.name) DESC,file.name
```
# Reading
```dataview
TABLE filename, finished
FROM #English 
WHERE contains(file.path,"Reading/")
SORT filename, finished
```
# Speaking
```dataview
LIST
FROM #English 
WHERE contains(file.path,"Speaking/")
```
# Writing
```dataview
LIST
FROM #English 
WHERE contains(file.path,"Writing/")
```

