```python
from django.contrib import admin
from .models import SmartsheetData, ExcelData

admin.site.register(SmartsheetData)
admin.site.register(ExcelData)
```