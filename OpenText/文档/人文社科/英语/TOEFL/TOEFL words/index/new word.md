---
tags: 
  - English
---
```dataview
TASK
FROM #English
WHERE file.folder = this.file.folder
AND !completed
LIMIT 30
```
